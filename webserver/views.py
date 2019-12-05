from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

# Create your views here.

def login(request):
    return render(request, 'webuser/login.html')

def index(request):
    return render(request, 'webuser/app.html')

def logout(request):
    return render(request, 'webuser/logout.html')