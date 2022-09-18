from django.urls import path
from . import views

urlpatterns = [

    # PATHS RENDERIZACIÓN DE INTERFACES.
    path('index', views.index, name="index"),
    path('index_keyword', views.index_keyword, name="index_keyword"),
    path('index_username', views.index_username, name="index_username"),

    # PATHS EXTRACCIÓN DE TWEETS.
    path('tweets', views.tweets, name="tweets"),
    path('tweets_keyword', views.tweets_keyword, name="tweets_keyword"),
    path('tweets_username', views.tweets_username, name="tweets_username"),
    
    # PATHS SERVICIO WEB API
    path('getTweets', views.get, name="getTweets"),
    path('getTweetsUsername', views.get_username, name="getTweetsUsername"),

    # PATHS MANEJO DE TWEETS LISTADO Y BASE DE DATOS
    path('tweets_database', views.tweets_database, name="tweets_database"),
    path('all_delete_database', views.all_delete_database, name="all_delete_database"),

    # PATH EXPORTACIÓN DE DATOS
    path('export_to_csv', views.export_to_csv, name="export_to_csv"),

]