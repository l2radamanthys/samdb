from rest_framework.test import APITestCase
from series.models.series import Serie


class APISerieTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/series')
        self.assertEqual(len(response.data['result']), 0)
