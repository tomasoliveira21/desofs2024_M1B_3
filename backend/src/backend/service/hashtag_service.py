from typing import List

from backend.domain.hashtag import HashtagDto
from backend.repository.hashtag_repository import HashtagRepository
from fastapi import Request


class HashtagService:
    def __init__(self):
        self._repository = HashtagRepository()

    def get_hashtags(self, request: Request) -> List[HashtagDto]:
        return self._repository.get_hashtags(request=request)

    def get_trends(self, request: Request) -> List[HashtagDto]:
        return self._repository.get_trends(request=request)
