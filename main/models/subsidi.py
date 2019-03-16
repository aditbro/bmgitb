from django.db import models
from .pasien import Kelompok_Pasien, Pasien
from .klinik import Tindakan, Kunjungan, Klinik
from .apotek import Pembelian

_short_length = 100
_medium_length = 255
_long_length = 800

class Subsidi_Tindakan(models.Model):
    nama = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()    
    sisa_subsidi_tahunan = models.IntegerField()

class Subsidi_Obat(models.Model):
    nama = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    pembelian = models.OneToOneField('Pembelian', on_delete=models.CASCADE)
    pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_pembelian = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

class Subsidi_Kunjungan(models.Model):
    pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    klinik = models.ManyToOneField('Klinik', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()