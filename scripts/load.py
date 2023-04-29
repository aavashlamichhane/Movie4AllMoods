import csv
import os
from home.models import Movies

def run():
    file = open('C:\Aavash files\COMP206\Project\Movie4AllMoods\scripts\MovieGenre.csv',encoding="utf-8")
    read_file=csv.reader(file)
    
    Movies.objects.all().delete()
    
    count=1
    
    for record in read_file:
        if count==1:
            pass
        else:
            Movies.objects.create(imdbid=record[0],imdblink=record[1],title=record[2],imdbscore=record[3],genre=record[4],poster=record[5])
        count=count+1