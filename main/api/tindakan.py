from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from ..models import Pasien, Mahasiswa
from ..models import Kunjungan, Tindakan_Kunjungan
from .helper import *
from .auth_decorators import *
import json
import traceback

@allow_only_roles(['loket', 'admin'])
def tindakan_kunjungan_insert(request):
    if(request.method == 'POST'):
        try :
            insert_tindakan_kunjungan(json.loads(request.body))
            return JsonResponse({'response':'success'}, status=200)
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message}
            return JsonResponse(response, status=400)
        except Exception as e:
            traceback.print_exc()
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else :
        return defaults.page_not_found(request, request.path_info)

def insert_tindakan_kunjungan(post_form):
    list_tindakan = []

    for tindakan in post_form['tindakan'] :
        tindakan = Tindakan_Kunjungan(**tindakan)
        tindakan.save()
        list_tindakan.append(tindakan)

    return list_tindakan

@allow_only_roles(['loket', 'admin', 'apotek'])
def tindakan_kunjungan_get_list(request, kode_kunjungan):
    if(request.method == 'GET'):
        try :
            tindakan_list = get_tindakan_kunjungan_list(kode_kunjungan)
            tindakan_list = transform_tindakan_kunjungan_list_to_dict(tindakan_list)
            return JsonResponse({'tindakan':tindakan_list,'response':'success','code':200})
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else:
        return defaults.bad_request(request, request.path_info)

def get_tindakan_kunjungan_list(kode_kunjungan):
    tindakan_list = Tindakan_Kunjungan.objects.filter(kunjungan__kode=kode_kunjungan)
    return tindakan_list

def transform_tindakan_kunjungan_list_to_dict(tindakan_list):
    result_tindakan_list = []

    for tindakan in tindakan_list :
        tindakan = tindakan_kunjungan_to_dict(tindakan)
        result_tindakan_list.append(tindakan)

    return result_tindakan_list

def tindakan_kunjungan_to_dict(tindakan):
    ret_tindakan = model_to_dict(tindakan)
    ret_tindakan['tindakan'] = model_to_dict(tindakan.tindakan)

    return ret_tindakan

@allow_only_roles(['loket', 'admin'])
def tindakan_kunjungan_update(request):
    if(request.method == 'POST'):
        try :
            update_tindakan_kunjungan(json.loads(request.body))
            return JsonResponse({'response':'success'}, status=200)
        except IntegrityError as e:
            traceback.print_exc()
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message}
            return JsonResponse(response, status=400)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else:
        return defaults.bad_request(request, request.path_info)

def update_tindakan_kunjungan(post_form):
    list_tindakan = []

    for tindakan in post_form['tindakan'] :
        old_tindakan = Tindakan_Kunjungan.objects.get(id=tindakan['id'])
        tindakan = Tindakan_Kunjungan(**tindakan)
        tindakan.id = old_tindakan.id
        tindakan.save()
        list_tindakan.append(tindakan)

    return list_tindakan
