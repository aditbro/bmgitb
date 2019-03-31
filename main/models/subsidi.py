from django.db import models
from django.forms.models import model_to_dict
from .klinik import Klinik, Tindakan

_short_length = 100
_medium_length = 255
_long_length = 800

class Subsidi_Tindakan(models.Model):
    kode = models.CharField(max_length=_short_length, null=True, blank=True)
    keterangan = models.CharField(max_length=_long_length)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField(null=True, blank=True)
    sisa_subsidi_bulan_ini = models.IntegerField(null=True, blank=True)    
    sisa_subsidi_tahunan = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_pasien_subsidi_from_parameter(cls, pasien):
        kategori = pasien.kategori
        list_parameter = Parameter_Subsidi_Tindakan.objects.filter(kategori_pasien=kategori)
        construction_parameter = {}
        subsidi_column = ['keterangan', 'tindakan', 'max_subsidi_per_kunjungan', 'sisa_subsidi_bulan_ini', 'sisa_subsidi_tahunan']

        for parameter in list_parameter :
            parameter_subsidi = model_to_dict(parameter)
            for key in subsidi_column :
                construction_parameter[key] = parameter_subsidi[key]
            
            construction_parameter['pasien'] = pasien
            construction_parameter['tindakan'] = parameter.tindakan

            subsidi = cls(**construction_parameter)
            subsidi.save()
            subsidi.kode = 'STi-' + str(subsidi.id)
            subsidi.save()

class Subsidi_Obat(models.Model):
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_pembelian = models.IntegerField(null=True, blank=True)
    sisa_subsidi_bulan_ini = models.IntegerField(null=True, blank=True)    
    sisa_subsidi_tahunan = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_pasien_subsidi_from_parameter(cls, pasien):
        kategori = pasien.kategori
        list_parameter = Parameter_Subsidi_Obat.objects.filter(kategori_pasien=kategori)
        construction_parameter = {}
        subsidi_column = ['keterangan', 'max_subsidi_per_pembelian', 'sisa_subsidi_bulan_ini', 'sisa_subsidi_tahunan']

        for parameter in list_parameter :
            parameter_subsidi = model_to_dict(parameter)
            for key in subsidi_column :
                construction_parameter[key] = parameter_subsidi[key]
            
            construction_parameter['pasien'] = pasien

            subsidi = cls(**construction_parameter)
            subsidi.save()
            subsidi.kode = 'SO-' + str(subsidi.id)
            subsidi.save()

class Subsidi_Kunjungan(models.Model):
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=_long_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField(null=True, blank=True)
    sisa_subsidi_bulan_ini = models.IntegerField(null=True, blank=True)    
    sisa_subsidi_tahunan = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_pasien_subsidi_from_parameter(cls, pasien):
        kategori = pasien.kategori
        list_parameter = Parameter_Subsidi_Kunjungan.objects.filter(kategori_pasien=kategori)
        construction_parameter = {}
        subsidi_column = ['keterangan', 'klinik', 'max_subsidi_per_kunjungan', 'sisa_subsidi_bulan_ini', 'sisa_subsidi_tahunan']

        for parameter in list_parameter :
            parameter_subsidi = model_to_dict(parameter)
            for key in subsidi_column :
                construction_parameter[key] = parameter_subsidi[key]
            
            construction_parameter['pasien'] = pasien
            construction_parameter['klinik'] = parameter.klinik

            subsidi = cls(**construction_parameter)
            subsidi.save()
            subsidi.kode = 'SK-' + str(subsidi.id)
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

class Parameter_Subsidi_Obat(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    max_subsidi_per_pembelian = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

    def __str__(self):
        return 'subsidi pembelian obat untuk ' + self.kategori_pasien

class Parameter_Subsidi_Kunjungan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=_long_length)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

    def __str__(self):
        return 'subsidi kunjungan ' + self.klinik.nama + ' untuk ' + self.kategori_pasien