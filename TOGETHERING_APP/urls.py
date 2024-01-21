from django.contrib import admin
from django.urls import path
from TOGETHERING_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.login , name='login'),
    path('register/' , views.register , name='register'),
    path('home/' , views.home , name='home'),
    path('watch/' , views.watch , name='watch')
]
