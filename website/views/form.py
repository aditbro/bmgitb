from django.forms.models import model_to_dict
from django.shortcuts import render
from main.models import Client, Pasien, Kunjungan, PembelianOTC, PembelianResep
from .main import *
from .auth import *

# @allow_only_roles(['admin', 'loket', 'diagnosis'])
def data_pasien(request, no_pasien):
    pasien = Pasien.objects.get(no_pasien=no_pasien)
    pasien = pasien.get_child_data()
    context = {
        'Resource': 'Pasien',
        'pasien': pasien.serialize(),
        'kategori_pasien': Pasien.KATEGORI_CHOICES,
        'button_status': 'disabled'
    }
    return render(request, 'website/common_form_page.html', context)

def form_insert_pasien(request):
    context = {
        'Resource': 'Pasien',
        'kategori_pasien': Pasien.KATEGORI_CHOICES,
    }
    return render(request, 'website/common_form_page.html', context)

@allow_only_roles(['admin', 'loket', 'diagnosis'])
def data_kunjungan(request):
    context = {'Resource': 'Kunjungan'}
    return render(request, 'website/common_daftar_page.html', context)

@allow_only_roles(['admin', 'apotek'])
def data_pembelian_resep(request):
    context = {'Resource': 'PembelianResep'}
    return render(request, 'website/common_daftar_page.html', context)

@allow_only_roles(['admin', 'apotek'])
def data_pembelian_otc(request):
    context = {'Resource': 'PembelianOTC'}
    return render(request, 'website/common_daftar_page.html', context)