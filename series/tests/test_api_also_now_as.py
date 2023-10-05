from rest_framework.test import APITestCase
from series.models.also_now_as import AlsoNowAs


class APIAlsoNowAsTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/alsonowas')
        self.assertEqual(len(response.data['result']), 0)
