from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from main.models import Pasien, Mahasiswa
from main.models import Kunjungan, Tindakan_Kunjungan
from main.services import GetModelList, get_list_params, KunjunganCreator
from .helper import *
from .auth_decorators import *
from .base_controller import BaseController
import json
import traceback
import pry

class KunjunganController(BaseController):    
    @allow_only_roles(['loket', 'admin'])
    def create(self, request):
        try :
            form_data = json.loads(request.body)
            KunjunganCreator(form_data).cal()
            return JsonResponse({'response':'success'}, status=200)
        except Exception as e:
            traceback.print_exc()
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    @allow_only_roles(['loket', 'admin', 'apotek', 'administrasi'])
    def get(self, request, kode_kunjungan):
        try :
            kunjungan = Kunjungan.objects.get(kode=kode_kunjungan, is_valid=True)
            kunjungan = kunjungan.serialize()
            return JsonResponse({'kunjungan':kunjungan, 'response':'success'}, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    @allow_only_roles(['loket', 'admin', 'apotek'])
    def index(self, request):
        try :
            list_params = get_list_params(request.GET.dict())
            kunjungan_list = GetModelList(Kunjungan, **list_params).call()
            kunjungan_list = list(map(lambda kunjungan: kunjungan.serialize(), kunjungan_list))

            data = { 
                'kunjungan': kunjungan_list,
                'response': 'success'
            }
            
            return JsonResponse(data, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    # @allow_only_roles(['loket', 'admin'])
    # def update(self, request):
    #     try :
    #         self.update_kunjungan(json.loads(request.body))
    #         return JsonResponse({'response':'success'}, status=200)
    #     except Exception as e:
    #         response = {'response':'Exception '+e.__str__()}
    #         return JsonResponse(response, status=400)