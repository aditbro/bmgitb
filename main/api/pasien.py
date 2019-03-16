from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.utils.datastructures import MultiValueDictKeyError
from ..models import Pasien, Kelompok_Pasien, Mahasiswa, Pegawai
import json

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

def mahasiswa_insert(request):
    if(request.method == 'POST'):
        pasien = None
        try :
            pasien = insert_pasien(request.POST.dict())
            insert_mahasiswa(request.POST.dict(), pasien)
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            if(pasien is not None):
                delete_pasien(pasien.no_pasien)
            pasien.delete()
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e:
            if(pasien is not None):
                delete_pasien(pasien.no_pasien)
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def pegawai_insert(request):
    if(request.method == 'POST'):
        pasien = None
        try :
            pasien = insert_pasien(request.POST.dict())
            insert_pegawai(request.POST.dict(), pasien)
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            if(pasien is not None):
                delete_pasien(pasien.no_pasien)
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e:
            if(pasien is not None):
                delete_pasien(pasien.no_pasien)
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def pasien_get_list(request, kelompok='pasien'):
    if(request.method == 'GET'):
        try :
            page_number = request.GET['page']
            entry_amount = request.GET['ammount']

            pasien_list = []
            if('search_parameter' in request.GET) :
                search_parameter = request.GET['search_parameter']
                search_value = request.GET['search_value']
                if kelompok == 'pasien' :
                    pasien_list = search_pasien(page_number, entry_amount, {search_parameter : search_value})
                elif kelompok == 'mahasiswa' :
                    pasien_list = search_mahasiswa(page_number, entry_amount, {search_parameter : search_value})
                elif kelompok == 'pegawai' : 
                    pasien_list = search_pegawai(page_number, entry_amount, {search_parameter : search_value})
            else :
                if kelompok == 'pasien' :
                    pasien_list = get_pasien_list(page_number, entry_amount)
                elif kelompok == 'mahasiswa' :
                    pasien_list = get_mahasiswa_list(page_number, entry_amount)
                elif kelompok == 'pegawai' : 
                    pasien_list = get_pegawai_list(page_number, entry_amount)

            return JsonResponse({'response':'success','code':200,'pasien_list':pasien_list})

        except KeyError as e :
            error_message = 'Key {} expected'.format(e.args[0])
            response = {'response':'Key error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e :
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else :
        return defaults.bad_request(request, request.path_info)

def mahasiswa_get_list(request):
    return pasien_get_list(request, 'mahasiswa')

def pegawai_get_list(request):
    return pasien_get_list(request, 'pegawai')

def pasien_get(request, no_pasien):
    if(request.method == 'GET'):
        try :
            pasien = get_pasien(no_pasien)
            
            if(pasien['kelompok_nama'] == 'Mahasiswa'):
                data_mahasiswa = get_mahasiswa(pasien)
                pasien = {'data_mahasiswa':data_mahasiswa, 'pasien':pasien}
            elif(pasien['kelompok_nama'] == 'Pegawai'):
                data_pegawai = get_pegawai(pasien)
                pasien = {'data_pegawai':data_pegawai,'pasien':pasien}

            return JsonResponse(pasien)
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return JsonResponse(response)
    else :
        return defaults.bad_request(request, request.path_info)

def pasien_update(request, no_pasien):
    if(request.method == 'POST'):
        try:
            update_pasien(request.POST.dict(), no_pasien)
            return JsonResponse({'response':'success','code':200})
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message, 'code':400}
            return HttpResponse(json.dumps(response))
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else :
        return defaults.bad_request(request, request.path_info)

def pasien_delete(request, no_pasien):
    if(request.method == 'POST'):
        try:
            delete_pasien(no_pasien)
            return JsonResponse({'response':'success','code':200})
        except Exception as e:
            response = {'response':'Exception '+e.__str__(), 'code':400}
            return HttpResponse(json.dumps(response))
    else:
        return defaults.bad_request(request, request.path_info)

def insert_pasien(post_form):
    try :
        required_column = ['no_pasien', 'nama', 'catatan', 'tipe_kartu_identitas', 'nomor_kartu_identitas', 'tempat_lahir', 'tanggal_lahir', 'alamat', 'kota', 'active', 'gender', 'email', 'no_telepon', 'no_hp', 'berat_badan', 'tinggi_badan', 'organisasi', 'kelompok', 'golongan_darah', 'rhesus']
        post_form = get_required_dict(required_column, post_form)

        if('kelompok' in post_form):
            post_form['kelompok'] = Kelompok_Pasien.objects.get(kode=post_form['kelompok'])
        else :
            raise Exception('Kelompok pasien tidak ada')

        new_pasien = Pasien(**post_form)
        new_pasien.save()
        new_pasien.no_pasien = 'P-' + str(new_pasien.id)
        new_pasien.save()
        return new_pasien
    except Exception as e:
        raise e

def insert_mahasiswa(post_form, pasien):
    try :
        required_column = ['nim', 'strata', 'internasional', 'tpb', 'program_studi', 'fakultas']
        post_form = get_required_dict(required_column, post_form)
        print(post_form)
        new_mahasiswa = Mahasiswa(no_pasien=pasien, **post_form)
        new_mahasiswa.save()
        return new_mahasiswa
    except Exception as e:
        raise e

