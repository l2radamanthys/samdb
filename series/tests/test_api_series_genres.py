from rest_framework.test import APITestCase
from series.models.series_genres import SerieGenre


class APISerieGenreTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/seriesgenres')
        self.assertEqual(len(response.data['result']), 0)
