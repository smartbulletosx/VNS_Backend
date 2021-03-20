from django.urls import path
from . import views

from .models import Player

urlpatterns = [
    path('', views.PlayerView.as_view(), name=''),
]