from typing import List
from uuid import UUID

import redis.asyncio as redis
from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

from backend.application.auth import JWTBearer
from backend.domain.hashtag import HashtagDto
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tweet_router = APIRouter(prefix="/tweet", tags=["Tweets"])
hashtag_router = APIRouter(prefix="/hashtag", tags=["Hashtag"])

# SERVICES
tweet_service = TweetService()
hashtag_service = HashtagService()


# TWEETS
@tweet_router.get("/{uuid}")
def get_tweet(uuid: UUID, request: Request) -> TweetDto:
    return tweet_service.get_tweet(uuid=uuid, request=request)


@tweet_router.get("")
def get_tweets(request: Request) -> List[TweetDto]:
    return tweet_service.get_all_tweets(request=request)


@tweet_router.post("")
def post_tweet(tweet: Tweet, request: Request) -> TweetDto:
    return tweet_service.create_tweet(tweet=tweet, request=request)


@tweet_router.delete("")
def delete_tweet(uuid: int, request: Request) -> TweetDto:
    return tweet_service.delete_tweet(tweet_id=uuid, request=request)


# HASHTAGS
@hashtag_router.get("")
def get_hashtags(request: Request) -> List[HashtagDto]:
    return hashtag_service.get_hashtags(request=request)


@hashtag_router.get("/trends")
def get_trends(request: Request) -> List[HashtagDto]:
    return hashtag_service.get_trends(request=request)


# ROUTERS
app.include_router(tweet_router)
app.include_router(hashtag_router)
