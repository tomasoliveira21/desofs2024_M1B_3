from typing import List

from fastapi import HTTPException, Request

from backend.application.exceptions import invalidSupabaseResponse
from backend.domain.hashtag import HashtagDto
from backend.infrastructure.logging import Logger
from backend.repository.hashtag_repository import HashtagRepository


class HashtagService:
    def __init__(self):
        self._repository = HashtagRepository()
        self._logger = Logger().get_logger()

    def get_hashtags(self, request: Request) -> List[HashtagDto]:
        self._logger.info(f'[{request.state.credentials["sub"]}] get all hashtags')
        try:
            return self._repository.get_hashtags(request=request)
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_trends(self, request: Request) -> List[HashtagDto]:
        self._logger.info(f'[{request.state.credentials["sub"]}] get trends')
        try:
            return self._repository.get_trends(request=request)
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
