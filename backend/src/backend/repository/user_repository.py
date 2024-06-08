from tempfile import NamedTemporaryFile
from typing import List

from fastapi import Request, UploadFile
from fastapi.responses import JSONResponse
from pydantic import TypeAdapter
from storage3.utils import StorageException

from backend.application.exceptions import (
    InvalidSupabaseResponse,
    ProfilePictureNotFound,
)
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
            raise InvalidSupabaseResponse("Could not get user at this moment.")

    def get_all_users(self, request: Request) -> List[UserDto]:
        self.__client.auth.set_session(access_token=request.state.jwt, refresh_token="")
        try:
            response = self.__client.table("users").select("*").execute()
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise InvalidSupabaseResponse("Could not get users at this moment.")

    def save_profile_picture(self, request: Request, image: UploadFile):
        with NamedTemporaryFile(
            delete=True,
        ) as tmp_image:
            try:
                self.__client.auth.set_session(
                    access_token=request.state.jwt, refresh_token=""
                )
                path = f"profile_pictures/{request.state.user.id}"
                contents = image.file.read()
                tmp_image.write(contents)
                self.__client.storage.from_("socialnet").upload(
                    path=path,
                    file=tmp_image.name,
                    file_options={"content-type": image.content_type}
                    if image.content_type
                    else None,
                )
            except Exception:
                raise InvalidSupabaseResponse("Error on uploading the image")
            finally:
                image.file.close()
        return JSONResponse(status_code=200, content={"message": path})

    def get_profile_picture(self, request: Request) -> str | None:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            res = self.__client.storage.from_("socialnet").create_signed_url(
                f"profile_pictures/{request.state.user.id}", expires_in=3600
            )
            return res.get("signedURL", None)
        except StorageException as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise ProfilePictureNotFound("User does not have a profile picture.")
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise InvalidSupabaseResponse(
                "Could not get profile picture at this moment."
            )
