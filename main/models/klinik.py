from django.db import models

_short_length = 100
_medium_length = 255
_long_length = 800

class Dokter(models.Model):
    kode = models.CharField(max_length=_short_length, unique=True)
    nama = models.CharField(max_length=_medium_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama + ', klinik ' + self.klinik.nama 

class Klinik(models.Model):
    kode = models.CharField(max_length=_short_length, unique=True)
    nama = models.CharField(max_length=_short_length)
    tarif_kunjungan = models.IntegerField()
    is_subsidi = models.CharField(max_length=_short_length, default='False')
    is_cash = models.CharField(max_length=_short_length, default='True')

    def __str__(self):
        return self.nama

class Diagnosis(models.Model):
    nama = models.CharField(max_length=_medium_length)
    kode = models.CharField(max_length=_short_length, primary_key=True)
    keterangan = models.CharField(max_length=_long_length)
    
    def __str__(self):
        return self.nama

class Tindakan(models.Model):
    nama = models.CharField(max_length=_medium_length)
    kode = models.CharField(max_length=_short_length, primary_key=True)
    keterangan = models.CharField(max_length=_long_length)
    tarif = models.IntegerField()
    is_subsidi = models.CharField(max_length=_short_length, default='False')
    is_cash = models.CharField(max_length=_short_length, default='True')

    def __str__(self):
        return self.nama