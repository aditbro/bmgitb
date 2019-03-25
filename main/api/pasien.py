from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.utils.datastructures import MultiValueDictKeyError
from .helper import *
from ..models import Pasien, Mahasiswa, Karyawan_BMG, Karyawan_ITB, Keluarga_Karyawan_ITB
from ..models import Mitra_Kerja_Sama, Umum

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

def pasien_get(request, no_pasien):
    if(request.method == 'GET'):
        try :
            pasien = get_pasien(no_pasien)
            pasien = model_to_dict(pasien)
            return JsonResponse({'pasien':pasien,'response':'success','code':200})
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def get_pasien(no_pasien):
    pasien = get_pasien_with_category(no_pasien)
    return pasien

def get_pasien_with_category(no_pasien):
    pasien = Pasien.objects.get(no_pasien=no_pasien)
    kategori = pasien.kategori

    return {
        'Mahasiswa': Mahasiswa,
        'Karyawan BMG': Karyawan_BMG,
        'Karyawan ITB': Karyawan_ITB,
        'Keluarga Karyawan': Keluarga_Karyawan_ITB,
        'Mitra Kerja Sama': Mitra_Kerja_Sama,
        'Umum': Umum
    }.get(kategori).objects.get(no_pasien=pasien.no_pasien)

def pasien_get_list(request):
    if(request.method == 'GET'):
        try :
            pasien_list = get_pasien_list(request.GET.dict())
            pasien_list = transform_pasien_list_to_dict_list(pasien_list)
            return JsonResponse({'pasien':pasien_list,'response':'success','code':200})
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def get_pasien_list(get_form):
    required_information = ['page', 'entry_per_page', 'kategori', 'sort_field', 'sort_dir']
    default_value = {
        'page' : 1,
        'entry_per_page' : 10,
        'kategori' : 'Pasien',
        'sort_field' : 'no_pasien',
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
    pasien_class = get_pasien_kategori_class(base_info_form['kategori'])
    sort_parameter = get_sort_parameter(base_info_form['sort_field'], base_info_form['sort_dir'])

    pasien_list = pasien_class.objects.filter(**get_form).order_by(sort_parameter)[start:end]
    return pasien_list

def get_entry_range_from_page(page_num, entry_num):
    start = (page_num-1) * entry_num
    end = start + entry_num

    return start, end

def get_pasien_kategori_class(kategori):
    return {
        'Mahasiswa': Mahasiswa,
        'Karyawan BMG': Karyawan_BMG,
        'Karyawan ITB': Karyawan_ITB,
        'Keluarga Karyawan': Keluarga_Karyawan_ITB,
        'Mitra Kerja Sama': Mitra_Kerja_Sama,
        'Umum': Umum, 
        'Pasien': Pasien
    }.get(kategori, Pasien)

def get_sort_parameter(field, direction):
    if direction == 'asc':
        direction = ''
    else :
        direction = '-'

    return direction + field

def transform_pasien_list_to_dict_list(pasien_list):
    psn_list = []
    for pasien in pasien_list :
        pasien_dict = model_to_dict(pasien)
        pasien_dict['waktu_registrasi'] = pasien.waktu_registrasi.strftime('%Y-%m-%d %H:%M')
        psn_list.append(pasien_dict)

    return psn_list

def pasien_update(request):
    if(request.method == 'POST'):
        try :
            update_pasien(request.POST.dict())
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            traceback.print_exc()
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def update_pasien(post_form):
    if not 'no_pasien' in post_form :
        raise Exception('no_pasien parameter missing')
    
    no_pasien = post_form['no_pasien']
    pasien = Pasien.objects.get(no_pasien=no_pasien)
    updated_pasien = construct_pasien_from_post_form(post_form)

    updated_pasien.id = pasien.id
    updated_pasien.no_pasien = pasien.no_pasien
    pasien.delete()
    updated_pasien.save()
    return updated_pasien