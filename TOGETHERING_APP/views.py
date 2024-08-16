from django.shortcuts import render ,redirect , HttpResponse
from .models import Video
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import uuid
import random
import string

def generate_room_name(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


# Create your views here.

def register(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        email = request.POST.get('email')
        passwrd = request.POST.get('pass')
        c_passwrd = request.POST.get('cpass')


        if (usern == '' or email == '' or passwrd == '' or c_passwrd == ''):
            if (c_passwrd != passwrd):
                messages.info(request , "Try Again!... Password and Confirm Password should be same")
                return render(request , 'register.html')
            
            else:
                messages.info(request , "Fields Can't be Blank...")
                return render(request , 'register.html')

        else:
            user = User.objects.create_user(username=usern, email=email, password=passwrd)
        
            user.save()
            print("user created!")
            return redirect('/')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request , user)
            return redirect('home')
        
        else:
            messages.info(request, "invalid credentials")
            return redirect("/")
        
    else:
        return render(request, 'login.html')
    

def LogOut(request):
    auth.logout(request)
    return redirect("/")



@login_required(login_url='login')
def home(request):
    room_name = generate_room_name()
    link = request.POST.get('room')
    return render(request, 'home.html', {'yt_video_link' : link , 'room_name' : room_name})

@login_required(login_url='login')
def watch(request, room_name):
    if request.method == "POST":
        link = request.POST.get('room')

        if(link == ''):
            return render(request, 'home.html')

    return render(request, 'watchpage.html', context={'roomname': room_name , 'video_link' : link})

    # return render(request, 'home.html')