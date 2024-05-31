from typing import List

from backend.domain.tweet import Tweet, TweetDto
from backend.repository.hashtag_repository import HashtagRepository
from backend.repository.tweet_repository import TweetRepository


class TweetService:
    def __init__(self):
        self._tweet_repository = TweetRepository()
        self._hashtag_repository = HashtagRepository()

    def get_all_tweets(self) -> List[TweetDto]:
        return self._tweet_repository.get_tweets()

    def create_tweet(self, tweet: Tweet) -> TweetDto:
        created_tweet = self._tweet_repository.save_tweet(tweet)

        if tweet.hashtags:
            for hashtag in tweet.hashtags:
                self._hashtag_repository.save_hashtag(
                    hashtag=hashtag, tweet_id=created_tweet.id
                )

        return created_tweet

    def remove_tweet(self, tweet_id: int) -> TweetDto:
        return self._tweet_repository.delete_tweet(tweet_id)

    def get_tweet_by_id(self, tweet_id: int) -> TweetDto:
        tweets = self._tweet_repository.get_tweets()
        for tweet in tweets:
            if tweet.id == tweet_id:
                return tweet
        raise ValueError(f"Tweet with id {tweet_id} not found.")
