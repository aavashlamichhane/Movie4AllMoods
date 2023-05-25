import csv
import os

import pandas as pd
from home.models import Movies
import ast
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pympler import asizeof

def get_list(x):
    if isinstance(x,list):
        names = [i['name'] for i in x]
        # if len(names)>:
        #     names = names[:4]
        return names
    return []

def clean_data(x):
    if isinstance(x,list):
        return [str.lower(i.replace(' ','')) for i in x]
    else:
        if isinstance(x,str):
            ahaha= str.lower(x.replace(' ',''))
            return ahaha.replace(',',' ')
        else:
            return ''

def create_soup(x):
    return ' '+x['crew']+' '+' '.join(x['cast'])+' '+x['genre']

# def get_recom(title,cosine_sim):
#     idx = indices[title]
    

def run():
    # file = open('C:\\Abhyudit Files\\COMP206\\Movie4AllMoods\\scripts\\home_movies_final.csv',encoding="utf-8")
    # read_file=csv.reader(file)
    # halo=Movies.objects.all().order_by('id')[:24544]
    # # halo.delete()
    # for haha in halo:
    #     haha.delete()
    # # Movies.objects.all().delete()
    
    # count=1
    # start = 299949
    # # for record in read_file:
    # #     if count==1:
    # #         pass
    # #     else:
    # #         print(start)
    # #         if start == 324493:
    # #             break
    # #         hallo = Movies.objects.get(id=start)
    # #         hallo.crew=record[12]
    # #         hallo.save()
    # #         Movies.objects.create(imdbid=record[0],imdbscore=record[2],cast=record[5],crew=record[6],genre=record[3],isAdult=record[8],numVotes=record[9],otitle=record[10],poster=record[4],title=record[1],runtime=record[11],date=record[7])
    # #     count=count+1
    
    # # for haha in halo:
    # #     haha.id = start
    # #     print(haha.id)
    # #     haha.save()
    # #     start+=1
        
        
        
        
    # # movie=Movies.objects.all().order_by('id')
    # # for entry in movie:
    # #     cast=[]
    # #     director =''
    # #     # print(type(entry.crew))
    # #     if len(entry.crew)==0:
    # #         continue
    # #     haha=ast.literal_eval(entry.crew)
    # #     # print(type(haha))
    # #     print(entry.id)
    # #     # num = 1
    # #     # num = int(num)
    # #     for man in haha:
    # #         # print(type(man))
    # #         # print(type(man))
    # #         # print(entry.id)
    # #         if man['job'] == 'Director':
    # #             director += man['name']+','
    # #         # cast+=man['character']+':'+man['name']+'\n'
    # #         # print(cast)
    # #         # hello = {'name':man['name'],'character':man['character']}
    # #         # cast.append(hello)
    # #         # if num >=6:
    # #         #     break
    # #         # else:
    # #         #     num = num+1
    # #             # director+=man['name']
    # #             # print(director)
    # #     print(director)
    # #     entry.crew=director
    # #     entry.save()
    
    movie = Movies.objects.all().order_by('-numVotes')[:10000]
    movies_panda=pd.DataFrame([t.__dict__ for t in movie])
    # # print(movie)
    # # print(movies_panda.head())
    # # print(movies_panda[['id','imdbid','title','crew','cast','otitle','numVotes','imdbscore','runtime','date','genre','isAdult','poster',]])
    features = ['cast']
    for feature in features:
        movies_panda[feature]=movies_panda[feature].apply(literal_eval)
    feature = ['cast']
    for feature in features:
        movies_panda[feature]=movies_panda[feature].apply(get_list)
    # print(movies_panda[['title','cast','crew','genre']].head(5))
    features = ['cast','crew','genre']
    for feature in features:
        movies_panda[feature] = movies_panda[feature].apply(clean_data)
    # print(movies_panda[['title','cast','crew','genre']].head(5))
    movies_panda['soup']=movies_panda.apply(create_soup,axis=1)
    print(movies_panda[['cast','crew','genre','soup']].head(5))
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(movies_panda['soup'])
    similarity = cosine_similarity(count_matrix,count_matrix)
    movies_panda = movies_panda.reset_index()
    indices = pd.Series(movies_panda.index,index=movies_panda['title'])
    
    def get_recom(title,cosine_sim=similarity):
        idx = indices[title]
        sim_scores= list(enumerate(cosine_sim[idx].tolist()))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:16]
        movie_indices = [i[0] for i in sim_scores]
        return movies_panda.iloc[movie_indices]
    
    oolala = get_recom('Iron Man')
    print(type(oolala))
    print(oolala['title'])
    
    
    
    
    # combined_features = movies_panda['genre']+' '+movies_panda['cast']+' '+movies_panda['crew']
    # # # print(combined_features)
    # vectorizer = TfidfVectorizer()
    # feature_vectors = vectorizer.fit_transform(combined_features)
    # similarity = cosine_similarity(feature_vectors)
    # print(similarity)
    # print(similarity.shape)
    # print(type(similarity))
    # print(asizeof.asizeof(similarity))
    # print(asizeof.asizeof(combined_features))
    # print(asizeof.asizeof(movies_panda))
    # print(asizeof.asizeof(movie))
    