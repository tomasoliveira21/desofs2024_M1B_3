
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Hashtag(BaseModel):
    name: str

class HashtagDto(Hashtag):
    id: int
    tweet_uuid: UUID
    created_at: datetime