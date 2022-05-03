from django.test import Client, TestCase
from fantasy.models import Player, Tournament, TournamentStage, CustomUser, UserTeam
from django.utils import timezone
from django.contrib.auth import get_user_model


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


class testLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(username='testuser')
        self.user.set_password('testPassword123')
        self.user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_view_register(self):
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testPassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('auth_user_id', self.client.session)


class testRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_view_register(self):
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'testPassword123',
            'password2': 'testPassword123',
            'country': 'PL'
        })
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)


class testLogoutView(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 302)

    def test_view_logout(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('auth_user_id', self.client.session)


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
        self.user = CustomUser.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client = Client()
        self.client.login(username='testuser', password='12345')
        Tournament.objects.create(
            name='Ultraliga Season 3', slug='ultraliga3')
        self.event = TournamentStage.objects.create(
            tournament_id=1, name='Finale', started=timezone.now() + timezone.timedelta(days=3))
        Player.objects.create(name='player', slug='player', country='PL')
        Player.objects.create(name='player2', slug='player2', country='PL')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/team-picker')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/team-picker')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fantasy/team_picker.html')

    def test_view_post_create_userTeam(self):
        self.client.post('/team-picker', data={'captainSelect': 1, 'player2Select': 1, 'player3Select': 1})
        self.assertEqual(UserTeam.objects.filter(user=self.user, tournament_stage=self.event).exists(), True)

    def test_view_post_update_userTeam(self):
        UserTeam.objects.create(user=self.user, tournament_stage=self.event, captain_id=1, player2_id=1, player3_id=1)
        self.client.post('/team-picker', data={'captainSelect': 2, 'player2Select': 2, 'player3Select': 2})
        self.assertEqual(UserTeam.objects.get(user=self.user, tournament_stage=self.event).captain_id, 2)
