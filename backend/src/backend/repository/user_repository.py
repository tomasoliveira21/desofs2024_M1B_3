from typing import List

from fastapi import Request
from pydantic import TypeAdapter

from backend.application.exceptions import invalidSupabaseResponse
from backend.domain.user import UserDto
from backend.infrastructure.logging import Logger
from backend.infrastructure.supabase_auth import SupabaseSingleton


class UserRepository:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(UserRepository, cls).__new__(cls)
            cls.__instance.__initialize_params()
        return cls.__instance

    def __initialize_params(self):
        self.__client = SupabaseSingleton().get_client()
        self.__adapter = TypeAdapter(List[UserDto])
        self.__logger = Logger().get_logger()

    def get_self_user(self, request: Request):
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
            raise invalidSupabaseResponse("Could not get user at this moment.")

    def get_all_users(self, request: Request) -> List[UserDto]:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        try:
            response = self.__client.table("users").select("*").execute()
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse("Could not get users at this moment.")
