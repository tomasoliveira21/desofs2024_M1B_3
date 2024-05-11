from typing import List

from backend.domain.tweet import Tweet, TweetDto
from pydantic import TypeAdapter
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions


class TweetRepository:
    __client: Client
    __adapter: TypeAdapter

    def __init__(self):
        opts = ClientOptions().replace(schema="socialnet")
        self.__client = create_client(
            # TODO: change this to be a singleton and remove hardcoded values
            supabase_url="http://127.0.0.1:8000",
            supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q",
            options=opts,
        )
        self.__client.postgrest.schema("socialnet")
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
