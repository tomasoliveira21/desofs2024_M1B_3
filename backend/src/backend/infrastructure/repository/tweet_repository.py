from typing import List

from pydantic import TypeAdapter

from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.config import settings
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions


class TweetRepository:
    __client: Client
    __adapter: TypeAdapter

    def __init__(self):
        opts = ClientOptions().replace(schema="socialnet")
        self.__client = create_client(
            # TODO: change this to be a singleton and remove hardcoded values
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key,
            options=opts,
        )
        self.__adapter = TypeAdapter(List[TweetDto])

    def get_tweets(self) -> List[TweetDto]:
        response = self.__client.table("Tweets").select("*").execute()
        return self.__adapter.validate_python(response.data)

    def save_tweet(self, tweet: Tweet) -> TweetDto:
        response = self.__client.table("Tweets").insert(tweet.model_dump()).execute()
        return self.__adapter.validate_python(response.data)[0]

    def delete_tweet(self, id: int) -> TweetDto:
        response = self.__client.table("Tweets").delete().eq("id", id).execute()
        return self.__adapter.validate_python(response.data)[0]
