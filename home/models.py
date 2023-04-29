from django.db import models

# Create your models here.

class Profile(models.Model):
    user_Id = models.AutoField
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=75)
    age = models.PositiveIntegerField
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    
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
