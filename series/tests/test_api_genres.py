from rest_framework.test import APITestCase
from series.models.genres import Genre


class APIGenreTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/genres')
        self.assertEqual(len(response.data['result']), 0)
