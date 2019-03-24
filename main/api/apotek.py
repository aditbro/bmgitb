# from django.views import defaults
# from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
# from django.db import IntegrityError
# from django.forms.models import model_to_dict
# from .helper import *
# import json


# def pembelian_resep_insert(request):
#     if(request.method == 'POST'):
#         try:
#             insert_pembelian_resep(request.POST.dict())
#             return JsonResponse({'response':'success','code':200})
#         except IntegrityError as e:
#             error_message = parse_exception(e)[1]
#             response = {'response':'Integrity error '+error_message, 'code':400}
#             return HttpResponse(json.dumps(response))
#         except Exception as e :
#             response = {'response':'Exception '+e.__str__(), 'code':400}
#             return HttpResponse(json.dumps(response))
#     else:
#         return defaults.bad_request(request, request.path_info)

# def insert_pembelian_resep(data_pembelian):
#     try:
#         required_column = ['pasien', 'kunjungan']
#         dict_pembelian = get_required_dict(required_column, data_pembelian)
#         dict_pembelian['pasien'] = Pasien.objects.get(no_pasien=dict_pembelian['pasien'])
#         dict_pembelian['kunjungan'] = Kunjungan.objects.get(kode=dict_pembelian['kunjungan'])

#         new_pembelian = Kunjungan(**dict_pembelian)
#         new_pembelian.save()

#         insert_pembelian_obat_resep(new_pembelian, data_pembelian['obat'])

#         return new_pembelian
#     except Exception as e:
#         raise e

# def insert_pembelian_obat_resep(pembelian, data_obat) :
#     tarif = 0
#     subsidi = 0
#     bayar = 0

#     for obat in data_obat :
#         data_pembelian = {}
#         data_pembelian['pembelianResep'] = pembelian
#         data_pembelian['obat'] = Obat.objects.get(kode=obat['kode'])
#         data_pembelian['jumlah'] = obat['jumlah']
#         data_pembelian['satuan'] = obat['satuan']

#         tarif = tarif + data_pembelian['obat'].harga_resep * data_pembelian['jumlah']
        
#         new_pembelian_obat_resep = PembelianResep(**pembelian)
#         new_pembelian_obat_resep.save()

#     subsidi = pembelian.pasien.get_subsidi_obat()
#     subsidi = subsidi if subsidi <= tarif else tarif
#     bayar = tarif - subsidi

#     pembelian.tarif = tarif
#     pembelian.subsidi = subsidi
#     pembelian.bayar = bayar
#     pembelian.save()