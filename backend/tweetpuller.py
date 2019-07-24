import twitter
import json
from datetime import datetime
import sqlite3


class TweetPuller:

    def __init__(self):
        credentials = json.loads('twitter/keys.json')
        self.api = twitter.Api(
            consumer_key=credentials['consumer_key'],
            consumer_secret=credentials['consumer_secret'],
            access_token_key=credentials['access_token_key'],
            access_token_secret=credentials['access_token_secret']
        )
        conn = sqlite3.connect('database.db')
        self.conn = conn.cursor()
    
    def pull_tweets(self, query):
        today = str(datetime.now())[:10]
        self.tweets = self.api.GetSearch(term=query, lang='en', since=today, return_json=True)
        
    


