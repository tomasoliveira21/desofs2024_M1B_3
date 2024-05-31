from typing import List

from pydantic import TypeAdapter

from backend.domain.hashtag import Hashtag, HashtagDto
from backend.infrastructure.supabase_auth import SupabaseSingleton


class HashtagRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HashtagRepository, cls).__new__(cls)
            cls._instance._initialize_params()
        return cls._instance

    def _initialize_params(self):
        self.__client = SupabaseSingleton().get_client()
        self.__adapter = TypeAdapter(List[HashtagDto])

    def save_hashtag(self, hashtag: Hashtag, tweet_id: int):
        h = {"name": hashtag.name, "tweet_id": tweet_id}
        print(h)
        response = self.__client.table("Hashtags").insert(h).execute()
        return self.__adapter.validate_python(response.data)[0]

    def get_hashtags(self):
        response = self.__client.table("Hashtags").select("*").execute()
        return self.__adapter.validate_python(response.data)

    def get_trends(self):
        response = self.__client.table("trends").select("*").execute()
        return response.data
