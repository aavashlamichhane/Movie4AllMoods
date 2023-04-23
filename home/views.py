from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def logIn(request):
    return render(request, "home/login.html")

def signUp(request):
    return render(request, "home/signup.html")

def help(request):
    return HttpResponse("This is where help lies.")

def aboutUs(request):
    return HttpResponse("This is where about us lies.")





