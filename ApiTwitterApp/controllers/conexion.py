import tweepy

# ENVIROMENT

__consumerKey = 'bNwnxKkmPra3xFTdTniucywKP'
__consumerSecret = '9P24DVDTEifAQ4y8K0AuKdT7qu5cuevEeUTHfblmJuYachpoEz'
__accessToken = '3667246037-Ka3FKrzTYvxOz1qMXocpST7Zr2zG62SYlmnfTTh'
__accessTokenSecret = 'oPUz9ejfa4KFadKBCMMKJfWBm94CiIPFa2LmCZ1mTzaJ1'

def connection():

    auth = tweepy.OAuthHandler(__consumerKey, __consumerSecret)

    auth.set_access_token(__accessToken, __accessTokenSecret)
    
    api = tweepy.API(auth)

    return api