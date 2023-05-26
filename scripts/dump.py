# ! This file contains dumped codes

# ? aboutUs:views.py:home

# # # # movie = Movies.objects.get(pk=266330)
    # # # # print(type(movie.cast))
    # # # # haha=ast.literal_eval(movie.cast)
    # # # # print(type(haha))
    # # # # print(haha[0]['name'])
    # # # # final = ''
    # # # # for names in haha:
    # # # #     final += names['name']
    # # # #     final +=' '
    # # # # print(final)

    # # movie = Movies.objects.all()
    # # movies_panda=pd.DataFrame([t.__dict__ for t in movie])
    # # # # print(movie)
    # # # # print(movies_panda.head())
    # # # # print(movies_panda[['id','imdbid','title','crew','cast','otitle','numVotes','imdbscore','runtime','date','genre','isAdult','poster',]])
    # # features = ['crew','cast','genre']
    # # combined_features = movies_panda['genre']+' '+movies_panda['cast']+' '+movies_panda['crew']
    # # # # print(combined_features)
    # # vectorizer = TfidfVectorizer()
    # # feature_vectors = vectorizer.fit_transform(combined_features)
    # # similarity = cosine_similarity(feature_vectors)
    
    
    
    # movie = Movies.objects.all().order_by('-numVotes')[:10000]
    # # print(type(movie))
    # movies_panda=pd.DataFrame([t.__dict__ for t in movie])
    # # # print(movie)
    # # print(movies_panda['cast'].head())
    # # # print(movies_panda[['id','imdbid','title','crew','cast','otitle','numVotes','imdbscore','runtime','date','genre','isAdult','poster',]])

    # features = ['crew','cast','genre']
    # combined_features = movies_panda['genre']+' '+movies_panda['cast']+' '+movies_panda['crew']
    # # # print(combined_features)
    # vectorizer = TfidfVectorizer()
    # feature_vectors = vectorizer.fit_transform(combined_features)
    # similarity = cosine_similarity(feature_vectors)
    
    
    
    # movie = Movies.objects.all().order_by('-numVotes')[:10000]
    # # print(type(movie))
    # movies_panda=pd.DataFrame([t.__dict__ for t in movie])
    # # # print(movie)
    # # print(movies_panda['cast'].head())
    # # # print(movies_panda[['id','imdbid','title','crew','cast','otitle','numVotes','imdbscore','runtime','date','genre','isAdult','poster',]])

    # features = ['cast']
    # for feature in features:
    #     movies_panda[feature]=movies_panda[feature].apply(literal_eval)
    # # print(movies_panda[['title','cast','crew','genre']].head(5))
    # # print(movies_panda['cast'][1][1]['name'])
    # features = ['cast']
    # for feature in features:
    #     movies_panda[feature]=movies_panda[feature].apply(get_list)
    # print(movies_panda[['title','cast','crew','genre']].head(5))
    # features = ['cast','crew','genre']
    # for feature in features:
    #     movies_panda[feature] = movies_panda[feature].apply(clean_data)
    # print(movies_panda[['title','cast','crew','genre']].head(5))
    # print(movies_panda['cast'][1][1]['name'])
    # features = ['cast']
    # for feature in features:
    #     movies_panda[feature]=movies_panda[feature].apply(get_list)
    # print(movies_panda[['title','cast','crew','genre']].head(5))
    # features = ['cast','crew','genre']
    # for feature in features:
    #     movies_panda[feature] = movies_panda[feature].apply(clean_data)
    # print(movies_panda[['title','cast','crew','genre']].head(5))
    # movies_panda['soup']=movies_panda.apply(create_soup,axis=1)
    # print(movies_panda[['cast','crew','genre','soup']].head(5))
    # count = CountVectorizer(stop_words='english')
    # count_matrix = count.fit_transform(movies_panda['soup'])
    # userlist = list.objects.filter(user=request.user,status=1,rating__gte=6)
    # ranges = range(10,5,-1)
    # list_of_list = []
    # for i in ranges:
    #     userlist = list.objects.filter(user=request.user,status=1,rating=i)
    #     hajar = []
    #     for m in userlist:
    #         hajar.append(m.movie.pk)
    #     list_of_list.append(hajar)
    # print(list_of_list)
    # print(type(umovies))
    # ? Following snippet is for converting user list to pandas
    
    # user_panda = pd.DataFrame([t.__dict__ for t in umovies])
    # user_panda['cast']=user_panda['cast'].apply(literal_eval)
    # user_panda['cast']=user_panda['cast'].apply(get_list)
    # features = ['cast','crew','genre']
    # for feature in features:
    #     user_panda[feature] = user_panda[feature].apply(clean_data)
    # user_panda['soup']=user_panda.apply(create_soup,axis=1)
    # # print(user_panda[['title','cast','crew','genre','soup']].head(5))
    # user_matrix = count.fit_transform(user_panda['soup'])
    
    
    # similarity = cosine_similarity(count_matrix,count_matrix)
    # # print(similarity.shape)
    # movies_panda = movies_panda.reset_index()
    # indices = pd.Series(movies_panda.index,index=movies_panda['title'])
    # def get_recom(title,number,cosine_sim=similarity):
    #     idx = indices[title]
    #     sim_scores= builtins.list(enumerate(cosine_sim[idx].tolist()))
    #     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #     sim_scores = sim_scores[1:number+1]
    #     movie_indices = [i[0] for i in sim_scores]
    #     return movies_panda.iloc[movie_indices]
    
    # recommended = []
    # ranvar = int(10)
    # for item in list_of_list:
    #     if len(item)==0:
    #         ranvar-=1
    #         continue
    #     for item2 in item:
    #         to_get = Movies.objects.get(pk=item2).title
    #         print(to_get)
    #         no_of_recom = get_no(ranvar,len(item))
    #         print(no_of_recom)
    #         if no_of_recom == 0:
    #             no_of_recom+=1
    #         recomm = get_recom(to_get,no_of_recom)
    #         print(type(recomm))
    #         print(recomm[['id','title']])
    #         for entries in recomm['id'].tolist():
    #             recommended.append(entries)
    #     ranvar-=1
    # movies = []
    # for entry in recommended:
    #     movies.append(Movies.objects.get(pk=entry))
    # print(type(movies))
    # print(len(movies))
    # print(recommended)
    # print(type(recommended))
    # print(len(recommended))
    
    # print(len(userlist))
    
    # print(user_panda.head())
    # print(type(userlist))

    
    # # for m in userlist:
    # #     print(m.movie.title)
    
    
    # # similarity = cosine_similarity(count_matrix,count_matrix)
    # # movies_panda = movies_panda.reset_index()
    # # indices = pd.Series(movies_panda.index,index=movies_panda['title'])
    # # def get_recom(title,cosine_sim=similarity):
    # #     idx = indices[title]
    # #     sim_scores= builtins.list(enumerate(cosine_sim[idx].tolist()))
    # #     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # #     sim_scores = sim_scores[1:11]
    # #     movie_indices = [i[0] for i in sim_scores]
    # #     return movies_panda.iloc[movie_indices]
    
    # # oolala = get_recom('The Avengers')
    # # print(type(oolala))
    # # print(oolala['title'])
    