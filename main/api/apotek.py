from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError, transaction
from django.forms.models import model_to_dict
from main.api import BaseController
from main.models import PembelianResep, PembelianObatResep, Obat, PembelianObatOTC, PembelianOTC, Pasien
from main.services import GetModelList, get_list_params
from .helper import *
from .auth_decorators import *
import json
import traceback

class ApotekController(BaseController):
    PembelianObatClass = None
    PembelianClass = None

    def create(self, request):
        try:
            params = json.loads(request.body)
            params['pasien'] = Pasien.objects.get(no_pasien=params['pasien'])
            list_obat = params.pop('obat')
            pembelian = params

            with transaction.atomic():
                pembelian = self.insert_pembelian(pembelian)
                self.insert_obat(pembelian, list_obat)
            
            return JsonResponse({'response':'success'}, status=200)
        except Exception as e:
            traceback.print_exc()
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    def get(self, request, id):
        try:
            pembelian = self.PembelianClass.objects.get(id=id)
            pembelian = pembelian.serialize()
            return JsonResponse({'pembelian':pembelian,'response':'success'}, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    def index(self, request):
        try :
            list_params = get_list_params(request.GET.dict())
            pembelian_list = GetModelList(self.PembelianClass, **list_params).call()
            pembelian_list = list(map(lambda pembelian: pembelian.serialize(), pembelian_list))

            data = { 
                'pembelian': pembelian_list,
                'response': 'success',
            }
            
            return JsonResponse(data, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)
        

    def insert_pembelian(self, pembelian):
        pembelian = self.PembelianClass(**pembelian)
        pembelian.save()
        
        return pembelian

    def insert_obat(self, pembelian, list_obat):
        for data in list_obat :
            data['obat'] = Obat.objects.get(kode=data['obat'])
            pembelian_obat = self.PembelianObatClass(**data)
            pembelian_obat.save()
            pembelian.obat.add(pembelian_obat)

class ApotekResepController(ApotekController):
    PembelianObatClass = PembelianObatResep
    PembelianClass = PembelianResep

class ApotekOTCController(ApotekController):
    PembelianObatClass = PembelianObatOTC
    PembelianClass = PembelianOTC