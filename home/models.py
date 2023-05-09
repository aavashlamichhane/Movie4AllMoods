from django.db import models
from datetime import date

# Create your models here.

class Profile(models.Model):
    bdate = models.DateField(default=date.today)
    
class Movies(models.Model):
    imdbid = models.CharField(max_length=10)
    title=models.CharField(max_length=200)
    imdbscore=models.FloatField(default=-1)
    genre=models.CharField(max_length=500)
    poster=models.CharField(max_length=500)
    cast=models.TextField()
    crew=models.TextField()
    isAdult= models.IntegerField()
    numVotes=models.IntegerField()
    otitle=models.CharField(max_length=200)
    runtime=models.IntegerField()
    date=models.IntegerField()
    def __str__(self):
        return self.title
    
class list(models.Model):
    userId = models.IntegerField(default=0)
    movieId = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    status = models.IntegerField(default=0)
