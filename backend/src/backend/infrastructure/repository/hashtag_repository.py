from datetime import datetime, timedelta
from os import name
from typing import List

from backend.domain.hashtag import Hashtag, HashtagDto
from pydantic import TypeAdapter
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions


class HashtagRepository:
    __client: Client
    __adapter: TypeAdapter

    def __init__(self):
        opts = ClientOptions().replace(schema="socialnet")
        self.__client = create_client(
            # TODO: change this to be a singleton and remove hardcoded values
            supabase_url="http://127.0.0.1:8000",
            supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q",
            options=opts,
        )
        self.__client.postgrest.schema("socialnet")
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
        query = """
            SELECT name, COUNT(*) as count
            FROM socialnet."Hashtags"
            WHERE created_at >= now() - INTERVAL '1 DAYS'
            GROUP BY name
            ORDER BY count DESC
            LIMIT 10
        """
        response = self.__client.table("Hashtags").select()
        return response
