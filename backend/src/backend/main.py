import redis.asyncio as redis
from fastapi import APIRouter, Depends, FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

from backend.application.auth import JWTBearer
from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.config import settings
from backend.service.hashtag_service import HashtagService
from backend.service.tweet_service import TweetService


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_connection = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
        encoding="utf-8",
        decode_responses=True,
    )
    await FastAPILimiter.init(redis_connection)
    yield


app = FastAPI(
    title="SocialNet - Backend",
    description="The Backend for the SocialNet application",
    dependencies=[Depends(JWTBearer()), Depends(RateLimiter(times=20, seconds=5))],
    lifespan=lifespan,
)

tweet_router = APIRouter(prefix="/tweet", tags=["Tweets"])
hashtag_router = APIRouter(prefix="/hashtag", tags=["Hashtag"])

# SERVICES
tweet_service = TweetService()
hashtag_service = HashtagService()


# TWEETS
@tweet_router.get("")
def get_tweets():
    return tweet_service.get_all_tweets()


@tweet_router.post("")
def post_tweet(tweet: Tweet) -> TweetDto:
    return tweet_service.create_tweet(tweet=tweet)


@tweet_router.delete("")
def delete_tweet(id: int) -> TweetDto:
    return tweet_service.remove_tweet(tweet_id=id)


# HASHTAGS
@hashtag_router.get("")
def get_hashtags():
    return hashtag_service.get_hashtags()


@hashtag_router.get("/trends")
def get_trends():
    return hashtag_service.get_trends()


# ROUTERS
app.include_router(tweet_router)
app.include_router(hashtag_router)
