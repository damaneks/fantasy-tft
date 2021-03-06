from django.test import TestCase
from django.utils import timezone
from fantasy.models import Player, PlayerScore, Tournament, TournamentStage, CustomUser, UserTeam


class testUserManagerModel(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user('testuser', email='testuser@gmail.com',
                                              password='testPassword123', country='PL')
        self.assertTrue(isinstance(user, CustomUser))


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
            tournament_id=1, name='Finale', started=timezone.now() + timezone.timedelta(days=3))
        self.data2 = TournamentStage.objects.create(
            tournament_id=1, name='Quarterfinale', started=timezone.now() - timezone.timedelta(days=3))
        self.data3 = TournamentStage.objects.create(
            tournament_id=1, name='Semifinale', started=timezone.now() + timezone.timedelta(days=1))

    def test_tournamentStage_model_entry(self):
        """
        Test TournamentStage model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, TournamentStage))
        self.assertEqual(str(data), 'Ultraliga Season 3 - Finale')

    def test_tournamentStage_custom_manager(self):
        """
        Test tournament stage custom manager returns only future events
        """
        data = TournamentStage.events.all()
        self.assertEqual(data.count(), 2)
        self.assertEqual(data[0], self.data1)


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
        self.assertEqual(str(self.data1), 'Ultraliga Season 3 - Finale - shircane')


class TestUserTeamModel(TestCase):

    def setUp(self):
        user = CustomUser.objects.create_user('testuser', email='testuser@gmail.com',
                                              password='testPassword123', country='PL')
        Tournament.objects.create(
            name='Ultraliga Season 3', slug='ultraliga3')
        TournamentStage.objects.create(
            tournament_id=1, name='Finale', started=timezone.now())
        Player.objects.create(name='shircane', slug='shircane')
        self.data1 = UserTeam.objects.create(user=user, tournament_stage_id=1,
                                             captain_id=1, player2_id=1, player3_id=1)

    def test_userTeam_model_entry(self):
        """
        Test UserTeam model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, UserTeam))
        self.assertEqual(str(self.data1), 'Ultraliga Season 3 - Finale - testuser')
