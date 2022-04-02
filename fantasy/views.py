from django.shortcuts import render

from .models import Player


def all_players(request):
    players = Player.objects.all()
    return render(request, 'fantasy/home.html', {'players': players})
