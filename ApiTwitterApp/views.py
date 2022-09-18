from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ApiTwitterApp.controllers.twitterApi import extraccion_keyword, extraction, extraction_username
from ApiTwitterApp.controllers.cleanData import clean
from ApiTwitterApp.controllers.database import saveTweets
from ApiTwitterApp.models import Comentario
import csv

HOSPITALES = ["HOSPITAL VICENTE CORRAL MOSCOSO", "IEES" ,"HOSPITAL GENERAL GUASMO SUR", "HOSPITAL LUIS VERNAZA", "HOSPITAL ENRIQUE GARCES", "HOSPITAL TEÓFILO DÁVILA"]

def index(request):

    context = {
        "hospitales": HOSPITALES,
    }

    return render(request, 'index.html', context)

def index_username(request):

    return render(request, 'index_username.html')

def index_keyword(request):

    return render(request, 'index_keyword.html')

def tweets(request):

    params = request.GET

    tweets = extraction(params["hospitales"],params["cantidad"])

    # clean_tweets = clean(tweets)

    saveTweets(tweets)

    context = {
        "tweets": tweets,
    }

    return render(request, 'tweets.html', context)

def tweets_username(request):

    params = request.GET

    tweets = extraction_username(params["username"], params["cantidad"])

    # clean_tweets = clean(tweets)

    saveTweets(tweets)

    context = {
        "tweets": tweets,
    }

    return render(request, 'tweets.html', context)

def tweets_keyword(request):

    params = request.GET

    tweets = extraccion_keyword(params["key_word"], params["cantidad"])

    saveTweets(tweets)

    context = {
        "tweets": tweets,
    }

    return render(request, 'tweets.html', context)

def tweets_database(request):

    tweets = Comentario.objects.all()

    tweets_text = []

    for tweet in tweets:
        if tweet.tweet != "":
            tweets_text.append(tweet.tweet)

    context = {
        'tweets': tweets_text,
    }

    return render(request, 'tweets_database.html', context)

def export_to_csv(request):

    tweets = Comentario.objects.all()

    response = HttpResponse('text/csv')

    response['Content-Disposition'] = 'attachment; filename=tweets.csv'

    writer = csv.writer(response)

    writer.writerow(['ID', 'TWEET'])

    tweets_list = tweets.values_list('id','tweet')

    for t in tweets_list:

        writer.writerow(t)

    return response

def all_delete_database(request):

    tweets = Comentario.objects.all()

    tweets.delete()

    context = {
        "hospitales": HOSPITALES,
    }

    return render(request, 'index.html', context)


def get(request):

    params = request.GET

    apiTweets = extraction(params["hospitales"],params["cantidad"])

    apiCleanTweets = clean(apiTweets)

    return JsonResponse(apiCleanTweets, safe=False)

def get_username(request):

    params = request.GET

    apiTweets = extraction_username(params["username"],params["cantidad"])

    apiCleanTweets = clean(apiTweets)

    return JsonResponse(apiCleanTweets, safe=False)

# TEST PAGE
def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")