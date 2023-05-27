import ast
import builtins
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Movies, list
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.db.models import Q
import pandas as pd
import numpy as np
import difflib
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pympler import asizeof
# Create your views here.

def search(request):
    query=request.GET['query']
    if query == '':
        allMovies = Movies.objects.all().order_by('-numVotes')[:20]
        params={'allMovies':allMovies, 'query':query}
        return render(request,"home/filter.html", params) 
    # exactMatch = Movies.objects.filter(title__iexact=query).first()
    # if exactMatch:    
    #     allMovies = [exactMatch] 
    
    allMoviesTitle = Movies.objects.filter(title__icontains=query)
    
    if allMoviesTitle.exists():
        allMovies = allMoviesTitle.order_by('-numVotes')
    
    else:
        allMoviesCast = Movies.objects.filter(cast__icontains=query)
        allMoviesCrew = Movies.objects.filter(crew__icontains=query)
        allMovies = allMoviesTitle.union(allMoviesCast,allMoviesCrew).order_by('-numVotes')

    params={'allMovies':allMovies, 'query':query}
    return render(request,"home/filter.html", params) 

def get_list(x):
    # for i in x:
        # print(type(i))
        # print(i['name'])
    # print(type(x))
    # if type(x) is list:
        names = [i['name'] for i in x]
        # if len(names)>:
        #     names = names[:4]
        # print(names)
        return names
    # else:
    #     # print('I am here.')
    #     return []

def clean_data(x):
    if isinstance(x,str):
        ahaha= str.lower(x.replace(' ',''))
        return ahaha.replace(',',' ')
    else:
        return [str.lower(i.replace(' ','')) for i in x]

def create_soup(x):
    return ' '+x['crew']+' '+' '.join(x['cast'])+' '+x['genre']

def get_no(x,y):
    if x==6:
        return int(15/y)
    elif x==7:
        return int(18/y)
    elif x==8:
        return int(20/y)
    elif x==9:
        return int(22/y)
    elif x==10:
        return int(25/y)
    else:
        return '0'

