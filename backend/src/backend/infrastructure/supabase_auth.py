from backend.infrastructure.config import settings
from supabase import Client, create_client
from supabase._sync.client import SyncClient
from supabase.lib.client_options import ClientOptions


class SupabaseSingleton:
    _instance = None
    _client: SyncClient

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseSingleton, cls).__new__(cls)
            cls._instance._initialize_clients()
        return cls._instance

    def _initialize_clients(self):
        if self._client is None:
            self._client: Client = create_client(
                supabase_url=settings.supabase_url,
                supabase_key=settings.supabase_key,
                options=ClientOptions().replace(schema="socialnet"),
            )

    @staticmethod
    def get_client() -> Client:
        instance = SupabaseSingleton()
        return instance._client
