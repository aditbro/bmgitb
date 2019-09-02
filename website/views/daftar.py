from django.forms.models import model_to_dict
from django.shortcuts import render
from main.models import Client
from .main import *

def daftar_pasien(request):
    try:
        allowed_roles = ['admin', 'loket']
        client = get_client(request)
        filter_client_role(client, allowed_roles)
        context = {'Resource': 'Pasien'}
        return render(request, 'website/common_daftar_page.html', context)
    except:
        return render(request, 'website/login.html', status=400)