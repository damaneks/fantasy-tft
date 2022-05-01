from django.urls import path

from . import views

app_name = 'fantasy'

urlpatterns = [
    path('', views.home, name='home'),
    path('players', views.all_players, name='all_players'),
    path('team-picker', views.team_picker, name='team-picker')
]
