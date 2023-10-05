from rest_framework.test import APITestCase
from series.models.servers import Server


class APIServerTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/servers')
        self.assertEqual(len(response.data['result']), 0)
