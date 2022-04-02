from django.db import models
from django_countries.fields import CountryField


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


class TournamentStage(models.Model):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name='tournament_stage')
    name = models.CharField(max_length=255)
    started = models.DateTimeField()

    def __str__(self):
        return self.tournament.name + ' - ' + self.name