def landing(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return render(request, 'home/landing.html')
 
def index(request):
    tmovie=Movies.objects.all().order_by('-imdbscore')[:10]
    pmovie=Movies.objects.all().order_by('-numVotes')[:10]
    lmovie=Movies.objects.all().order_by('-date')[:10]
    rmovie=Movies.objects.all().order_by('-title')[:10]
    params={'titem':tmovie,'pitem':pmovie,'litem':lmovie, 'ritem':rmovie}
    return render(request, 'home/index.html',params)

def logIn(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully.")
            return redirect("/home")
        else:
            messages.warning(request,"Incorrect credentials.")
            return redirect("/home/login")
            
    return render(request, "home/login.html")

def signUp(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email= request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmpassword')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        # print(username)
        # print(email)
        # print(pass1)
        # print(pass2)
        # print(fname)
        # print(lname)
        # print(check)
        if User.objects.filter(username=username):
            messages.error(request,"Username already exists.")
            return redirect('/home/signup')
        if User.objects.filter(email=email):
            messages.error(request,"E-Mail already exists.")
            return redirect('/home/signup') 
        if len(username)>30:
            messages.error(request,"Username is longer than 30 characters.")
            return redirect('/home/signup')
        if pass1!=pass2:
            messages.error(request,"Passwords donot match")
            return redirect('/home/signup')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('/home/signup')
        newuser = User.objects.create_user(username,email,pass1)
        newuser.first_name = fname
        newuser.last_name = lname
        
        newuser.save()
        
        messages.success(request,"Successfully created your account. Please log in.")
        return redirect("/home/login")
    
    
    return render(request, "home/signup.html")


def aboutus(request):
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
    features = ['cast']
    for feature in features:
        movies_panda[feature]=movies_panda[feature].apply(get_list)
    print(movies_panda[['title','cast','crew','genre']].head(5))
    features = ['cast','crew','genre']
    for feature in features:
        movies_panda[feature] = movies_panda[feature].apply(clean_data)
    print(movies_panda[['title','cast','crew','genre']].head(5))
    movies_panda['soup']=movies_panda.apply(create_soup,axis=1)
    print(movies_panda[['cast','crew','genre','soup']].head(5))
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(movies_panda['soup'])
    userlist = list.objects.filter(user=request.user,status=1,rating__gte=6)
    ranges = range(10,5,-1)
    list_of_list = []
    for i in ranges:
        userlist = list.objects.filter(user=request.user,status=1,rating=i)
        hajar = []
        for m in userlist:
            hajar.append(m.movie.pk)
        list_of_list.append(hajar)
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
    
    
    similarity = cosine_similarity(count_matrix,count_matrix)
    # print(similarity.shape)
    movies_panda = movies_panda.reset_index()
    indices = pd.Series(movies_panda.index,index=movies_panda['title'])
    def get_recom(title,number,cosine_sim=similarity):
        idx = indices[title]
        sim_scores= builtins.list(enumerate(cosine_sim[idx].tolist()))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:number+1]
        movie_indices = [i[0] for i in sim_scores]
        return movies_panda.iloc[movie_indices]
    
    recommended = []
    ranvar = int(10)
    for item in list_of_list:
        if len(item)==0:
            ranvar-=1
            continue
        for item2 in item:
            to_get = Movies.objects.get(pk=item2).title
            print(to_get)
            no_of_recom = get_no(ranvar,len(item))
            print(no_of_recom)
            if no_of_recom == 0:
                no_of_recom+=1
            recomm = get_recom(to_get,no_of_recom)
            print(type(recomm))
            print(recomm[['id','title']])
            for entries in recomm['id'].tolist():
                recommended.append(entries)
        ranvar-=1
    movies = []
    for entry in recommended:
        movies.append(Movies.objects.get(pk=entry))
    print(type(movies))
    print(len(movies))
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
    
    
    
    
    
    return render(request, "home/aboutus.html")

def help(request):
    return render(request, "home/help.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect('/home')

def recommend(request):
    # rmovie=Movies.objects.all().order_by('-title')[:50]
    # params={'ritem':rmovie, 'range':range(10)}
    movie = Movies.objects.all().order_by('-numVotes')[:10000]
    movies_panda=pd.DataFrame([t.__dict__ for t in movie])
    
    features = ['cast']
    for feature in features:
        movies_panda[feature]=movies_panda[feature].apply(literal_eval)
    
    features = ['cast']
    for feature in features:
        movies_panda[feature]=movies_panda[feature].apply(get_list)
    print(movies_panda[['title','cast','crew','genre']].head(5))
    features = ['cast','crew','genre']
    for feature in features:
        movies_panda[feature] = movies_panda[feature].apply(clean_data)
    print(movies_panda[['title','cast','crew','genre']].head(5))
    movies_panda['soup']=movies_panda.apply(create_soup,axis=1)
    print(movies_panda[['cast','crew','genre','soup']].head(5))
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(movies_panda['soup'])
    userlist = list.objects.filter(user=request.user,status=1,rating__gte=6)
    ranges = range(10,5,-1)
    list_of_list = []
    for i in ranges:
        userlist = list.objects.filter(user=request.user,status=1,rating=i)
        hajar = []
        for m in userlist:
            hajar.append(m.movie.pk)
        list_of_list.append(hajar)
    
    
    
    similarity = cosine_similarity(count_matrix,count_matrix)
    movies_panda = movies_panda.reset_index()
    indices = pd.Series(movies_panda.index,index=movies_panda['title'])
    def get_recom(title,number,cosine_sim=similarity):
        idx = indices[title]
        sim_scores= builtins.list(enumerate(cosine_sim[idx].tolist()))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:number+1]
        movie_indices = [i[0] for i in sim_scores]
        return movies_panda.iloc[movie_indices]
    
    recommended = []
    ranvar = int(10)
    for item in list_of_list:
        if len(item)==0:
            ranvar-=1
            continue
        for item2 in item:
            to_get = Movies.objects.get(pk=item2).title
            print(to_get)
            no_of_recom = get_no(ranvar,len(item))
            print(no_of_recom)
            if no_of_recom == 0:
                no_of_recom+=1
            recomm = get_recom(to_get,no_of_recom)
            print(type(recomm))
            print(recomm[['id','title']])
            for entries in recomm['id'].tolist():
                recommended.append(entries)
        ranvar-=1
    movies = []
    for entry in recommended:
        movies.append(Movies.objects.get(pk=entry))
    print(type(movies))
    print(len(movies))
    params = {'ritem':movies,'total':len(movies)}
    
    return render(request, "home/recommend.html",params)

def filter(request):
    
    srmovie=Movies.objects.all().order_by('-genre')[:30]
    params={'sritem':srmovie, 'range':range(10)}
    return render(request, "home/filter.html",params)

@login_required
def profile(request,*args,**kwargs):
    # user_id = kwargs.get('user_id')
    # print(user_id)
    # try:
    #     user= User.objects.get(pk=user_id)
    # except User.DoesNotExist:
    #     return HttpResponse("Something went wrong.")
    # if user.pk != request.user.pk:
    #     return HttpResponse("Cannot edit this data.")
    # context = {}
    # if request.POST:
    #     form = EditProfileForm(request.POST,instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/home/userprofile',user_id=user.pk)
    #     else:
    #         form = EditProfileForm(request.POST,instance=request.user,
    #             initial={
    #                 "first_name":user.first_name,
    #                 "last_name":user.last_name,
    #                 "username":user.username,
    #                 "email":user.email,
    #             }    
    #         )
    #         context['form']=form
    # else:
    #     form = EditProfileForm(
    #             initial={
    #                 "first_name":user.first_name,
    #                 "last_name":user.last_name,
    #                 "username":user.username,
    #                 "email":user.email,
    #             }    
    #         )
    #     context['form']=form
    # return render(request,'home/profile.html',context)
    
    if request.method == 'POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            user_form=form.save()
            return redirect('/home/userprofile')
    else:
        form= EditProfileForm(instance=request.user)
        args={}
        args['form']=form
        return render(request,"home/profile.html",args)




def lists(request):
    tmovie=list.objects.filter(user=request.user,status=2)
    params={'titem':tmovie}
    return render(request,"home/list.html",params)


def p2w(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Log in first.")
        return redirect('/home/login')
    else:
        if request.method =='POST':
            movieId = request.POST['movieId']
            movie = Movies.objects.get(pk=movieId)
            if list.objects.filter(user=request.user,movie=movie):
                entry = list.objects.get(user=request.user,movie=movie)
                if entry.status == 1:
                    messages.warning(request,"Entry already exists in Already Watched.")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                elif entry.status == 2:
                    messages.warning(request,"Entry already exists in Plan-To-Watch")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponse("Something went wrong1.")
            else:
                list_entry = list(user=request.user,movie=movie,rating=0,status=2)
                list_entry.save()
                messages.success(request,"Added to plan to watch.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse("Something went wrong.")
    



def watched(request):
    tmovie=list.objects.filter(user=request.user,status=1)
    params={'titem':tmovie}
    return render(request,"home/watched.html",params)

def alwat(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Log in first.")
        return redirect('/home/login')
    else:
        if request.method =='POST':
            movieId = request.POST['amovieId']
            movie = Movies.objects.get(pk=movieId)
            rating = request.POST['rating']
            if list.objects.filter(user=request.user,movie=movie):
                entry = list.objects.get(user=request.user,movie=movie)
                if entry.status == 1:
                    messages.warning(request,"Entry already exists in Already Watched.")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                elif entry.status == 2:
                    messages.warning(request,"Entry already exists in Plan-To-Watch")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    return HttpResponse("Something went wrong2.")
            else:
                list_entry = list(user=request.user,movie=movie,rating=rating,status=1)
                list_entry.save()
                messages.success(request,"Added to already watched.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse("Something went wrong.")
        
def updaterating(request):
    if request.method =='POST':
        rating=request.POST['uprating']
        entry_id =request.POST['entryid']
        entry = list.objects.get(pk=entry_id)
        entry.rating=rating
        entry.save()
        messages.success(request,"Rating updated.")
        return redirect('/home/watched')
    else:
        return HttpResponse("some thing went wrong.")
    
def deleteListEntry(request):
    if request.method == 'POST':
        entry_id = request.POST['delete']
        entry = list.objects.get(pk=entry_id)
        entry.delete()
        messages.success(request,"Entry deleted.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("some thing went wrong.")
    
def updateStatus(request):
    if request.method=="POST":
        entry_id=request.POST['update']
        rating=request.POST['rating11']
        entry = list.objects.get(pk=entry_id)
        entry.status=1
        entry.rating=rating
        entry.save()
        messages.success(request,"Entry moved to already watched.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def moviedes(request):
    return render(request, "home/moviedes.html")

def recommend(request):
    return render(request, "home/recommend.html")