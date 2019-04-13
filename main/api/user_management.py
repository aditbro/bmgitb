from ..models import Client
from .auth_decorators import require_token
from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.db import models
from django.forms.models import model_to_dict
import json
import traceback

def user_insert(request):
    if(request.method == 'POST'):
        try :
            insert_user(json.loads(request.body))
            return JsonResponse({'response' : 'success'}, status = 200)
        except Exception as e:
            response = {'response' : 'Exception '+e.__str__()}
            return JsonResponse(response, status = 400)
    else :
        return defaults.page_not_found(request, request.path_info)

def insert_user(post_form):
    print(post_form)
    if('username' in post_form and 'password' in post_form):
        client = Client.create_client(post_form['username'], post_form['password'])
        client.save()
    else:
        raise Exception("parameter tidak lengkap")

def user_authenticate(request):
    if(request.method == 'POST'):
        try :
            print(json.loads(request.body))
            user = authenticate_user(json.loads(request.body))
            return JsonResponse({'access_token' : user.access_token}, status = 200)
        except Exception as e:
            traceback.print_exc()
            response = {'response' : 'Exception '+e.__str__()}
            return JsonResponse(response, status = 400)
    else :
        return defaults.page_not_found(request, request.path_info)

def authenticate_user(post_form):
    username = post_form['username']
    password = post_form['password']

    user = Client.authenticate_credentials(username, password)

    return user

@require_token
def profile_get(request) :
    if(request.method == 'GET'):
        try :
            user = get_user(request.headers)
            user = model_to_dict(user)
            return JsonResponse({'user' : user}, status = 200)
        except Exception as e:
            response = {'response' : 'Exception '+e.__str__()}
            return JsonResponse(response, status = 400)
    else :
        return defaults.page_not_found(request, request.path_info)

def get_user(get_header):
    user = Client.authenticate_access_token(get_header['Access-Token'])
    return user
