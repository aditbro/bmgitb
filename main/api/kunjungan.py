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
def kunjungan_insert(request):
    if(request.method == 'POST'):
        try :
            insert_kunjungan(json.loads(request.body))
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

def insert_kunjungan(post_form):
    kunjungan = Kunjungan(**post_form)
    kunjungan.save()

    return kunjungan

@allow_only_roles(['loket', 'admin', 'apotek', 'administrasi'])
def kunjungan_get(request, kode_kunjungan):
    if(request.method == 'GET'):
        try :
            kunjungan = get_kunjungan(kode_kunjungan)
            kunjungan = kunjungan_model_to_dict(kunjungan)
            return JsonResponse({'kunjungan':kunjungan,'response':'success'}, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else:
        return defaults.bad_request(request, request.path_info)

def get_kunjungan(kode_kunjungan):
    kunjungan = Kunjungan.objects.get(kode=kode_kunjungan, is_valid=True)
    return kunjungan

def kunjungan_model_to_dict(kunjungan):
    kunjungan_foreign_key = {}
    kunjungan_foreign_key['pasien'] = model_to_dict(kunjungan.pasien)
    kunjungan_foreign_key['klinik'] = model_to_dict(kunjungan.klinik)
    kunjungan_foreign_key['dokter'] = model_to_dict(kunjungan.dokter)

    kunjungan = {**model_to_dict(kunjungan), **kunjungan_foreign_key}

    return kunjungan

@allow_only_roles(['loket', 'admin', 'apotek'])
def kunjungan_get_list(request):
    if(request.method == 'GET'):
        try :
            kunjungan_list = get_kunjungan_list(request.GET.dict())
            kunjungan_list = transform_kunjungan_list_to_dict_list(kunjungan_list)
            return JsonResponse({'kunjungan':kunjungan_list,'response':'success'}, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else:
        return defaults.bad_request(request, request.path_info)

def get_kunjungan_list(get_form):
    required_information = ['page', 'entry_per_page', 'sort_field', 'sort_dir']
    default_value = {
        'page' : 1,
        'entry_per_page' : 10,
        'sort_field' : 'waktu_kunjungan',
        'sort_dir' : 'ascending'
    }

    base_info_form = {}
    for info in required_information :
        if not info in get_form :
            base_info_form[info] = default_value[info]            
        else :
            base_info_form[info] = get_form[info]
            del get_form[info]

    start, end = get_entry_range_from_page(base_info_form['page'], base_info_form['entry_per_page'])
    sort_parameter = get_sort_parameter(base_info_form['sort_field'], base_info_form['sort_dir'])

    kunjungan_list = Kunjungan.objects.filter(**get_form).order_by(sort_parameter)[start:end]
    return kunjungan_list

def transform_kunjungan_list_to_dict_list(kunjungan_list):
    result_kunjungan_list = []

    for kunjungan in kunjungan_list :
        result_kunjungan_list.append(kunjungan_model_to_dict(kunjungan))

    return result_kunjungan_list

@allow_only_roles(['loket', 'admin', 'apotek'])
def kunjungan_update(request):
    if(request.method == 'POST'):
        try :
            update_kunjungan(json.loads(request.body))
            return JsonResponse({'response':'success'}, status=200)
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message}
            return JsonResponse(response, status=400)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else:
        return defaults.bad_request(request, request.path_info)

def update_kunjungan(post_form):
    if not 'kode' in post_form :
        raise Exception('Kode kunjungan is missing from request')

    old_kunjungan = get_kunjungan(post_form['kode'])
    old_kunjungan.is_valid = False
    old_kunjungan.restore_subsidi_pasien()
    old_kunjungan.save()

    new_kunjungan = insert_kunjungan(post_form)
    new_kunjungan.id = None
    new_kunjungan.koreksi = old_kunjungan
    new_kunjungan.save()
    new_kunjungan.kode = old_kunjungan.kode
    new_kunjungan.save()

    return new_kunjungan