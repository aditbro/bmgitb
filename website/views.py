from django.forms.models import model_to_dict
from django.shortcuts import render
from main.models import Client
import pry

# Create your views here.
def main(request):
    try:
        access_token = request.COOKIES.get('access_token')
        client = Client.authenticate_access_token(access_token)
        client = model_to_dict(client)
        return render(request, 'website/mainpage.html', client)
    except Exception as e:
        return render(request, 'website/login.html')

def login(request):
    return render(request, 'website/login.html')