from django.db import models
# from .pasien import Pasien

_short_length = 100
_medium_length = 255
_long_length = 800

class Obat(models.Model):
    kode = models.CharField(max_length=_short_length, primary_key=True)
    nama = models.CharField(max_length=_short_length)
    jumlah_stok = models.IntegerField()
    satuan = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    harga_otc = models.IntegerField()
    harga_resep = models.IntegerField()

class PembelianObatOTC(models.Model):
    pembelianOTC = models.ForeignKey('PembelianOTC', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    obat = models.ForeignKey('Obat', on_delete=models.CASCADE)

class PembelianObatResep(models.Model):
    pembelianResep = models.ForeignKey('PembelianResep', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    obat = models.ForeignKey('Obat', on_delete=models.CASCADE)

class PembelianOTC(models.Model):
    tarif = models.IntegerField()
    bayar = models.IntegerField()
    waktu_pembelian = models.DateTimeField(auto_now_add=True)

class PembelianResep(models.Model):
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    tarif = models.IntegerField()
    subsidi = models.IntegerField()
    bayar = models.IntegerField()
    waktu_pembelian = models.DateTimeField(auto_now_add=True)

    #TODO tambahin method __init__()
    #init harus ngitung tarif, subsidi, dan bayar
