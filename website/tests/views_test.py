from django.test import TestCase
from http.cookies import SimpleCookie
from main.models import Client

class IndexTest(TestCase):
    def setUp(self):
        self.url = '/'

    def test_when_access_token_exist_and_valid(self):
        client = Client.create_client('test', 'test', 'loket')
        access_token = client.generate_access_token()
        self.client.cookies['access_token'] = access_token

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/mainpage.html')

    def test_when_access_token_exist_but_invalid(self):
        self.client.cookies['access_token'] = 'arskadmskamdsa'
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/login.html')

    def test_when_access_token_does_not_exist(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/login.html')
        
