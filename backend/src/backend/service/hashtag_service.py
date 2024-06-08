from typing import List
from uuid import UUID

from fastapi import HTTPException, Request

from backend.application.exceptions import InvalidSupabaseResponse
from backend.application.utils import single_read_object
from backend.domain.hashtag import Hashtag, HashtagDto
from backend.infrastructure.logging import Logger
from backend.infrastructure.supabase_auth import SupabaseSingleton
from backend.repository.hashtag_repository import HashtagRepository


class HashtagService:
    def __init__(self):
        self.__client = SupabaseSingleton().get_client()
        self.__repository = HashtagRepository()
        self.__logger = Logger().get_logger()

    def save_hashtags(
        self,
        hashtags: List[Hashtag] | Hashtag,
        tweet_uuid: UUID,
        request: Request,
    ):
        self.__logger.info(f"[{request.state.credentials['sub']}] save hashtags")
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        if not isinstance(hashtags, list):
            hashtags = [hashtags]
        try:
            for hashtag in hashtags:
                with single_read_object(
                    self.__repository.save_hashtag(
                        hashtag=hashtag, tweet_uuid=tweet_uuid, request=request
                    )
                ):
                    pass
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_hashtags(self, request: Request) -> List[HashtagDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get all hashtags")
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        try:
            with single_read_object(
                self.__repository.get_hashtags(request=request)
            ) as hashtags:
                return hashtags
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_trends(self, request: Request) -> List[HashtagDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get trends")
        try:
            with single_read_object(
                self.__repository.get_trends(request=request)
            ) as trends:
                return trends
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
