from django.contrib import admin

from .models import Player, Tournament, TournamentStage


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
