'''test user (client) models'''

from django.test import TestCase
from django.forms.models import model_to_dict
from main.models import Client
from main.tests.factories import ClientFactory

class UserModelTestCases(TestCase):
    '''test the validity of user model'''

    def setUp(self):
        '''setup user data'''
        self.users = ClientFactory.create_batch(3)

    def test_user_can_generate_access_token(self):
        '''test if user can generate access token'''
        for user in self.users:
            client = Client.objects.get(username=user.username)
            client.generate_access_token()
            self.assertIsNotNone(client.access_token)

    def test_user_can_authenticate_username_password(self):
        '''test if user can login with username and password'''
        username = 'test1'
        password = 'test1'
        
        Client(
            username = username,
            password = password,
            bagian = 'admin'
        ).save()

        result = Client.authenticate_credentials(username, password)
        self.assertIsNotNone(result)

    def test_user_can_authenticate_access_token(self):
        '''test if user can be authenticated using access token'''
        for user in self.users:
            client = Client.objects.get(username=user.username)
            client.generate_access_token()

            access_token = client.access_token
            fetched_client = Client.authenticate_access_token(access_token)

            client = model_to_dict(client)
            fetched_client = model_to_dict(fetched_client)
            self.assertEqual(client, fetched_client)
