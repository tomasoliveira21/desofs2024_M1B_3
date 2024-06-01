from typing import List

from fastapi import Request
from pydantic import TypeAdapter

from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.supabase_auth import SupabaseSingleton


class TweetRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TweetRepository, cls).__new__(cls)
            cls._instance._initialize_params()
        return cls._instance

    def _initialize_params(self):
        self.__client = SupabaseSingleton().get_client()
        self.__adapter = TypeAdapter(List[TweetDto])

    def get_tweets(self, request: Request) -> List[TweetDto]:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        response = self.__client.table("Tweets").select("*").execute()
        return self.__adapter.validate_python(response.data)

    def save_tweet(self, tweet: Tweet, request: Request) -> TweetDto:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        response = self.__client.table("Tweets").insert(tweet.model_dump()).execute()
        return self.__adapter.validate_python(response.data)[0]

    def delete_tweet(self, id: int, request: Request) -> TweetDto:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        response = self.__client.table("Tweets").delete().eq("id", id).execute()
        print(response)
        return self.__adapter.validate_python(response.data)[0]
