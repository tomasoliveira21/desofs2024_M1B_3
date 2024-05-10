from fastapi import FastAPI

from backend.domain.tweet import Tweet
from backend.infrastructure.repository.tweet_repository import TweetRepository

app = FastAPI(
    title="SocialNet - Backend", description="The Backend for the SocialNet application"
)


# TWEETS
@app.get("/tweet")
async def get_tweets():
    tr: TweetRepository = TweetRepository()
    return tr.get_tweets()


@app.post("/tweet")
async def post_tweet(tweet: Tweet):
    tr: TweetRepository = TweetRepository()
    print(tweet.hashtags)
    return tr.save_tweet(tweet=tweet)


@app.delete("/tweet")
async def delete_tweet(id: int):
    tr: TweetRepository = TweetRepository()
    return tr.delete_tweet(id=id)
