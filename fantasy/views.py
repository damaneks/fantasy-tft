from django.shortcuts import render

from .models import Player


def home(request):
    return render(request, 'fantasy/home.html')


def all_players(request):
    players = Player.objects.all()
    return render(request, 'fantasy/players.html', {'players': players})
