from typing import List
from uuid import UUID

from fastapi import Request
from pydantic import TypeAdapter

from backend.application.exceptions import InvalidSupabaseResponse
from backend.domain.hashtag import Hashtag, HashtagDto
from backend.infrastructure.logging import Logger
from backend.infrastructure.supabase_auth import SupabaseSingleton


class HashtagRepository:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(HashtagRepository, cls).__new__(cls)
            cls.__instance.__initialize_params()
        return cls.__instance

    def __initialize_params(self):
        self.__client = SupabaseSingleton().get_client()
        self.__adapter = TypeAdapter(List[HashtagDto])
        self.__logger = Logger().get_logger()

    def save_hashtag(self, hashtag: Hashtag, tweet_uuid: UUID, request: Request):
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            h = {"name": hashtag.name, "tweet_uuid": str(tweet_uuid)}
            response = self.__client.table("Hashtags").insert(h).execute()
            self.__client.auth.sign_out()
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise InvalidSupabaseResponse("Could not get tweets at this moment.")

    def get_hashtags(self, request: Request):
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = self.__client.table("Hashtags").select("*").execute()
            self.__client.auth.sign_out()
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise InvalidSupabaseResponse("Could not get tweets at this moment.")

    def get_trends(self, request: Request):
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = self.__client.table("trends").select("*").execute()
            self.__client.auth.sign_out()
            return response.data
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise InvalidSupabaseResponse("Could not get tweets at this moment.")
