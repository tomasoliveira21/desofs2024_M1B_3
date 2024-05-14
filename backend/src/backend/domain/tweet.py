import re
from datetime import datetime
from typing import Annotated, List

from pydantic import BaseModel, StringConstraints, TypeAdapter

from backend.domain.hashtag import Hashtag
from backend.infrastructure.config import settings


class Tweet(BaseModel):
    content: Annotated[
        str,
        StringConstraints(
            min_length=settings.tweet_min_size,
            max_length=settings.tweet_max_size,
        ),
    ]

    @property
    def hashtags(self) -> List[Hashtag]:
        return TypeAdapter(List[Hashtag]).validate_python(
            [{"name": h} for h in re.findall(r"#(\w+)", self.content)]
        )


class TweetDto(Tweet):
    id: int
    created_at: datetime
