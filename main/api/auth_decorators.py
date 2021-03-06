from ..models import Client
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.db import models
from django.forms.models import model_to_dict
import json
import pry

#for decorator with parameter
def parameterized(dec, *o_args, **o_kwargs):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

def require_token(func, *o_args, **o_kwargs):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.META['HTTP_ACCESS_TOKEN']
            user = Client.authenticate_access_token(token)
            
            return func(request, *args, **kwargs)
        except Exception as e :
            response = {'response' : 'Exception ' + e.__str__()}
            return JsonResponse(response, status=403)
    
    return wrapper

@parameterized
def allow_only_roles(func, roles, *o_args, **o_kwargs):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.META['HTTP_ACCESS_TOKEN'] or request.headers['Access-Token']
            user = Client.authenticate_access_token(token)
            check_if_user_has_role(user, roles)

            return func(self, request, *args, **kwargs)
        except Exception as e :
            response = {'response' : 'Exception ' + e.__str__()}
            return JsonResponse(response, status=403)

    return wrapper

def check_if_user_has_role(user, roles):
    if(not user.bagian in roles):
        raise Exception("user unauthorized to acess this resource")