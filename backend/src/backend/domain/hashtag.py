
from datetime import datetime

from pydantic import BaseModel


class Hashtag(BaseModel):
    name: str

class HashtagDto(Hashtag):
    id: int
    tweet_id: int
    created_at: datetime