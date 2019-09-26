from django.db import models
from .pasien import Pasien
from .klinik import Klinik, Dokter, Tindakan, Diagnosis
from .subsidi import Subsidi_Tindakan
from datetime import datetime
from django.forms.models import model_to_dict
from faker import Faker

_short_length = 100
_medium_length = 255
_long_length = 800

class Kunjungan(models.Model):
    kode = models.CharField(max_length=_short_length, null=True, blank=True)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    dokter = models.ForeignKey('Dokter', on_delete=models.CASCADE)
    tarif = models.IntegerField()
    klaim = models.IntegerField()
    cash = models.IntegerField()
    koreksi = models.ForeignKey('Kunjungan', on_delete=models.SET_NULL, null=True, blank=True)
    asal = models.CharField(max_length=_short_length, null=True, blank=True)
    waktu_kunjungan = models.DateTimeField(auto_now_add=True, blank=True)
    is_valid = models.BooleanField(blank=True, default=True)

    @classmethod
    def new_id(cls):
        return 'Ku-' + Faker().uuid4(cast_to=str)[:8]

    def serialize(self):
        kunjungan = model_to_dict(self)
        kunjungan['pasien'] = self.pasien.serialize()
        kunjungan['klinik'] = self.klinik.serialize()
        kunjungan['dokter'] = self.dokter.serialize()
        kunjungan['waktu_kunjungan'] = str(self.waktu_kunjungan.strftime("%d %b %Y %H:%M"))
        

        return kunjungan

    def save_waktu_kunjungan(self):
        if(not self.waktu_kunjungan):
            self.waktu_kunjungan = datetime.now()

    def restore_subsidi_pasien(self):
        tindakan_kunjungan = Tindakan_Kunjungan.objects.filter(kunjungan__id=self.id)

        for tindakan in tindakan_kunjungan :
            tindakan.restore_subsidi_pasien()


    def __str__(self):
        return self.pasien.nama + ' ' + self.klinik.nama

class Tindakan_Kunjungan(models.Model):
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    cash = models.IntegerField()
    klaim = models.IntegerField()
        
class Diagnosis_Kunjungan(models.Model):
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    Diagnosis = models.ManyToManyField('Diagnosis')

class Parameter_Tarif_Kunjungan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    tarif = models.IntegerField()

    def __str__(self):
        return 'harga kunjungan ' + self.kategori_pasien