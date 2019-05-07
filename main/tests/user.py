from django.test import TestCase, Client
import json

class userTestCase(TestCase):
    users = [
        {
            "username" : "admin",
            "password" : "admin",
            "bagian" : "admin"
        },
        {
            "username" : "loket",
            "password" : "loket",
            "bagian" : "loket"
        },
        {
            "username" : "apotek",
            "password" : "apotek",
            "bagian" : "apotek"
        },
        {
            "username" : "admin2",
            "password" : "admin2",
            "bagian" : "administrasi"
        }
    ]

    def setUp(self):
        requests = Client()
        create_user_url = '/main/user/create/'

        for user in self.users:
            result = requests.post(create_user_url, data=user, content_type='application/json')

    def test_user_can_login(self):
        requests = Client()
        login_url = '/main/user/authenticate/'

        for idx, user in enumerate(self.users):
            result = requests.post(login_url, data=user, content_type='application/json')
            result = json.loads(result.content)
            self.assertIsNotNone(result['Access-Token'])
            self.users[idx]['Access-Token'] = result['Access-Token']

    def test_user_can_authenticate_token(self):
        requests = Client()
        login_url = '/main/user/authenticate/'
        profile_url = '/main/user/profile/'

        for idx, user in enumerate(self.users):
            result = requests.post(login_url, data=user, content_type='application/json')
            result = json.loads(result.content)
            self.assertIsNotNone(result['Access-Token'])
            self.users[idx]['Access-Token'] = result['Access-Token']

        for user in self.users:
            header = {'HTTP_ACCESS_TOKEN' : user['Access-Token']}
            result = requests.get(profile_url, content_type='application/json', **header)
            result = json.loads(result.content)
            self.assertEqual(result['user']['username'], user['username'], msg=user['username']+ ' profile not equal')

