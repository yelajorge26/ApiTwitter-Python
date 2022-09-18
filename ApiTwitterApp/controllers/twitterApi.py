import tweepy
from datetime import datetime
from ApiTwitterApp.controllers.conexion import connection

def extraccion_keyword(key_word, cantidad):

    __api = connection()

    keyword_tweets = []

    for tweet in tweepy.Cursor(__api.search_tweets, lang = 'es', q = key_word, tweet_mode="extended", exclude_replies = True, include_rts = False).items(int(cantidad)):
        
        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
            
            keyword_tweets.append(tweet.full_text)

    return keyword_tweets

def extraction_username(username, cantidad):
    
    __api = connection()

    user_tweets = []

    for tweet in __api.user_timeline(screen_name = username, count = cantidad, tweet_mode="extended", exclude_replies = True, include_rts = False):

        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):

            user_tweets.append(tweet.full_text)

    return user_tweets

def extraction(medical_center, cantidad):

    __api = connection()

    word = medical_center.lower() + " covid"

    from_date = date_format("01/03/2020 00:00")

    to_date = date_format("17/04/2022 00:00")

    live_tweets = []

    for t in tweepy.Cursor(__api.search_full_archive, label='developer', query = word, fromDate=from_date, toDate=to_date).items(int(cantidad)):

        if (not t.retweeted) and ('RT @' not in t.text):

            live_tweets.append(t.text)

    return live_tweets

def date_format(date):

    newDate = datetime.strptime(date,'%d/%m/%Y %H:%M').strftime('%Y%m%d%H%M')

    return newDate