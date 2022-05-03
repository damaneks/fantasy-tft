from django.test import Client, TestCase
from fantasy.models import Tournament, TournamentStage
from django.utils import timezone


class testHomeView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fantasy/home.html')


class testPlayersView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/players')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/players')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fantasy/players.html')


class testTeamPickerView(TestCase):

    def setUp(self):
        self.client = Client()
        Tournament.objects.create(
            name='Ultraliga Season 3', slug='ultraliga3')
        self.data1 = TournamentStage.objects.create(
            tournament_id=1, name='Finale', started=timezone.now() + timezone.timedelta(days=3))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/team-picker')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/team-picker')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fantasy/team_picker.html')
