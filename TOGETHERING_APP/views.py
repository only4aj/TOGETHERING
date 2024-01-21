from django.shortcuts import render,redirect, HttpResponse
from .models import Video
from django.contrib import messages

# Create your views here.

def register(request):
    return render(request , 'register.html')

def login(request):
    return render(request , 'login.html')

def home(request):
    return render(request , 'home.html')

def watch(request):
    if request.method == "POST":
        link = request.POST.get('link')

        if(link == ''):
            return render(request , 'home.html')
        
        else:
            videos = Video(url=link)

            videos.save()

            play = Video.objects.all()

            return render(request , 'watchpage.html', context={'play' : play})
    
    
    return render(request , 'home.html')

    
