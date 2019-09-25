from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import render
from main.models import Client
from .main import *
import pry

def login(request):
    return render(request, 'website/login.html')

def parameterized(dec, *o_args, **o_kwargs):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parameterized
def allow_only_roles(func, roles, *o_args, **o_kwargs):
    def wrapper(request, *args, **kwargs):
        try:
            token = request.COOKIES['access_token']
            user = Client.authenticate_access_token(token)
            check_if_user_has_role(user, roles)

            return func(request, *args, **kwargs)
        except Exception as e :
            response = {'response' : 'Exception ' + e.__str__()}
            return render(request, 'website/login.html', status=403)

    return wrapper

def check_if_user_has_role(user, roles):
    if(not user.bagian in roles):
        raise Exception("user unauthorized to acess this resource")