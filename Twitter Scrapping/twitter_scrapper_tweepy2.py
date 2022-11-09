import tweepy
import configparser
import pandas as pd
import re

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = 'NYPDTips'
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
# keywords = '@NYPDTips'
# limit=300
#
# tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
    full = tweet.full_text
    wanted = "WANTED"

    if (re.search('(?<=WANTED )(\w+)', full)) != None:
        print(re.search('(?<=WANTED )!?(?:\s+[a-z]!+)*([^\:]*)', full).group(0))


df = pd.DataFrame(data, columns=columns)

print(df)
