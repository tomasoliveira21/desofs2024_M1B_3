from typing import List
from uuid import UUID

from fastapi import HTTPException, Request

from backend.application.exceptions import invalidSupabaseResponse
from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.logging import Logger
from backend.repository.hashtag_repository import HashtagRepository
from backend.repository.tweet_repository import TweetRepository


class TweetService:
    def __init__(self):
        self._tweet_repository = TweetRepository()
        self._hashtag_repository = HashtagRepository()
        self._logger = Logger().get_logger()

    def get_tweet(self, uuid: UUID, request: Request) -> TweetDto:
        self._logger.info(f'[{request.state.credentials["sub"]}] get tweet {uuid}')
        try:
            return self._tweet_repository.get_tweet(uuid=uuid, request=request)
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_tweets(self, request: Request) -> List[TweetDto]:
        self._logger.info(f'[{request.state.credentials["sub"]}] get all tweets')
        try:
            return self._tweet_repository.get_tweets(request=request)
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def create_tweet(self, tweet: Tweet, request: Request) -> TweetDto:
        self._logger.info(f'[{request.state.credentials["sub"]}] create tweet')
        try:
            created_tweet = self._tweet_repository.save_tweet(tweet, request=request)

            if tweet.hashtags:
                for hashtag in tweet.hashtags:
                    self._logger.info(
                        f'[{request.state.credentials["sub"]}] create hashtag'
                    )
                    self._hashtag_repository.save_hashtag(
                        hashtag=hashtag, tweet_uuid=created_tweet.uuid, request=request
                    )

            return created_tweet
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_tweet(self, tweet_id: int, request: Request) -> TweetDto:
        self._logger.info(
            f'[{request.state.credentials["sub"]}] delete tweet {tweet_id}'
        )
        try:
            return self._tweet_repository.delete_tweet(tweet_id, request=request)
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
