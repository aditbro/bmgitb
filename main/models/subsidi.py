from django.db import models
from django.forms.models import model_to_dict
from .klinik import Klinik, Tindakan

_short_length = 100
_medium_length = 255
_long_length = 800

class Subsidi_Tindakan(models.Model):
    kode = models.CharField(max_length=_short_length, null=True)
    keterangan = models.CharField(max_length=_long_length)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()    
    sisa_subsidi_tahunan = models.IntegerField()

    def __init__(self, pasien, parameter_subsidi) :
        constructor_parameter = {}
        parameter_subsidi = model_to_dict(parameter_subsidi)
        required_column = ['kode', 'keterangan', 'tindakan', 'max_subsidi_per_kunjungan', 'sisa_subsidi_bulan_ini', 'sisa_subsidi_tahunan']
        constructor_parameter['pasien'] = pasien

        for col in required_column :
            constructor_parameter[col] = parameter_subsidi[col]
        
        super().__init__(**constructor_parameter)

class Subsidi_Obat(models.Model):
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    max_subsidi_per_pembelian = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

    def __init__(self, pasien, parameter_subsidi) :
        constructor_parameter = {}
        parameter_subsidi = model_to_dict(parameter_subsidi)
        required_column = ['kode', 'keterangan', 'max_subsidi_per_kunjungan', 'sisa_subsidi_bulan_ini', 'sisa_subsidi_tahunan']
        constructor_parameter['pasien'] = pasien

        for col in required_column :
            constructor_parameter[col] = parameter_subsidi[col]
        
        super().__init__(**constructor_parameter)

class Subsidi_Kunjungan(models.Model):
    pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=_long_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

    def __init__(self, pasien, parameter_subsidi) :
        constructor_parameter = {}
        parameter_subsidi = model_to_dict(parameter_subsidi)
        required_column = ['keterangan', 'max_subsidi_per_kunjungan', 'sisa_subsidi_bulan_ini', 'sisa_subsidi_tahunan']
        constructor_parameter['pasien'] = pasien
        constructor_parameter['klinik'] = Klinik.objects.get(id=parameter_subsidi['klinik'])

        for col in required_column :
            constructor_parameter[col] = parameter_subsidi[col]
        
        super().__init__(**constructor_parameter)

class Parameter_Subsidi_Tindakan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length, null=True)
    tindakan = models.ForeignKey('Tindakan', on_delete=models.CASCADE)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()    
    sisa_subsidi_tahunan = models.IntegerField()

class Parameter_Subsidi_Obat(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    max_subsidi_per_pembelian = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()

class Parameter_Subsidi_Kunjungan(models.Model):
    kategori_pasien = models.CharField(max_length=_short_length)
    klinik = models.ForeignKey('Klinik', on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=_long_length)
    max_subsidi_per_kunjungan = models.IntegerField()
    sisa_subsidi_bulan_ini = models.IntegerField()
    sisa_subsidi_tahunan = models.IntegerField()