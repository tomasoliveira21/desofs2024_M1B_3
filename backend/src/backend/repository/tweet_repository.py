from typing import List
from uuid import UUID

from fastapi import Request
from pydantic import TypeAdapter

from backend.application.exceptions import invalidSupabaseResponse
from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.logging import Logger
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
        self.__logger = Logger().get_logger()

    def get_tweet(self, uuid: UUID, request: Request) -> TweetDto:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        try:
            response = (
                self.__client.table("Tweets").select("*").eq("uuid", uuid).execute()
            )
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f'teste user: {request.state.credentials["sub"]} - {e}')
            raise invalidSupabaseResponse("Could not get tweets at this moment.")

    def get_tweets(self, request: Request) -> List[TweetDto]:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        try:
            response = self.__client.table("Tweets").select("*").execute()
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f'teste user: {request.state.credentials["sub"]} - {e}')
            raise invalidSupabaseResponse("Could not get tweets at this moment.")

    def save_tweet(self, tweet: Tweet, request: Request) -> TweetDto:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = (
                self.__client.table("Tweets")
                .insert(tweet.model_dump(exclude={"hashtags"}))
                .execute()
            )
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f'[{request.state.credentials["sub"]}] {e}')
            raise invalidSupabaseResponse("Could not save the tweet at this moment.")

    def delete_tweet(self, id: int, request: Request) -> TweetDto:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = self.__client.table("Tweets").delete().eq("id", id).execute()
            print(response)
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f'[{request.state.credentials["sub"]}] {e}')
            raise invalidSupabaseResponse("Could not delete the tweet at this moment.")
