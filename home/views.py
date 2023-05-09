from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Movies
from django.contrib.auth.decorators import login_required

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
    return render(request, "home/filter.html")

def profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email= request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        if User.objects.filter(username=username):
            messages.error(request,"Username already exists.")
            return redirect('/home/userprofile')
        if User.objects.filter(email=email):
            messages.error(request,"E-Mail already exists.")
            return redirect('/home/userprofile') 
        if len(username)>30:
            messages.error(request,"Username is longer than 30 characters.")
            return redirect('/home/userprofile')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('/home/signup')
        
    return render(request, "home/profile.html")
    



def list(request):
    return render(request,"home/list.html")

def p2w(request):
    messages.success(request,"Added.")
    return redirect('/home')