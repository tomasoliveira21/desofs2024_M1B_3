from typing import List
from uuid import UUID

from fastapi import HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse
from pydantic_core import Url
from storage3.utils import StorageException

from backend.application.exceptions import InvalidSupabaseResponse
from backend.application.utils import single_read_object
from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.logging import Logger
from backend.repository.tweet_repository import TweetRepository
from backend.service.hashtag_service import HashtagService


class TweetService:
    def __init__(self):
        self.__tweet_repository = TweetRepository()
        self.__hashtag_service = HashtagService()
        self.__logger = Logger().get_logger()

    def get_tweet(self, uuid: UUID, request: Request) -> TweetDto:
        self.__logger.info(f"[{request.state.credentials['sub']}] get tweet {uuid}")
        try:
            with single_read_object(
                self.__tweet_repository.get_tweet(uuid=uuid, request=request)
            ) as tweet:
                return tweet
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_tweets(self, request: Request) -> List[TweetDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get all tweets")
        try:
            with single_read_object(
                self.__tweet_repository.get_all_tweets(request=request)
            ) as tweets:
                return tweets
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_user_tweet(self, user_uuid: UUID, request: Request) -> List[TweetDto]:
        self.__logger.info(
            f"[{request.state.credentials['sub']}] get user {user_uuid} tweets"
        )
        try:
            with single_read_object(
                self.__tweet_repository.get_user_tweets(
                    user_uuid=user_uuid, request=request
                )
            ) as tweets:
                return tweets
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_self_tweet(self, request: Request) -> List[TweetDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get self tweets")
        try:
            with single_read_object(
                self.__tweet_repository.get_self_tweets(request=request)
            ) as tweets:
                return tweets
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def create_tweet(self, tweet: Tweet, request: Request) -> TweetDto:
        self.__logger.info(f"[{request.state.credentials['sub']}] save tweet")
        try:
            with single_read_object(
                self.__tweet_repository.save_tweet(tweet=tweet, request=request)
            ) as created_tweet:
                if tweet.hashtags:
                    self.__hashtag_service.save_hashtags(
                        hashtags=tweet.hashtags,
                        tweet_uuid=created_tweet.uuid,
                        request=request,
                    )
                return created_tweet
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_tweet(self, uuid: UUID, request: Request) -> TweetDto:
        self.__logger.info(f"[{request.state.credentials['sub']}] delete tweet {uuid}")
        try:
            with single_read_object(
                self.__tweet_repository.delete_tweet(uuid=uuid, request=request)
            ) as deleted_tweet:
                return deleted_tweet
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def save_image(
        self, request: Request, uuid: UUID, image: UploadFile
    ) -> JSONResponse:
        self.__logger.info(f"[{request.state.credentials['sub']}] save tweet image")
        try:
            with single_read_object(
                self.__tweet_repository.save_image(
                    request=request, uuid=uuid, image=image
                )
            ) as uploaded_image:
                return uploaded_image
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_image(self, request: Request, uuid: UUID) -> Url:
        self.__logger.info(f"[{request.state.credentials['sub']}] get tweet image")
        try:
            with single_read_object(
                self.__tweet_repository.get_image(request=request, uuid=uuid)
            ) as image:
                return Url(url=image)
        except StorageException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
