from tempfile import NamedTemporaryFile
from typing import List
from uuid import UUID

from fastapi import Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import TypeAdapter

from backend.application.exceptions import invalidSupabaseResponse
from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.logging import Logger
from backend.infrastructure.supabase_auth import SupabaseSingleton


class TweetRepository:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(TweetRepository, cls).__new__(cls)
            cls.__instance.__initialize_params()
        return cls.__instance

    def __initialize_params(self):
        self.__client = SupabaseSingleton().get_client()
        self.__adapter = TypeAdapter(List[TweetDto])
        self.__logger = Logger().get_logger()

    def get_tweet(self, uuid: UUID, request: Request) -> TweetDto:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = (
                self.__client.table("Tweets").select("*").eq("uuid", uuid).execute()
            )
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse("tweets at this moment.")

    def get_all_tweets(self, request: Request) -> List[TweetDto]:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = self.__client.table("Tweets").select("*").execute()
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse("Could not get tweets at this moment.")

    def get_self_tweets(self, request: Request) -> List[TweetDto]:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = (
                self.__client.table("Tweets")
                .select("*")
                .eq("user_uuid", request.state.user.id)
                .execute()
            )
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse("Could not get tweets at this moment.")

    def get_user_tweets(self, user_uuid: UUID, request: Request) -> List[TweetDto]:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = (
                self.__client.table("Tweets")
                .select("*")
                .eq("user_uuid", user_uuid)
                .execute()
            )
            return self.__adapter.validate_python(response.data)
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
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
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse("Could not save the tweet at this moment.")

    def delete_tweet(self, uuid: UUID, request: Request) -> TweetDto:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            response = self.__client.table("Tweets").delete().eq("id", uuid).execute()
            print(response)
            return self.__adapter.validate_python(response.data)[0]
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse("Could not delete the tweet at this moment.")

    def save_image(
        self, request: Request, uuid: UUID, image: UploadFile
    ) -> JSONResponse:
        with NamedTemporaryFile(
            delete=True,
        ) as tmp_image:
            try:
                self.__client.auth.set_session(
                    access_token=request.state.jwt, refresh_token=""
                )
                path = f"tweets/{uuid}"
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
                raise invalidSupabaseResponse("Error on uploading the tweet image")
            finally:
                image.file.close()
        return JSONResponse(status_code=200, content={"message": path})

    def get_image(self, request: Request, uuid: UUID) -> FileResponse:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            with NamedTemporaryFile(delete=False, mode="wb+") as tmp_image:
                res = self.__client.storage.from_("socialnet").download(
                    f"tweets/{uuid}"
                )
                tmp_image.write(res)
                return FileResponse(tmp_image.name, media_type="image/png")
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse(
                "Could not get the tweet image at this moment."
            )

    def has_image(self, uuid: UUID, request: Request) -> bool:
        try:
            self.__client.auth.set_session(
                access_token=request.state.jwt, refresh_token=""
            )
            res = self.__client.storage.from_("socialnet").list(path="tweets")
            if len(res) > 0:
                for file in res:
                    if file.get("name") == str(uuid):
                        return True
            return False
        except Exception as e:
            self.__logger.error(f"[{request.state.credentials['sub']}] {e}")
            raise invalidSupabaseResponse(
                "Could not confirm tweet has image at this moment."
            )
