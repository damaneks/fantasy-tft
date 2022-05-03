from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, country, password=None):
        """
        Creates and saves a User with the given username, email, country and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            country=country
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    country = CountryField()
    is_premium = models.BooleanField(default=False)
    objects = UserManager()


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


class PlayerScore(models.Model):
    tournament_stage = models.ForeignKey(
        TournamentStage, on_delete=models.CASCADE, related_name='player_score')
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player_score')
    score = models.IntegerField(default=0)
