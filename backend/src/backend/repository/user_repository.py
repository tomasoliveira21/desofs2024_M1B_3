from typing import List

from fastapi import Request
from pydantic import TypeAdapter

from backend.application.exceptions import invalidSupabaseUser
from backend.domain.user import UserDto
from backend.infrastructure.logging import Logger
from backend.infrastructure.supabase_auth import SupabaseSingleton


class UserRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRepository, cls).__new__(cls)
            cls._instance._initialize_params()
        return cls._instance

    def _initialize_params(self):
        self.__client = SupabaseSingleton().get_client()
        self.__adapter = TypeAdapter(List[UserDto])
        self.__logger = Logger().get_logger()

    def get_user(self, request: Request):
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        try:
            response = (
                self.__client.table("users")
                .select("*")
                .eq("id", request.state.credentials["sub"])
                .execute()
            )
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f'request.state.credentials["sub"] {e}')
            raise invalidSupabaseUser("Could not get user at this moment.")
