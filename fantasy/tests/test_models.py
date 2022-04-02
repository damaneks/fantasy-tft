from django.test import TestCase

from fantasy.models import Player, Tournament


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
