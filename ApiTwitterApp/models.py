from django.db import models

class Comentario(models.Model):
    tweet = models.CharField(max_length=1000)