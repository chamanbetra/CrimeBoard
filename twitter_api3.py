import tweepy
import csv
import pandas as pd
import os
import wget
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

tweets =pd.DataFrame(columns=["id","created_at","text","media_url","location"])

auth = tweepy.auth.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
outtweets = [] #initialize master list to hold our ready tweets
for tweet in tweepy.Cursor(api.search_tweets,q="#crime",count=100, #The q variable holds the hashtag
                           lang="en",
                           since="2022-11-06",
                           until="2022-11-07").items():
    print(tweet)
    media = tweet.entities.get('media', [])
    if(tweet.entities.get('media',[])) : #This condition appends only those tweets to the list which have image URL's
        media = tweet.entities.get('media')
        outtweets.append([tweet.id_str,tweet.created_at,tweet.text.encode("utf-8"),media[0]['media_url'],tweet.user.location])
        print(media[0]['media_url'])


