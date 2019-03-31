from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from .helper import *
import json


def pembelian_resep_insert(request):
    if(request.method == 'POST'):
        try :
            insert_pembelian_resep(json.loads(request.body))
            return JsonResponse({'response':'success'}, status=200)
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message}
            return JsonResponse(response, status=400)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else :
        return defaults.page_not_found(request, request.path_info)

def insert_pembelian_resep(post_form):
    pass