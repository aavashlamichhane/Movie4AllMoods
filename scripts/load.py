import csv
import os
from home.models import Movies
import ast

# def run():
    # file = open('C:\\Aavash files\\COMP206\\Project\\Movie4AllMoods\\scripts\\finale.csv',encoding="utf-8")
    # read_file=csv.reader(file)
    # # halo=Movies.objects.all()
    
    # count=1
    # start = 299949
    # for record in read_file:
    #     if count==1:
    #         pass
    #     else:
    #         print(start)
    #         if start == 324493:
    #             break
    #         hallo = Movies.objects.get(id=start)
    #         hallo.crew=record[12]
    #         hallo.save()
    #         # Movies.objects.create(imdbid=record[0],imdbscore=record[2],cast=record[5],crew=record[6],genre=record[3],isAdult=record[8],numVotes=record[9],otitle=record[10],poster=record[4],title=record[1],runtime=record[11],date=record[7])
    #     count=count+1
    #     start =start+1
        
        
        
        
    # movie=Movies.objects.all().order_by('id')
    # for entry in movie:
    #     cast=[]
    #     director =''
    #     # print(type(entry.crew))
    #     if len(entry.crew)==0:
    #         continue
    #     haha=ast.literal_eval(entry.crew)
    #     # print(type(haha))
    #     print(entry.id)
    #     # num = 1
    #     # num = int(num)
    #     for man in haha:
    #         # print(type(man))
    #         # print(type(man))
    #         # print(entry.id)
    #         if man['job'] == 'Director':
    #             director += man['name']+','
    #         # cast+=man['character']+':'+man['name']+'\n'
    #         # print(cast)
    #         # hello = {'name':man['name'],'character':man['character']}
    #         # cast.append(hello)
    #         # if num >=6:
    #         #     break
    #         # else:
    #         #     num = num+1
    #             # director+=man['name']
    #             # print(director)
    #     print(director)
    #     entry.crew=director
    #     entry.save()