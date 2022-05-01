from django.shortcuts import render

from .models import Player, PlayerScore, TournamentStage


def home(request):
    return render(request, 'fantasy/home.html')


def all_players(request):
    players = Player.objects.all()
    return render(request, 'fantasy/players.html', {'players': players})


def team_picker(request):
    events = TournamentStage.events.all()
    event = events[0]
    players_ids = PlayerScore.objects.filter(tournament_stage_id=event.id).values('player_id')
    players = Player.objects.filter(id__in=players_ids)
    return render(request, 'fantasy/team_picker.html', {'players': players, 'event': event})
