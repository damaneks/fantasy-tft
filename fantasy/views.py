from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from fantasy.forms import LoginForm, RegisterForm

from .models import Player, PlayerScore, TournamentStage, UserTeam


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm


def home(request):
    return render(request, 'fantasy/home.html')


def all_players(request):
    players = Player.objects.all()
    return render(request, 'fantasy/players.html', {'players': players})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fantasy:home')
    return render(request, 'registration/register.html', {"form": form})


def custom_logout(request):
    logout(request)
    return redirect('fantasy:home')


def team_picker(request):
    events = TournamentStage.events.all()
    event = events[0]
    user_team_filter = UserTeam.objects.filter(tournament_stage=event, user=request.user)
    if request.method == 'POST':
        captain_id = request.POST.get('captainSelect')
        player2_id = request.POST.get('player2Select')
        player3_id = request.POST.get('player3Select')
        if user_team_filter.exists():
            user_team = UserTeam.objects.get(tournament_stage=event, user=request.user)
            user_team.captain_id = captain_id
            user_team.player2_id = player2_id
            user_team.player3_id = player3_id
            user_team.save()
        else:
            UserTeam.objects.create(user=request.user, tournament_stage=event,
                                    captain_id=captain_id, player2_id=player2_id, player3_id=player3_id)
    players_ids = PlayerScore.objects.filter(tournament_stage_id=event.id).values('player_id')
    players = Player.objects.filter(id__in=players_ids)
    if user_team_filter.exists():
        return render(request, 'fantasy/team_picker.html', {'players': players, 'event': event, 'user_team': user_team_filter[0]})
    else:
        return render(request, 'fantasy/team_picker.html', {'players': players, 'event': event})
