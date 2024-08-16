from django.contrib import admin
from django.urls import path
from TOGETHERING_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('watch/<str:room_name>/', views.watch, name='watch'),
]