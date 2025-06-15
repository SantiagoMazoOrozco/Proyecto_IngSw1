from django.urls import path
from . import views

urlpatterns = [
    path('cambiar-avatar/', views.cambiar_avatar, name='cambiar_avatar'),
]
