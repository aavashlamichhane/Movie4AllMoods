from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Movies, list
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.views import generic

# Create your views here.

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
            messages.error(request,"Incorrect creds.")
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

def help(request):
    return render(request, "home/aboutus.html")

def aboutus(request):
    return render(request, "home/aboutus.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect('/home')

def recommend(request):
    rmovie=Movies.objects.all().order_by('-title')[:50]
    params={'ritem':rmovie, 'range':range(10)}
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
                    return redirect('/home')
                elif entry.status == 2:
                    messages.warning(request,"Entry already exists in Plan-To-Watch")
                    return redirect('/home')
                else:
                    return HttpResponse("Something went wrong1.")
            else:
                list_entry = list(user=request.user,movie=movie,rating=0,status=2)
                list_entry.save()
                messages.success(request,"Added to plan to watch.")
                return redirect('/home')
        else:
            return HttpResponse("Something went wrong.")
    

def search(request):
    return render(request,"home/search.html") 

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
                    return redirect('/home')
                elif entry.status == 2:
                    messages.warning(request,"Entry already exists in Plan-To-Watch")
                    return redirect('/home')
                else:
                    return HttpResponse("Something went wrong2.")
            else:
                list_entry = list(user=request.user,movie=movie,rating=rating,status=1)
                list_entry.save()
                messages.success(request,"Added to already watched.")
                return redirect('/home')
        else:
            return HttpResponse("Something went wrong.")