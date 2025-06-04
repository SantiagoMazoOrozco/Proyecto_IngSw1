"""
URL configuration for retrohub_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Vista directa usando render
def home(request):
    return render(request, 'index.html')  # Ajustar el nombre de la plantilla

def browse(request):
    return render(request, 'browse.html')

def details(request):
    return render(request, 'details.html')

def profile(request):
    return render(request, 'profile.html')

def streams(request):
    return render(request, 'streams.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def play_chrono_trigger(request):
    return render(request, 'play.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Esta línea hace que se cargue en la raíz /
    path('browse/', browse, name='browse'),
    path('details/', details, name='details'),
    path('profile/', profile, name='profile'),
    path('streams/', streams, name='streams'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('play/chrono-trigger/', play_chrono_trigger, name='play_chrono_trigger'),
]