from typing import List
from uuid import UUID

from fastapi import HTTPException, Request

from backend.application.exceptions import invalidSupabaseResponse
from backend.application.utils import single_read_object
from backend.domain.hashtag import Hashtag, HashtagDto
from backend.infrastructure.logging import Logger
from backend.repository.hashtag_repository import HashtagRepository


class HashtagService:
    def __init__(self):
        self._repository = HashtagRepository()
        self._logger = Logger().get_logger()

    def save_hashtags(
        self,
        hashtags: List[Hashtag] | Hashtag,
        tweet_uuid: UUID,
        request: Request,
    ):
        self._logger.info(f'[{request.state.credentials["sub"]}] save hashtags')
        if not isinstance(hashtags, list):
            hashtags = [hashtags]
        try:
            for hashtag in hashtags:
                with single_read_object(
                    self._repository.save_hashtag(
                        hashtag=hashtag, tweet_uuid=tweet_uuid, request=request
                    )
                ):
                    pass
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_hashtags(self, request: Request) -> List[HashtagDto]:
        self._logger.info(f'[{request.state.credentials["sub"]}] get all hashtags')
        try:
            with single_read_object(
                self._repository.get_hashtags(request=request)
            ) as hashtags:
                return hashtags
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_trends(self, request: Request) -> List[HashtagDto]:
        self._logger.info(f'[{request.state.credentials["sub"]}] get trends')
        try:
            with single_read_object(
                self._repository.get_trends(request=request)
            ) as trends:
                return trends
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
