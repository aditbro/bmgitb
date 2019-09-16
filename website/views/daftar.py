from django.forms.models import model_to_dict
from django.shortcuts import render
from main.models import Client
from .main import *
from .auth import *

@allow_only_roles(['admin', 'loket'])
def daftar_pasien(request):
    context = {'Resource': 'Pasien'}
    return render(request, 'website/common_daftar_page.html', context)

@allow_only_roles(['admin', 'loket'])
def daftar_kunjungan(request):
    context = {'Resource': 'Kunjungan'}
    return render(request, 'website/common_daftar_page.html', context)

@allow_only_roles(['admin', 'apotek'])
def daftar_pembelian_resep(request):
    context = {'Resource': 'PembelianResep'}
    return render(request, 'website/common_daftar_page.html', context)

@allow_only_roles(['admin', 'apotek'])
def daftar_pembelian_otc(request):
    context = {'Resource': 'PembelianOTC'}
    return render(request, 'website/common_daftar_page.html', context)