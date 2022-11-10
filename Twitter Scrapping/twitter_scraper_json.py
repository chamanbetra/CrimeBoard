import tweepy
import json
import sys
import configparser
import pandas as pd
from sqlalchemy import create_engine

config = configparser.ConfigParser()

config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

alltweets = []

new_tweets = api.user_timeline(screen_name ='NYPDTips', count=200)
alltweets.extend(new_tweets)

tweet_list = []

for tweet in alltweets:
    tweet_information =dict()
    tweet_information['id_str']=tweet.id_str
    tweet_information['text']=tweet.text

    tweet_information['created_at']=tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
    tweet_information['retweet_count']=tweet.retweet_count
    tweet_information['favorite_count']=tweet.favorite_count
    user_dictionary = tweet._json['user']
    tweet_information['location']=user_dictionary['location']
    tweet_information['followers_count']=user_dictionary['followers_count']
    tweet_information['screen_name']=user_dictionary['screen_name']

    tweet_list.append(tweet_information)
# file = 'tweets.json'
# file_des = open(file,'w')
# json.dump(tweet_list,file_des,indent=4,sort_keys=True)
#
# file_des.close()

# data_df = pd.read_json('tweets.json')
data_df = pd.DataFrame(tweet_list)
#print(data_df)
# print(data_df .head(10))
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='1996Ch1609*')

# cursor = connection.cursor()

# sql = "create database crimeboard"
# cursor.execute(sql)


# connection.commit()

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

data_df.to_sql('tweets', con = engine, if_exists='append', chunksize=100, index=False)







