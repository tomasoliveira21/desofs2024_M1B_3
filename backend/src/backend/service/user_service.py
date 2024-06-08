from typing import List

from fastapi import HTTPException, Request, UploadFile
from pydantic_core import Url
from storage3.utils import StorageException

from backend.application.exceptions import InvalidSupabaseResponse
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
            ) as user:
                return user
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_users(self, request: Request) -> List[UserDto]:
        self.__logger.info(f"[{request.state.credentials['sub']}] get all users")
        try:
            with single_read_object(
                self.__repository.get_all_users(request=request)
            ) as users:
                return users
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def save_profile_picture(self, request: Request, image: UploadFile):
        self.__logger.info(f"[{request.state.credentials['sub']}] save profile picture")
        try:
            with single_read_object(
                self.__repository.save_profile_picture(request=request, image=image)
            ) as pfpicture:
                return pfpicture
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_profile_picture(self, request: Request) -> Url:
        self.__logger.info(f"[{request.state.credentials['sub']}] get profile picture")
        try:
            with single_read_object(
                self.__repository.get_profile_picture(request=request)
            ) as pfpicture:
                return Url(url=pfpicture)
        except StorageException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except InvalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
