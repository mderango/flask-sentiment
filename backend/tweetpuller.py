import twitter
import json
from datetime import datetime
import sqlite3
import vaderSentiment as vs
from utils import *

class TweetPuller(object):

    def __init__(self):
        credentials = json.loads('twitter/keys.json')
        self.api = twitter.Api(
            consumer_key=credentials['consumer_key'],
            consumer_secret=credentials['consumer_secret'],
            access_token_key=credentials['access_token_key'],
            access_token_secret=credentials['access_token_secret']
        )
        conn = sqlite3.connect('database.db')
        self.c = conn.cursor()
        self.analyzer = vs.vaderSentiment.SentimentIntensityAnalyzer()
    
    def pull_tweets(self, query):
        today = str(datetime.utcnow())[:10]
        tweets = self.api.GetSearch(term=query, lang='en', since=today,
                                    result_type='recent', return_json=True)
        tweets = tweets['statuses']
        # add to database
        for tweet in tweets:
            # needs to be preprocessed
            date = tweet['created_at']
            # pull text and analyze sentiment
            text = tweet['text']
            # polarity scores include pos, neu, neg, and compound
            score = self.analyzer.polarity_scores(text)['compound']
            retweet_count = tweet['retweet_count']
            favorite_count = tweet['favorite_count']

            insert = (date, query, score, retweet_count, favorite_count)

            self.c.execute('INSERT INTO stocks VALUES (?,?,?,?,?)', insert)

