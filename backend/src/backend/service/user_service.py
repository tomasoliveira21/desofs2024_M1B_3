from typing import List

from fastapi import HTTPException, Request

from backend.application.exceptions import invalidSupabaseResponse
from backend.application.utils import single_read_object
from backend.domain.user import UserDto
from backend.infrastructure.logging import Logger
from backend.repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self._repository = UserRepository()
        self._logger = Logger().get_logger()

    def get_user(self, request: Request) -> List[UserDto]:
        self._logger.info(f'[{request.state.credentials["sub"]}] get user')
        try:
            with single_read_object(
                self._repository.get_user(request=request)
            ) as trends:
                return trends
        except invalidSupabaseResponse as e:
            raise HTTPException(status_code=500, detail=str(e))
