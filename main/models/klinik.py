from django.db import models

_short_length = 100
_medium_length = 255
_long_length = 800

class Dokter(models.Model):
    kode = models.CharField(max_length=_short_length, unique=True)
    nama = models.CharField(max_length=_medium_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)

class Klinik(models.Model):
    kode = models.CharField(max_length=_short_length, unique=True)
    nama = models.CharField(max_length=_short_length)
    tarif_kunjungan = models.IntegerField()
    is_subsidi = models.CharField(max_length=_short_length, default='False')
    is_cash = models.CharField(max_length=_short_length, default='True')

class Kunjungan(models.Model):
    kode = models.CharField(max_length=_short_length, unique=True)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    dokter = models.ForeignKey('Dokter', on_delete=models.CASCADE)
    asal = models.CharField(max_length=_short_length)
    tarif = models.IntegerField()
    klaim = models.IntegerField()
    cash = models.IntegerField()
    koreksi = models.ForeignKey('Kunjungan', on_delete=models.SET_NULL, null=True)
    waktu_kunjungan = models.DateTimeField(auto_now_add=True)

class Diagnosis(models.Model):
    nama = models.CharField(max_length=_medium_length)
    kode = models.CharField(max_length=_short_length, primary_key=True)
    keterangan = models.CharField(max_length=_long_length)

class Tindakan(models.Model):
    nama = models.CharField(max_length=_medium_length)
    kode = models.CharField(max_length=_short_length, primary_key=True)
    keterangan = models.CharField(max_length=_long_length)
    tarif = models.IntegerField()
    is_subsidi = models.CharField(max_length=_short_length, default='False')
    is_cash = models.CharField(max_length=_short_length, default='True')

class Tindakan_Kunjungan(models.Model):
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    cash = models.IntegerField()
    klaim = models.IntegerField()

class Diagnosis_Kunjungan(models.Model):
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    Diagnosis = models.ManyToManyField('Diagnosis')

class Tarif_Kunjungan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    tarif = models.IntegerField()