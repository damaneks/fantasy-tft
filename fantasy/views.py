from django.shortcuts import render

from .models import Player, PlayerScore, TournamentStage, UserTeam


def home(request):
    return render(request, 'fantasy/home.html')


def all_players(request):
    players = Player.objects.all()
    return render(request, 'fantasy/players.html', {'players': players})


def team_picker(request):
    events = TournamentStage.events.all()
    event = events[0]
    if request.method == 'POST':
        captain_id = request.POST.get('captainSelect')
        player2_id = request.POST.get('player2Select')
        player3_id = request.POST.get('player3Select')
        UserTeam.objects.create(user=request.user.id, tournament_stage=event.id,
                                captain=captain_id, player2=player2_id, player3=player3_id)
        print(request.POST)
    players_ids = PlayerScore.objects.filter(tournament_stage_id=event.id).values('player_id')
    players = Player.objects.filter(id__in=players_ids)
    return render(request, 'fantasy/team_picker.html', {'players': players, 'event': event})
