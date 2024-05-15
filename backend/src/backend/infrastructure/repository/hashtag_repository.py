from typing import List

from pydantic import TypeAdapter

from backend.domain.hashtag import Hashtag, HashtagDto
from backend.infrastructure.config import settings
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions


class HashtagRepository:
    __client: Client
    __adapter: TypeAdapter

    def __init__(self):
        opts = ClientOptions().replace(schema="socialnet")
        self.__client = create_client(
            # TODO: change this to be a singleton and remove hardcoded values
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key,
            options=opts,
        )
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
        """
        DROP VIEW IF EXISTS socialnet.trends;
        CREATE VIEW socialnet.trends AS
        SELECT
            name,
            COUNT(*) AS count,
            ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS position
        FROM     socialnet."Hashtags"
        WHERE    created_at >= Now() - interval '1 DAYS'
        group BY name
        ORDER BY count DESC limit 10;
        """
        response = self.__client.table("trends").select("*").execute()
        return response.data
