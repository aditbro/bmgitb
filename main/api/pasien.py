from django.http import JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from .helper import *
from .auth_decorators import allow_only_roles
from ..models import Pasien, Mahasiswa, Karyawan_BMG, Karyawan_ITB, Keluarga_Karyawan_ITB
from ..models import Mitra_Kerja_Sama, Umum
import json
import traceback
import pry
from main.services.pasien import PasienCreator, PasienFetcher
from main.services import GetModelList, get_list_params
from .base_controller import BaseController

class PasienController(BaseController):
    @allow_only_roles(['loket', 'admin'])
    def create(self, request):
        try :
            PasienCreator(json.loads(request.body)).create()
            return JsonResponse({'response':'success'}, status=200)
        except IntegrityError as e:
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message}
            return JsonResponse(response, status=400)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    @allow_only_roles(['loket', 'admin', 'apotek'])
    def get(self, request, no_pasien):
        try :
            pasien = PasienFetcher(no_pasien).fetch()
            pasien_dict = pasien.serialize()
            pasien_dict['subsidi'] = pasien.serialize_subsidi()

            return JsonResponse({'pasien':pasien_dict,'response':'success'}, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    @allow_only_roles(['loket', 'admin', 'apotek'])
    def index(self, request):
        try :
            list_params = get_list_params(request.GET.dict())
            pasien_list = GetModelList(Pasien, **list_params).call()
            pasien_list = list(map(lambda pasien: pasien.serialize(), pasien_list))
            pasien_count = Pasien.objects.count()

            data = { 
                'pasien': pasien_list,
                'response': 'success',
                'pasien_count' : pasien_count
            }
            
            return JsonResponse(data, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    @allow_only_roles(['loket', 'admin', 'apotek'])
    def update(self, request, no_pasien):
        try :
            request = json.loads(request.body)
            pasien = PasienFetcher(no_pasien).fetch()
            Pasien.objects.filter(id=pasien.id).update(**request)
            return JsonResponse({'response':'success'}, status=200)
        except IntegrityError as e:
            traceback.print_exc()
            error_message = parse_exception(e)[1]
            response = {'response':'Integrity error '+error_message}
            return JsonResponse(response, status=400)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)