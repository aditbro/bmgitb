from django.forms.models import model_to_dict
from django.shortcuts import render
from main.models import Client
from main.api import allow_only_roles

def main(request):
    try:
        client = get_client(request)
        client = model_to_dict(client)
        return render(request, 'website/mainpage.html', client)
    except Exception as e:
        return render(request, 'website/login.html')

def login(request):
    return render(request, 'website/login.html')

def daftar_pasien(request):
    try:
        allowed_roles = ['admin', 'loket']
        client = get_client(request)
        filter_client_role(client, allowed_roles)
        client = model_to_dict(client)
        return render(request, 'website/daftar_pasien.html', client)
    except Exception as e:
        return render(request, 'website/login.html', status=400)

def get_client(request):
    access_token = request.COOKIES.get('access_token')
    client = Client.authenticate_access_token(access_token)
    return client

def filter_client_role(client, allowed_roles):
    if (not client.bagian in allowed_roles):
        raise Exception("user unauthorized to acess this resource")