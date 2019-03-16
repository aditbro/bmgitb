from django.db import models
from .pasien import Pasien

_short_length = 100
_medium_length = 255
_long_length = 800

class Obat(models.Model):
    kode = models.CharField(max_length=_short_length, primary_key=True)
    nama = models.CharField(max_length=_short_length)
    jumlah_stok = models.IntegerField()
    keterangan = models.CharField(max_length=_long_length)
    harga_otc = models.IntegerField()
    harga_resep = models.IntegerField()

class PembelianOTC(models.Model):
    tarif = models.IntegerField()
    bayar = models.IntegerField()
    obat = models.ManyToManyField('Obat')

class PembelianResep(models.Model):
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASADE)
    tarif = models.IntegerField()
    subsidi = models.IntegerField()
    bayar = models.IntegerField()
    obat = models.ManyToManyField('Obat')

