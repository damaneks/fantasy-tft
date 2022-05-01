from datetime import datetime
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    country = CountryField()
    is_premium = models.BooleanField(default=False)


class Player(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    country = CountryField(blank=True)
    twitter_url = models.URLField(blank=True)
    twitch_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TournamentStageManager(models.Manager):
    def get_queryset(self):
        return super(TournamentStageManager, self).get_queryset().filter(started__gt=datetime.now())


class TournamentStage(models.Model):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name='tournament_stage')
    name = models.CharField(max_length=255)
    started = models.DateTimeField()
    events = TournamentStageManager()

    def __str__(self):
        return self.tournament.name + ' - ' + self.name


class PlayerScore(models.Model):
    tournament_stage = models.ForeignKey(
        TournamentStage, on_delete=models.CASCADE, related_name='player_score')
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player_score')
    score = models.IntegerField(default=0)
    is_final = models.BooleanField(default=False)
