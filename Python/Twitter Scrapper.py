import pytz
import tweepy  # importing tweepy library for twitter API
import configparser  # importing configparser for reading config.ini
import pandas as pd  # importing pandas for dataframe related operations
from sqlalchemy import create_engine  # for sql related operations
from datetime import datetime, timedelta  # for date conversion

config = configparser.ConfigParser()

config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

alltweets = []

keyword_list = ['#crime', '#gunshot', '#violence', '#safety']
#
for keyword in keyword_list:
    new_tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(200)
    alltweets.extend(new_tweets)

tweet_list = []
tweet_userlist = []

for tweet in alltweets:
    tweet_information = dict()
    tweet_userinfo = dict()
    user_dictionary = tweet._json['user']
    # appending user information
    tweet_userinfo['id'] = user_dictionary['id']
    tweet_userinfo['screen_name'] = user_dictionary['screen_name']
    tweet_userinfo['followers_count'] = user_dictionary['followers_count']
    datetime_object = datetime.strftime(datetime.strptime(user_dictionary['created_at'], '%a %b %d %H:%M:%S +0000 %Y'),
                                        '%Y-%m-%d %H:%M:%S')
    tweet_userinfo['created_at'] = datetime_object

    # appending tweet information
    tweet_information['id_str'] = tweet.id_str
    tweet_information['text'] = tweet.text
    tweet_information['created_at'] = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
    tweet_information['retweet_count'] = tweet.retweet_count
    tweet_information['favorite_count'] = tweet.favorite_count
    place = user_dictionary['location']
    string_list = place.split(',')
    try:
        tweet_information['city'] = string_list[0]
        tweet_information['state'] = string_list[1]
    except IndexError:
        pass
    tweet_information['country'] = "United States"
    tweet_information['id'] = user_dictionary['id']
    tweet_list.append(tweet_information)
    tweet_userlist.append(tweet_userinfo)

data_df = pd.DataFrame(tweet_list).drop_duplicates()
data_df_user = pd.DataFrame(tweet_userlist).drop_duplicates()

# user history(past 24hr tweet)
uniq = data_df_user['id'].unique()
tz_ny = pytz.timezone('America/New_York')
tweet_userhistory = []

for uni in uniq:
    tweet_usrhist = dict()
    tweets_user = api.user_timeline(user_id=uni, count=20, include_rts=False, tweet_mode='extended')
    tweet_count = 0
    for info in tweets_user:
        tweet_times = info.created_at
        if tweet_times > tz_ny.localize(datetime.now() - timedelta(hours=24)):
            tweet_count = tweet_count + 1
            tweet_usrhist['user_id'] = format(info.id)
            tweet_usrhist['tweet_text'] = info.full_text
    tweet_userhistory.append(tweet_usrhist)
data_df_user_hist = pd.DataFrame(tweet_userhistory)
data_df_user_tweet_hist = data_df_user_hist.dropna(inplace=False)


#connecting to SQL DB
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

# converting dataframe to SQL table
data_df_user.to_sql('tweet_users', con=engine, if_exists='append', chunksize=100, index=False)
data_df.to_sql('tweets', con=engine, if_exists='append', chunksize=100, index=False)
data_df_user_tweet_hist.to_sql('tweet_userhist', con=engine, if_exists='append', chunksize=100, index=False)
