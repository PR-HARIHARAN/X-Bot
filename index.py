from datetime import time

import tweepy

api_key = ""
api_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

search_items = ["Python", "machine learning", "Data science"]


class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print("connected")

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)


stream = MyStream(bearer_token=bearer_token)

for term in search_items:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])
