import os
from typing import List

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f".env.{ENVIRONMENT}", env_file_encoding="utf-8"
    )
    tweet_min_size: int
    tweet_max_size: int
    supabase_url: HttpUrl
    supabase_key: str
    jwt_secret_key: str
    jwt_algorithms: List[str]
    jwt_audience: List[str]


settings = Settings()  # type: ignore