def insert_pegawai(post_form, pasien):
    try :
        required_column = ['nip']
        post_form = get_required_dict(required_column, post_form)
        print(post_form)
        new_pegawai = Pegawai(no_pasien=pasien, **post_form)
        new_pegawai.save()
        return new_pegawai
    except Exception as e:
        raise e

def get_pasien(no_pasien):
    try :
        pasien = Pasien.objects.get(no_pasien=no_pasien)
        pasien = model_to_dict(pasien)
        kelompok_pasien = Kelompok_Pasien.objects.get(kode=pasien['kelompok'])
        kelompok_pasien = rename_dict('kelompok_',model_to_dict(kelompok_pasien))
        data_pasien = {**pasien, **kelompok_pasien}
        return data_pasien
    except Pasien.DoesNotExist as e:
        raise Http404(e.__str__())
    except Exception as e:
        raise e

def get_mahasiswa(pasien):
    try :
        mahasiswa = Mahasiswa.objects.get(no_pasien__pk=pasien['id'])
        mahasiswa = model_to_dict(mahasiswa)
        return mahasiswa
    except Pasien.DoesNotExist as e:
        raise Http404(e.__str__())
    except Exception as e:
        raise e

def get_pegawai(pasien):
    try :
        pegawai = Mahasiswa.objects.get(no_pasien__pk=pasien['id'])
        pegawai = model_to_dict(pegawai)
        return pegawai
    except Pasien.DoesNotExist as e:
        raise Http404(e.__str__())
    except Exception as e:
        raise e

def get_pasien_list(page_number, entry_amount):
    try :
        list_start = (int(page_number)-1)*int(entry_amount)
        list_end = list_start + int(entry_amount) + 1
        pasien_list = Pasien.objects.all()[list_start:list_end]
        pasien_list = list(pasien_list)
        return model_list_to_list_of_dict(pasien_list)
    except Exception as e:
        raise e

def get_mahasiswa_list(page_number, entry_amount):
    try :
        list_start = (int(page_number)-1)*int(entry_amount)
        list_end = list_start + int(entry_amount) + 1
        mahasiswa_list = Mahasiswa.objects.all()[list_start:list_end]
        mahasiswa_list = list(mahasiswa_list)
        return model_list_to_list_of_dict(mahasiswa_list)
    except Exception as e:
        raise e

def get_pegawai_list(page_number, entry_amount):
    try :
        list_start = (int(page_number)-1)*int(entry_amount)
        list_end = list_start + int(entry_amount) + 1
        pegawai_list = Pegawai.objects.all()[list_start:list_end]
        pegawai_list = list(pegawai_list)
        return model_list_to_list_of_dict(pegawai_list)
    except Exception as e:
        raise e

def search_pasien(page_number, entry_amount, search_query):
    try : 
        list_start = (int(page_number)-1)*int(entry_amount)
        list_end = list_start + int(entry_amount) + 1
        pasien_list = Pasien.objects.all().filter(**search_query)[list_start:list_end]
        pasien_list = list(pasien_list)
        return model_list_to_list_of_dict(pasien_list)
    except Exception as e:
        raise e

def search_mahasiswa(page_number, entry_amount, search_query):
    try : 
        list_start = (int(page_number)-1)*int(entry_amount)
        list_end = list_start + int(entry_amount) + 1
        mahasiswa_list = Mahasiswa.objects.all().filter(**search_query)[list_start:list_end]
        mahasiswa_list = list(mahasiswa_list)
        return model_list_to_list_of_dict(mahasiswa_list)
    except Exception as e:
        raise e

def search_pegawai(page_number, entry_amount, search_query):
    try : 
        list_start = (int(page_number)-1)*int(entry_amount)
        list_end = list_start + int(entry_amount) + 1
        pegawai_list = Pegawai.objects.all().filter(**search_query)[list_start:list_end]
        pegawai_list = list(pegawai_list)
        return model_list_to_list_of_dict(pegawai_list)
    except Exception as e:
        raise e

def update_pasien(post_form, no_pasien):
    try :
        id_pasien = no_pasien[2:]
        pasien = Pasien.objects.get(no_pasien=no_pasien)

        if('kelompok' in post_form):
            post_form['kelompok'] = Kelompok_Pasien.objects.get(kode=post_form['kelompok'])

        pasien = Pasien(id=id_pasien, no_pasien=no_pasien, **post_form)
        pasien.save()
        return pasien
    except Pasien.DoesNotExist as e:
        raise Http404(e.__str__())
    except Exception as e:
        raise e

def delete_pasien(no_pasien):
    try :
        pasien = Pasien.objects.get(no_pasien=no_pasien)
        pasien.delete()
        return pasien
    except Exception as e:
        raise e

def parse_exception(exception):
    return exception.__str__().replace('"','').replace('(','').replace(')','').split(',')

def rename_dict(prefix, old_dict):
    new_dict = {}
    for key in old_dict:
        new_dict[prefix+key] = old_dict[key]
    
    return new_dict

def get_required_dict(required_column, old_dict):
    new_dict = {}
    for key in required_column:
        if(key in old_dict):
            new_dict[key] = old_dict[key]

    return new_dict

def model_list_to_list_of_dict(model_list):
    list_of_dict = [model_to_dict(model) for model in model_list]
    return list_of_dict