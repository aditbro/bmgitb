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
from main.services import GetModelList
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
            pasien = model_to_dict(pasien)
            return JsonResponse({'pasien':pasien,'response':'success'}, status=200)
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    @allow_only_roles(['loket', 'admin', 'apotek'])
    def index(self, request):
        try :
            list_params = self.get_list_params(request.GET.dict())
            pasien_list = GetModelList(Pasien, **list_params).call()
            pasien_list = list(map(lambda pasien: pasien.serialize(), pasien_list))
            return JsonResponse({'pasien':pasien_list,'response':'success','code':200})
        except Exception as e:
            response = {'response':'Exception '+e.__str__()}
            return JsonResponse(response, status=400)

    def get_list_params(self, request):
        result_params = {}
        pagination_params = ['page', 'limit', 'kategori', 'sort_field', 'sort_dir']

        for param in pagination_params:
            if param in request:
                result_params[param] = request[param]
                del request[param]

        result_params['search_dict'] = request

        return result_params

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