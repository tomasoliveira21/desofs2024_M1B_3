from backend.infrastructure.config import settings
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions


class SupabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseSingleton, cls).__new__(cls)
            cls._instance._initialize_clients()
        return cls._instance

    def _initialize_clients(self):
        self.client_auth: Client = create_client(
            supabase_url=settings.supabase_auth_url,
            supabase_key=settings.supabase_auth_key,
        )
        self.client_db: Client = create_client(
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key,
            options=ClientOptions().replace(schema="socialnet"),
        )

    @staticmethod
    def get_client_db() -> Client:
        instance = SupabaseSingleton()
        return instance.client_db

    @staticmethod
    def get_client_auth() -> Client:
        instance = SupabaseSingleton()
        return instance.client_db