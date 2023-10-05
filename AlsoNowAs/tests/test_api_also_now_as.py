from rest_framework.test import APITestCase
from AlsoNowAs.models.also_now_as import Genre


class APIGenreTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/alsonowas')
        self.assertEqual(len(response.data['result']), 0)
