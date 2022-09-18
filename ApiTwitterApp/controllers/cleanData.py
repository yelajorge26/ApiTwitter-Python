import re

def clean(tweets):

    tweets_new_1 = del_caracteres(tweets)
    
    tweets_new_2 = del_usernames(tweets_new_1)

    return tweets_new_2
    

def del_caracteres(tweets):

    delwords = ["@","#","|","RT"]

    tweets_del_caracters = list(map(lambda x: ' '.join([word for word in x.split() if word not in (delwords)]), tweets))

    return tweets_del_caracters

def del_usernames(tweets):
    
    tweets_del_usernames = []

    for tweet in tweets:
        tweets_del_usernames.append(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', r"", tweet))

    return tweets_del_usernames