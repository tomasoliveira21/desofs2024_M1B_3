from socialNet_backend.app import config
from socialnet.redis.connection import configure_connection


def setup_redis():
    default_redis_alias = 'default'

    configure_connection(
        default_redis_alias,
        url=config.REDIS_URL
    )
