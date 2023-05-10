from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
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
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    movie = models.OneToOneField(Movies,null=True,on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    status = models.IntegerField(default=0)
