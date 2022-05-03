from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from fantasy.forms import LoginForm, RegisterForm

from .models import Player


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
