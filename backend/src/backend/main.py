from fastapi import APIRouter, FastAPI

from backend.domain.tweet import Tweet, TweetDto
from backend.infrastructure.repository.hashtag_repository import HashtagRepository
from backend.infrastructure.repository.tweet_repository import TweetRepository

app = FastAPI(
    title="SocialNet - Backend", description="The Backend for the SocialNet application"
)

tweet_router = APIRouter(prefix="/tweet", tags=["Tweets"])
hashtag_router = APIRouter(prefix="/hashtag", tags=["Hashtag"])

tr: TweetRepository = TweetRepository()
hr: HashtagRepository = HashtagRepository()


# TWEETS
@tweet_router.get("")
def get_tweets():
    return tr.get_tweets()


@tweet_router.post("")
def post_tweet(tweet: Tweet) -> TweetDto:
    r_tweet: TweetDto = tr.save_tweet(tweet=tweet)
    if tweet.hashtags:
        hr: HashtagRepository = HashtagRepository()
        for hashtag in tweet.hashtags:
            hr.save_hashtag(hashtag=hashtag, tweet_id=r_tweet.id)
    return r_tweet


@tweet_router.delete("")
def delete_tweet(id: int) -> TweetDto:
    return tr.delete_tweet(id=id)


# HASHTAGS
@hashtag_router.get("")
def get_hashtags():
    return hr.get_hashtags()


@hashtag_router.get("/trends")
def get_trends():
    return hr.get_trends()


# ROUTERS
app.include_router(tweet_router)
app.include_router(hashtag_router)
