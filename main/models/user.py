from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import authenticate
import datetime
import uuid

_short_length = 100
_medium_length = 255
_long_length = 800

class Client(User) :
    access_token = models.CharField(max_length=_short_length, null=True, blank=True)
    token_expire_time = models.DateTimeField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    bagian = models.CharField(max_length=_short_length)

    @classmethod
    def authenticate_access_token(cls, access_token):
        client = cls.objects.filter(access_token=access_token)

        if not client :
            raise Exception('invalid token')
        else :
            client = client[0]

        if client.token_expire_time < datetime.datetime.now(datetime.timezone.utc):
            client.access_token = ''
            client.save()
            raise Exception('invalid token')
        else :
            return client

    @classmethod
    def authenticate_credentials(cls, username, password):
        user = authenticate(username=username, password=password)
        
        if not user :
            raise Exception('invalid credentials')
        else :
            client = cls.get_client(user.username)
            client.generate_access_token()
            return client

    @classmethod
    def create_client(cls, username, password):
        pseudo_email = username + '@jabar.org'
        client = Client.objects.create_user(username, pseudo_email, password)

        return client

    @classmethod
    def get_client(cls, username):
        client = Client.objects.get(username=username)

        if not client :
            raise Exception('Client with username ' + username + ' not found')
        else :
            return client

    def generate_access_token(self):
        token = str(uuid.uuid1())
        self.access_token = token
        
        now = datetime.datetime.now()
        token_valid_duration = datetime.timedelta(days=1)
        self.token_expire_time = now + token_valid_duration
        self.save()

        return self.access_token