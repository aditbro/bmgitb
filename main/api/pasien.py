from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.utils.datastructures import MultiValueDictKeyError
from .helper import *
from ..models import Pasien, Mahasiswa, Karyawan_BMG, Karyawan_ITB, Keluarga_Karyawan_ITB
from ..models import Mitra_Kerja_Sama, Umum
import json

#TODO ubah CRUD jadi 1 fungsi

def pasien_insert(request):
    if(request.method == 'POST'):
        try :
            insert_pasien(request.POST.dict())
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def insert_pasien(post_form):
    try :
        new_pasien = construct_pasien_from_post_form(post_form)
        new_pasien.save()
        new_pasien.no_pasien = 'P-' + str(new_pasien.id)
        new_pasien.save()
        return new_pasien
    except Exception as e:
        raise e

def construct_pasien_from_post_form(post_form):
    kategori = post_form['kategori']
    
    return {
        'Mahasiswa': Mahasiswa,
        'Karyawan BMG': Karyawan_BMG,
        'Karyawan ITB': Karyawan_ITB,
        'Keluarga Karyawan': Keluarga_Karyawan_ITB,
        'Mitra Kerja Sama': Mitra_Kerja_Sama,
        'Umum': Umum
    }.get(kategori)(**post_form)