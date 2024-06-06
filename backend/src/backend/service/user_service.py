from typing import List

from fastapi import HTTPException, Request

from backend.application.exceptions import invalidSupabaseResponse
from backend.application.utils import single_read_object
from backend.domain.user import UserDto
from backend.infrastructure.logging import Logger
from backend.repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.__repository = UserRepository()
        self.__logger = Logger().get_logger()

    def get_self_user(self, request: Request) -> List[UserDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get self user")
        try:
            with single_read_object(
                self.__repository.get_self_user(request=request)
            ) as trends:
                return trends
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_users(self, request: Request) -> List[UserDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get all users")
        try:
            with single_read_object(
                self.__repository.get_all_users(request=request)
            ) as trends:
                return trends
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))