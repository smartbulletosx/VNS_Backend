from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Player


class PlayerView(ListView):
    mode = Player
    template_name = "index.html"
    context_object_name = "players"

    def get_queryset(self):
        return Player.objects.order_by("id")



