from typing import List

from backend.domain.hashtag import HashtagDto
from backend.repository.hashtag_repository import HashtagRepository


class HashtagService:
    def __init__(self):
        self._repository = HashtagRepository()

    def get_hashtags(self) -> List[HashtagDto]:
        return self._repository.get_hashtags()

    def get_trends(self) -> List[HashtagDto]:
        return self._repository.get_trends()
