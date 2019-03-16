from django.views import defaults
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.db import IntegrityError
from django.forms.models import model_to_dict
from ..models import Pasien, Kelompok_Pasien, Mahasiswa, Pegawai
from ..models import Kunjungan, Diagnosis, Klinik, Dokter
from ..models import Obat, Pembelian, PembelianObat
import json



