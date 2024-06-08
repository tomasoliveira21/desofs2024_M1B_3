from typing import List
from uuid import UUID

import redis.asyncio as redis
from fastapi import APIRouter, Depends, FastAPI, Request, UploadFile
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from pydantic_core import Url

from backend.application.auth import JWTBearer
from backend.application.rbac import RBAC
from backend.domain.hashtag import HashtagDto
from backend.domain.tweet import Tweet, TweetDto
from backend.domain.user import UserRole
from backend.infrastructure.config import settings
from backend.service.hashtag_service import HashtagService
from backend.service.tweet_service import TweetService
from backend.service.user_service import UserService


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_connection = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
        encoding="utf-8",
        decode_responses=True,
    )
    try:
        await FastAPILimiter.init(redis_connection, prefix="fastapi-limiter")
        yield
    finally:
        await redis_connection.aclose()


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
user_router = APIRouter(prefix="/user", tags=["User"])

# SERVICES
tweet_service = TweetService()
hashtag_service = HashtagService()
user_service = UserService()


# TWEETS
@tweet_router.get("/all", dependencies=[Depends(RBAC(minimum_role=UserRole.default))])
def get_tweets(request: Request) -> List[TweetDto]:
    return tweet_service.get_all_tweets(request=request)


@tweet_router.get(
    "/{uuid}", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def get_tweet(uuid: UUID, request: Request) -> TweetDto:
    return tweet_service.get_tweet(uuid=uuid, request=request)


@tweet_router.get(
    "/user/self", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def get_self_tweets(request: Request) -> List[TweetDto]:
    return tweet_service.get_self_tweet(request=request)


@tweet_router.get(
    "/user/{user_uuid}", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def get_user_tweets(user_uuid: UUID, request: Request) -> List[TweetDto]:
    return tweet_service.get_user_tweet(user_uuid=user_uuid, request=request)


@tweet_router.post("", dependencies=[Depends(RBAC(minimum_role=UserRole.default))])
def post_tweet(
    tweet: Tweet,
    request: Request,
) -> TweetDto:
    return tweet_service.create_tweet(tweet=tweet, request=request)


@tweet_router.post(
    "/{uuid}/image", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def post_image(
    uuid: UUID,
    image: UploadFile,
    request: Request,
):
    return tweet_service.save_image(request=request, uuid=uuid, image=image)


@tweet_router.delete("", dependencies=[Depends(RBAC(minimum_role=UserRole.admin))])
def delete_tweet(uuid: UUID, request: Request) -> TweetDto:
    return tweet_service.delete_tweet(uuid=uuid, request=request)


@tweet_router.get(
    "/{uuid}/image", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def get_image(uuid: UUID, request: Request) -> Url:
    return tweet_service.get_image(request=request, uuid=uuid)


# HASHTAGS
@hashtag_router.get("", dependencies=[Depends(RBAC(minimum_role=UserRole.default))])
def get_hashtags(request: Request) -> List[HashtagDto]:
    return hashtag_service.get_hashtags(request=request)


@hashtag_router.get(
    "/trends", dependencies=[Depends(RBAC(minimum_role=UserRole.premium))]
)
def get_trends(request: Request):
    return hashtag_service.get_trends(request=request)


# USERS
@user_router.get("/self", dependencies=[Depends(RBAC(minimum_role=UserRole.default))])
def get_self_user(request: Request):
    return request.state.user


@user_router.get("/all", dependencies=[Depends(RBAC(minimum_role=UserRole.default))])
def get_users(request: Request):
    return user_service.get_all_users(request=request)


@user_router.get("/{uuid}", dependencies=[Depends(RBAC(minimum_role=UserRole.default))])
def get_user(request: Request, uuid: UUID):
    return user_service.get_user(uuid=uuid, request=request)


@user_router.post(
    "/profile_picture", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def post_profile_picture(image: UploadFile, request: Request):
    return user_service.save_profile_picture(request=request, image=image)


@user_router.get(
    "/profile_picture", dependencies=[Depends(RBAC(minimum_role=UserRole.default))]
)
def get_profile_picture(request: Request) -> Url:
    return user_service.get_profile_picture(request=request)


# ROUTERS
app.include_router(tweet_router)
app.include_router(hashtag_router)
app.include_router(user_router)
