from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from main.models import Pasien, Mahasiswa
from main.models import Kunjungan, Tindakan_Kunjungan
from main.services import GetModelList, get_list_params
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
            Kunjungan.create(**form_data)
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

    @allow_only_roles(['loket', 'admin', 'apotek'])
    def update(self, request):
        if(request.method == 'POST'):
            try :
                self.update_kunjungan(json.loads(request.body))
                return JsonResponse({'response':'success'}, status=200)
            except Exception as e:
                response = {'response':'Exception '+e.__str__()}
                return JsonResponse(response, status=400)
        else:
            return defaults.bad_request(request, request.path_info)

    def update_kunjungan(self, post_form):
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