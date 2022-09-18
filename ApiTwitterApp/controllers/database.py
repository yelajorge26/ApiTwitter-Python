from ApiTwitterApp.models import Comentario

def saveTweets(tweets):
    
    for tweet in tweets:
        tweet1 = Comentario(tweet = tweet)
        tweet1.save()
        print("save tweet id: " + str(tweet1.id))