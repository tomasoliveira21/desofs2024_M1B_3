
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions

from backend.infrastructure.config import settings


class SupabaseSingleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SupabaseSingleton, cls).__new__(cls)
            cls.__instance.__initialize_client()
        return cls.__instance

    def __initialize_client(self):
        self.__client: Client = create_client(
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key,
            options=ClientOptions().replace(schema="socialnet"),
        )

    @staticmethod
    def get_client() -> Client:
        instance = SupabaseSingleton()
        return instance.__client
