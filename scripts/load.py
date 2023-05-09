import csv
import os
from home.models import Movies

def run():
    file = open('C:\\Abhyudit Files\\COMP206\\Movie4AllMoods\\scripts\\finale.csv',encoding="utf-8")
    read_file=csv.reader(file)
    
    Movies.objects.all().delete()
    
    count=1
    
    for record in read_file:
        if count==1:
            pass
        else:
            Movies.objects.create(imdbid=record[0],imdbscore=record[7],cast=record[11],crew=record[12],genre=record[6],isAdult=record[3],numVotes=record[8],otitle=record[2],poster=record[10],title=record[1],runtime=record[5],date=record[4])
        count=count+1