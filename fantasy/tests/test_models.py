from django.test import TestCase
from django.utils import timezone

from fantasy.models import Player, PlayerScore, Tournament, TournamentStage


class TestPlayerModel(TestCase):

    def setUp(self):
        self.data1 = Player.objects.create(name='shircane', slug='shircane')

    def test_player_model_entry(self):
        """
        Test Player model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Player))
        self.assertEqual(str(data), 'shircane')


class TestTournamentModel(TestCase):

    def setUp(self):
        self.data1 = Tournament.objects.create(
            name='Ultraliga Season 3', slug='ultraliga3')

    def test_tournament_model_entry(self):
        """
        Test Tournament model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Tournament))
        self.assertEqual(str(data), 'Ultraliga Season 3')


class TestTournamentStageModel(TestCase):

    def setUp(self):
        Tournament.objects.create(
            name='Ultraliga Season 3', slug='ultraliga3')
        self.data1 = TournamentStage.objects.create(
            tournament_id=1, name='Finale', started=timezone.now())

    def test_tournamentStage_model_entry(self):
        """
        Test TournamentStage model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, TournamentStage))
        self.assertEqual(str(data), 'Ultraliga Season 3 - Finale')


class TestPlayerScoreModel(TestCase):

    def setUp(self):
        Tournament.objects.create(
            name='Ultraliga Season 3', slug='ultraliga3')
        TournamentStage.objects.create(
            tournament_id=1, name='Finale', started=timezone.now())
        Player.objects.create(name='shircane', slug='shircane')
        self.data1 = PlayerScore.objects.create(
            tournament_stage_id=1, player_id=1)

    def test_playerScore_model_entry(self):
        """
        Test PlayerScore model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, PlayerScore))
