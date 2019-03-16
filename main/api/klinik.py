from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from ..models import Pasien, Kelompok_Pasien, Mahasiswa, Pegawai
from ..models import Kunjungan, Diagnosis, Klinik, Dokter
import json

def kunjungan_insert(request):
    if(request.method == 'POST'):
        try :
            insert_kunjungan(request.POST.dict())
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e :
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else :
        return defaults.bad_request(request, request.path_info)

def insert_kunjungan(data_kunjungan):
    try:
        required_column = ['no_pasien', 'dokter', 'baru', 'asal', 'tarif', 'subsidi', 'bayar', 'diagnosis']
        data_kunjungan = get_required_dict(required_column, data_kunjungan)
        data_kunjungan['dokter'] = Dokter.objects.get(kode=data_kunjungan['dokter'])
        data_kunjungan['no_pasien'] = Pasien.objects.get(no_pasien=data_kunjungan['no_pasien'])

        new_kunjungan = Kunjungan(**data_kunjungan)
        new_kunjungan.save()
        new_kunjungan.kode = "Ku-" + str(new_kunjungan.id)
        new_kunjungan.save()
        return new_kunjungan
    except Exception as e:
        raise e

def kunjungan_get(request, kode_kunjungan):
    if(request.method == 'GET'):
        try:
            kunjungan = get_kunjungan(kode_kunjungan)
            dokter = kunjungan.dokter
            pasien = kunjungan.no_pasien

            data_kunjungan = {'kunjungan':model_to_dict(kunjungan), 'dokter':model_to_dict(dokter), 'pasien':model_to_dict(pasien)}

            return JsonResponse(data_kunjungan)
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return JsonResponse(response)
        
    else :
        return defaults.bad_request(request, request.path_info)

def get_kunjungan(kode_kunjungan):
    try:
        kunjungan = Kunjungan.objects.get(kode=kode_kunjungan)
        return kunjungan
    except Kunjungan.DoesNotExist as e:
        raise Http404(e.__str__())
    except Exception as e:
        raise e

def kunjungan_update(request, kode_kunjungan):
    if(request.method == 'POST'):
        try :
            update_kunjungan(request.POST.dict(), kode_kunjungan)
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e :
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else :
        return defaults.bad_request(request, request.path_info)

def update_kunjungan(data_kunjungan, kode_kunjungan):
    try:
        kunjungan = get_kunjungan(kode_kunjungan)
        id = kunjungan.id

        required_column = ['no_pasien', 'dokter', 'baru', 'asal', 'tarif', 'subsidi', 'bayar', 'diagnosis']
        data_kunjungan = get_required_dict(required_column, data_kunjungan)
        data_kunjungan['dokter'] = Dokter.objects.get(kode=data_kunjungan['dokter'])
        data_kunjungan['no_pasien'] = Pasien.objects.get(no_pasien=data_kunjungan['no_pasien'])
        
        kunjungan = Kunjungan(**data_kunjungan)
        kunjungan.id = id

        kunjungan.save()
    except Exception as e:
        raise e

def kunjungan_delete(request, kode_kunjungan):
    if(request.method == 'POST') :
        try :
            delete_kunjungan(request.POST.dict(), kode_kunjungan)
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e :
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else :
        return defaults.bad_request(request, request.path_info)

def delete_kunjungan(data_kunjungan, kode_kunjungan):
    try:
        kunjungan = get_kunjungan(kode_kunjungan)
        kunjungan.delete()
        
        return kunjungan
    except Exception as e:
        raise e


def get_required_dict(required_column, old_dict):
    new_dict = {}
    for key in required_column:
        if(key in old_dict):
            new_dict[key] = old_dict[key]

    return new_dict

def parse_exception(exception):
    return exception.__str__().replace('"','').replace('(','').replace(')','').split(',')
