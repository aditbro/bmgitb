from django.db import models
from django.forms.models import model_to_dict
from .klinik import Klinik, Tindakan

_short_length = 100
_medium_length = 255
_long_length = 800

class Subsidi(models.Model):
    def substract(self, amount):
        if(amount > self.max_subsidi_per_kunjungan or amount > self.sisa_subsidi_bulan_ini):
            raise Exception("Sisa subsidi tidak mencukupi")

        self.sisa_subsidi_bulan_ini -= amount
        self.sisa_subsidi_tahunan -= amount
        self.save()

class Subsidi_Tindakan(Subsidi):
    keterangan = models.CharField(max_length=_long_length, null=True, blank=True)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField(null=True, blank=True)
    sisa_subsidi_bulan_ini = models.IntegerField(null=True, blank=True)    
    sisa_subsidi_tahunan = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_from_parameter(cls, pasien):
        kategori = pasien.kategori
        list_parameter = Parameter_Subsidi_Tindakan.objects.filter(kategori_pasien=kategori)

        for parameter in list_parameter :
            parameter_subsidi = parameter.to_dict()
            parameter_subsidi['pasien'] = pasien
            parameter_subsidi.pop("kategori_pasien")
            parameter_subsidi.pop("kode")
            
            subsidi = cls(**parameter_subsidi)
            subsidi.save()

class Subsidi_Obat(Subsidi):
    keterangan = models.CharField(max_length=_long_length, null=True, blank=True)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField(null=True, blank=True)
    sisa_subsidi_bulan_ini = models.IntegerField(null=True, blank=True)    
    sisa_subsidi_tahunan = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_from_parameter(cls, pasien):
        kategori = pasien.kategori
        list_parameter = Parameter_Subsidi_Obat.objects.filter(kategori_pasien=kategori)

        for parameter in list_parameter :
            parameter_subsidi = parameter.to_dict()
            parameter_subsidi['pasien'] = pasien
            parameter_subsidi.pop("kategori_pasien")
            parameter_subsidi.pop("kode")

            subsidi = cls(**parameter_subsidi)
            subsidi.save()

class Subsidi_Kunjungan(Subsidi):
    keterangan = models.CharField(max_length=_long_length, null=True, blank=True)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField(null=True, blank=True)
    sisa_subsidi_bulan_ini = models.IntegerField(null=True, blank=True)    
    sisa_subsidi_tahunan = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_from_parameter(cls, pasien):
        kategori = pasien.kategori
        list_parameter = Parameter_Subsidi_Kunjungan.objects.filter(kategori_pasien=kategori)

        for parameter in list_parameter :
            parameter_subsidi = parameter.to_dict()
            parameter_subsidi['pasien'] = pasien
            parameter_subsidi.pop("kategori_pasien")
            parameter_subsidi.pop("kode")

            subsidi = cls(**parameter_subsidi)
            subsidi.save()

class Parameter_Subsidi_Tindakan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length, null=True, blank=True)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()    
    sisa_subsidi_tahunan = models.IntegerField()

    def __str__(self):
        return 'subsidi ' + self.tindakan.nama + ' untuk ' + self.kategori_pasien

    def to_dict(self):
        subsidi = model_to_dict(self)
        subsidi['tindakan'] = self.tindakan
        
        return subsidi

class Parameter_Subsidi_Obat(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

    def __str__(self):
        return 'subsidi pembelian obat untuk ' + self.kategori_pasien

    def to_dict(self):
        subsidi = model_to_dict(self)
        return subsidi

class Parameter_Subsidi_Kunjungan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=_long_length)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

    def __str__(self):
        return 'subsidi kunjungan ' + self.klinik.nama + ' untuk ' + self.kategori_pasien

    def to_dict(self):
        subsidi = model_to_dict(self)
        subsidi['klinik'] = self.klinik
        
        return subsidi