from django.shortcuts import render,redirect, HttpResponse

# Create your views here.

def register(request):
    return render(request , 'register.html')

def login(request):
    return render(request , 'login.html')

def home(request):
    return render(request , 'home.html')