from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    tweet_min_size: int
    tweet_max_size: int
    supabase_url: str
    supabase_key: str
    jwt_secret_key: str
    jwt_algorithms: List[str]
    jwt_audience: List[str]
    redis_host: str
    redis_port: int
    redis_password: str


settings = Settings()  # type: ignore
