from typing import List

from pydantic import TypeAdapter

from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.supabase_auth import SupabaseSingleton


class TweetRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TweetRepository, cls).__new__(cls)
            cls._instance._initialize_params()
        return cls._instance

    def _initialize_params(self):
        self.client = SupabaseSingleton().get_client()
        self.adapter = TypeAdapter(List[TweetDto])

    def get_tweets(self) -> List[TweetDto]:
        response = self.client.table("Tweets").select("*").execute()
        return self.adapter.validate_python(response.data)

    def save_tweet(self, tweet: Tweet) -> TweetDto:
        response = self.client.table("Tweets").insert(tweet.model_dump()).execute()
        return self.adapter.validate_python(response.data)[0]

    def delete_tweet(self, id: int) -> TweetDto:
        response = self.client.table("Tweets").delete().eq("id", id).execute()
        return self.adapter.validate_python(response.data)[0]
