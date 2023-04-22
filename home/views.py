from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def logIn(request):
    return HttpResponse("This is where login lies.")

def signUp(request):
    return HttpResponse("This is where Sign up lies.")

def help(request):
    return HttpResponse("This is where help lies.")

def aboutUs(request):
    return HttpResponse("This is where about us lies.")





