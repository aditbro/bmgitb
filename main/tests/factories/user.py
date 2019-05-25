'''generate random user data'''

from .randomizer import random_string

def generate_clients(amount):
    '''Generate random client data'''
    clients = []
    for _ in range(amount):
        clients.append({
            'username': random_string(10),
            'password': random_string(10),
            'bagian' : random_string(10)
        })

    return clients
