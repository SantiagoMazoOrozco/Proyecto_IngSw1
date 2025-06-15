from .models import Perfil
from .forms import AvatarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
