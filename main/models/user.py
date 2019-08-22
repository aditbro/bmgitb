import datetime
import hashlib
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models

_short_length = 100
_medium_length = 255
_long_length = 800

class Client(User) :
    access_token = models.CharField(max_length=_short_length, null=True, blank=True)
    token_expire_time = models.DateTimeField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    bagian = models.CharField(max_length=_short_length)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.is_active = True
        self.is_staff = True
        if(len(self.password) < 80):
            self.password = self.hash_password(self.password)
            self.is_password_hashed = True


    @classmethod
    def authenticate_access_token(cls, access_token):
        client = cls.objects.filter(access_token=access_token)

        if not client :
            raise Exception('invalid token')
        else :
            client = client[0]

        if client.token_expire_time < datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))):
            client.access_token = ''
            client.save()
            raise Exception('invalid token')
        else :
            return client

    @classmethod
    def authenticate_credentials(cls, username, password):
        client = cls.get_client(username)
        if(not client.check_password(password)):            
            return None
        else :
            client.generate_access_token()
            return client


    @classmethod
    def create_client(cls, username, password, bagian):
        pseudo_email = username + '@bmg.itb.ac.id'
        client = Client(username=username, password=password, bagian=bagian)
        client.save()

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
        
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
        token_valid_duration = datetime.timedelta(days=1)
        self.token_expire_time = now + token_valid_duration
        self.save()

        return self.access_token

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        
    def check_password(self, user_password):
        password, salt = self.password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

class ClientBackEnd():
    def authenticate(self, request, username=None, password=None):
        return Client.authenticate_credentials(username, password)

    def get_user(self, user_id):
        try:
            return Client.objects.get(id=user_id)
        except Client.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        return True
