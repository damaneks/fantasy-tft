from django.test import Client, TestCase


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
