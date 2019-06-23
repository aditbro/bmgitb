'''generate random user data'''

from faker import Faker
from main.models import Client
from random import choice

def generate_clients(amount):
    '''Generate random client data'''
    fake = Faker()
    clients = []
    for _ in range(amount):
        new_client = Client(
            username = fake.user_name(),
            password = fake.password(),
            bagian = choice(['admin','loket','apotek'])
        )
        clients.append(new_client)
        new_client.save()

    return clients
