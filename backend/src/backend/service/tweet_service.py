from typing import List
from uuid import UUID

from fastapi import HTTPException, Request

from backend.application.exceptions import invalidSupabaseResponse
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
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_tweets(self, request: Request) -> List[TweetDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get all tweets")
        try:
            with single_read_object(
                self.__tweet_repository.get_tweets(request=request)
            ) as tweets:
                return tweets
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def create_tweet(self, tweet: Tweet, request: Request) -> TweetDto:
        self.__logger.info(f"[{request.state.credentials['sub']}] save tweet")
        try:
            with single_read_object(
                self.__tweet_repository.save_tweet(tweet, request=request)
            ) as created_tweet:
                if tweet.hashtags:
                    self.__hashtag_service.save_hashtags(
                        hashtags=tweet.hashtags,
                        tweet_uuid=created_tweet.uuid,
                        request=request,
                    )
                return created_tweet
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_tweet(self, tweet_id: UUID, request: Request) -> TweetDto:
        self.__logger.info(
            f"[{request.state.credentials['sub']}] delete tweet {tweet_id}"
        )
        try:
            with single_read_object(
                self.__tweet_repository.delete_tweet(tweet_id, request=request)
            ) as deleted_tweet:
                return deleted_tweet
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
