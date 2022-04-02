from django.contrib import admin

from .models import Player, PlayerScore, Tournament, TournamentStage


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(TournamentStage)
class TournamentStageAdmin(admin.ModelAdmin):
    list_display = ['get_tournament_name', 'name', 'started']

    @admin.display(ordering='tournament__name', description='Tournament')
    def get_tournament_name(self, obj):
        return obj.tournament.name


@admin.register(PlayerScore)
class PlayerScoreAdmin(admin.ModelAdmin):
    list_display = ['get_tournament_stage_name', 'get_player_name', 'score']

    @admin.display(ordering='tournament_stage__name', description='Tournament')
    def get_tournament_stage_name(self, obj):
        return obj.tournament_stage

    @admin.display(ordering='player__name', description='Player')
    def get_player_name(self, obj):
        return obj.player.name
