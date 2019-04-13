from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from .helper import *
from .auth_decorators import *
from ..models import PembelianResep, PembelianObatResep, Obat, PembelianObatOTC, PembelianOTC
import json
import traceback

@allow_only_roles(['admin', 'apotek_resep'])
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
            traceback.print_exc()
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
    else :
        return defaults.page_not_found(request, request.path_info)

def insert_pembelian_resep(post_form):
    list_obat = post_form['obat']
    list_obat_result = []

    for obat in list_obat :
        obat['obat'] = Obat.objects.get(kode=obat['obat'])
        new_obat = PembelianObatResep(**obat)
        new_obat.save()
        list_obat_result.append(new_obat)
        
    pembelian_resep = PembelianResep(**post_form)
    pembelian_resep.save()

    for obat in list_obat_result :
        pembelian_resep.obat.add(obat)

    pembelian_resep.save()
    
@allow_only_roles(['loket', 'admin', 'apotek_otc'])
def pembelian_otc_insert(request):
    if(request.method == 'POST'):
        try :
            insert_pembelian_otc(json.loads(request.body))
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

def insert_pembelian_otc(post_form):
    list_obat = post_form['obat']
    list_obat_result = []

    for obat in list_obat :
        obat['obat'] = Obat.objects.get(kode=obat['obat'])
        new_obat = PembelianObatOTC(**obat)
        new_obat.save()
        list_obat_result.append(new_obat)

    pembelian_otc = PembelianOTC(**post_form)
    pembelian_otc.save()

    for obat in list_obat_result :
        pembelian_otc.obat.add(obat)

    pembelian_otc.save()
    