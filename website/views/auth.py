from django.forms.models import model_to_dict
from django.shortcuts import render
from main.models import Client
from .main import *

def login(request):
    return render(request, 'website/login.html')