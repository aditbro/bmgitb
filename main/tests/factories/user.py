'''generate random user data'''

from faker import Factory
from main.models import Client
from random import choice
import factory

faker = Factory.create()

class ClientFactory(factory.django.DjangoModelFactory):
    '''Generate random client data'''
    class Meta:
        model = Client

    username = factory.LazyFunction(faker.user_name)
    password = factory.LazyFunction(faker.password)
    bagian = factory.LazyAttribute(lambda obj: choice(['admin','loket','apotek']))
