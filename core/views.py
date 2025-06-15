from .models import Perfil
from .forms import AvatarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def cambiar_avatar(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=perfil)
    return render(request, 'cambiar_avatar.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Cambia 'home' por la vista que prefieras tras el registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
