from django.db import models
from .pasien import Pasien
from .klinik import Klinik, Dokter, Tindakan, Diagnosis
from .subsidi import Subsidi_Tindakan
from datetime import datetime

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
    waktu_kunjungan = models.DateTimeField(blank=True)
    is_valid = models.BooleanField(blank=True, default=True)

    def __init__(self, *args, **kwargs):
        required_column = ['pasien', 'klinik', 'dokter']
        construction_parameter = {}

        for key,value in kwargs.items() :
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if(not args and kwargs):        
            if required_column :
                raise Exception("missing parameter(s) " + ", ".join(required_column))

            construction_parameter['pasien'] = Pasien.objects.get(no_pasien=kwargs['pasien'])
            construction_parameter['klinik'] = Klinik.objects.get(kode=kwargs['klinik'])
            construction_parameter['dokter'] = Dokter.objects.get(kode=kwargs['dokter'])
            construction_parameter['tarif'] = Parameter_Tarif_Kunjungan.objects.get(kategori_pasien=construction_parameter['pasien'].kategori).tarif
            construction_parameter['cash'] = construction_parameter['tarif']
            construction_parameter['klaim'] = 0

        super().__init__(*args, **construction_parameter)

    def save(self):
        self.save_waktu_kunjungan()
        super().save()
        self.insert_kode_kunjungan()
        super().save()

    def insert_kode_kunjungan(self):
        if(not self.kode):
            self.kode = 'K-' + str(self.id)

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

    def __init__(self, *args, **kwargs):
        required_column = ['kunjungan', 'tindakan', 'cash', 'klaim']
        construction_parameter = {}

        for key,value in kwargs.items() :
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if(not args and kwargs):        
            if required_column :
                raise Exception("missing parameter(s) " + ", ".join(required_column))

            construction_parameter['kunjungan'] = Kunjungan.objects.get(id=kwargs['kunjungan'])
            construction_parameter['tindakan'] = Tindakan.objects.get(kode=kwargs['tindakan'])

        super().__init__(*args, **construction_parameter)

    def save(self):
        if(self.tindakan.is_subsidi):
            self.reduce_subsidi_pasien()
            
        super().save()

    def reduce_subsidi_pasien(self):
        subsidi_pasien = Subsidi_Tindakan.objects.filter(pasien__id=self.kunjungan.pasien.id, tindakan=self.tindakan)[0]
        if(subsidi_pasien):
            subsidi_pasien.sisa_subsidi_bulan_ini -= self.klaim
            subsidi_pasien.sisa_subsidi_tahunan -= self.klaim

            if(subsidi_pasien.sisa_subsidi_bulan_ini < 0 or subsidi_pasien.sisa_subsidi_tahunan < 0) :
                raise Exception('Sisa subsidi pasien kurang untuk tindakan {}'.format(self.tindakan.nama))

            subsidi_pasien.save()

    def restore_subsidi_pasien(self):
        subsidi_pasien = Subsidi_Tindakan.objects.filter(pasien__id=self.kunjungan.pasien.id, tindakan=self.tindakan)[0]
        if(subsidi_pasien):
            subsidi_pasien.sisa_subsidi_bulan_ini += self.klaim
            subsidi_pasien.sisa_subsidi_tahunan += self.klaim
            subsidi_pasien.save()
        
class Diagnosis_Kunjungan(models.Model):
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    Diagnosis = models.ManyToManyField('Diagnosis')

class Parameter_Tarif_Kunjungan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    tarif = models.IntegerField()

    def __str__(self):
        return 'harga kunjungan ' + self.kategori_pasien