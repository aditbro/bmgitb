from django.db import models
from .subsidi import Parameter_Subsidi_Kunjungan, Parameter_Subsidi_Obat, Parameter_Subsidi_Tindakan
from .subsidi import Subsidi_Kunjungan, Subsidi_Obat, Subsidi_Tindakan

_short_length = 100
_medium_length = 255
_long_length = 800

class Pasien(models.Model):
    no_pasien = models.CharField(max_length=_short_length, null=True)
    kategori = models.CharField(max_length=_short_length)
    nama = models.CharField(max_length=_medium_length)
    tipe_kartu_identitas = models.CharField(max_length=_short_length)
    nomor_kartu_identitas = models.CharField(max_length=_short_length)
    tempat_lahir = models.CharField(max_length=_medium_length)
    tanggal_lahir = models.DateField('tanggal lahir')
    gender = models.CharField(max_length=_short_length)
    waktu_registrasi = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=_short_length, null=True)
    no_telepon = models.CharField(max_length=_short_length, null=True)
    no_hp = models.CharField(max_length=_short_length, null=True)
    golongan_darah = models.CharField(max_length=_short_length, null=True)
    rhesus = models.CharField(max_length=_short_length, null=True)
    catatan = models.CharField(max_length=_long_length, null=True)
    alamat = models.CharField(max_length=_long_length, null=True)
    kota = models.CharField(max_length=_short_length, null=True)
    subsidi_initiated = False

    def __init__(self, *args, **kwargs):
        required_column = ['kategori', 'nama', 'tipe_kartu_identitas', 'nomor_kartu_identitas', 'tempat_lahir', 'tanggal_lahir', 'gender']
        construction_parameter = {}

        for key,value in kwargs.items() :
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if(not args and kwargs):        
            if required_column :
                raise Exception("missing parameter(s) " + ", ".join(required_column))

        super().__init__(*args, **construction_parameter)

    def save(self):
        super().save()
        if(not self.subsidi_initiated):
            self.init_subsidi()
            self.subsidi_initiated = True

    def init_subsidi(self):
        self.init_subsidi_obat()
        self.init_subsidi_kunjungan()
        self.init_subsidi_tindakan()

    def init_subsidi_obat(self):
        parameter_subsidi = Parameter_Subsidi_Obat.objects.filter(kategori_pasien=self.kategori)
        
        for subsidi in parameter_subsidi :
            new_subsidi = Subsidi_Obat(self, subsidi)
            new_subsidi.save()

    def init_subsidi_tindakan(self):
        parameter_subsidi = Parameter_Subsidi_Tindakan.objects.filter(kategori_pasien=self.kategori)
        
        for subsidi in parameter_subsidi :
            new_subsidi = Subsidi_Tindakan(self, subsidi)
            new_subsidi.save()

    def init_subsidi_kunjungan(self):
        parameter_subsidi = Parameter_Subsidi_Kunjungan.objects.filter(kategori_pasien=self.kategori)
        
        for subsidi in parameter_subsidi :
            new_subsidi = Subsidi_Kunjungan(self, subsidi)
            new_subsidi.save()

    def __str__(self):
        return self.no_pasien

class Mahasiswa(Pasien):
    nim = models.CharField(max_length=_short_length, unique=True)
    strata = models.CharField(max_length=_short_length)
    internasional = models.CharField(max_length=_short_length)
    tpb = models.CharField(max_length=_short_length)
    program_studi = models.CharField(max_length=_short_length)
    fakultas = models.CharField(max_length=_short_length)

    def __init__(self, *args, **kwargs):
        required_column = ['nim']
        construction_parameter = {}

        for key,value in kwargs.items() :
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if(not args and kwargs):
            if required_column :
                raise Exception("missing parameter(s) " + ", ".join(required_column))

        super().__init__(*args, **construction_parameter)

    def __str__(self):
        return self.nim

class Karyawan_BMG(Pasien):
    nip = models.CharField(max_length=_short_length, unique=True)

    def __init__(self, *args, **kwargs):
        required_column = ['nip']
        construction_parameter = {}

        for key,value in kwargs.items():
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if(not args and kwargs):
            if required_column :
                raise Exception("missing parameter(s) " + ", ".join(required_column))

        super().__init__(*args, **construction_parameter)

    def __str__(self):
        return self.nip

class Karyawan_ITB(Pasien):
    nip = models.CharField(max_length=_short_length, unique=True)

    def __init__(self, *args, **kwargs):
        required_column = ['nip']
        construction_parameter = {}

        for key,value in kwargs.items():
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if(not args and kwargs):
            if required_column :
                raise Exception("missing parameter(s) " + ", ".join(required_column))

        super().__init__(*args, **construction_parameter)

    def __str__(self):
        return self.nip

class Keluarga_Karyawan_ITB(Pasien):
    karyawan = models.ForeignKey('Karyawan_ITB', on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):        
        if 'karyawan' in kwargs:
            kwargs['karyawan'] = Karyawan_ITB.objects.get(nip=kwargs['karyawan'])
        elif(args):
            pass
        else :
            raise Exception('missing parameter(s) karyawan')

        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.nip

class Umum(Pasien):
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.nama

class Mitra_Kerja_Sama(Pasien):
    organisasi = models.CharField(max_length=_short_length)

    def __init__(self, *args, **kwargs):        
        required_column = ['organisasi']
        construction_parameter = {}

        for key,value in kwargs.items():
            construction_parameter[key] = value
            if key in required_column :
                required_column.remove(key)

        if required_column :
            raise Exception("missing parameter(s) " + ", ".join(required_column))

        super().__init__(*args, **construction_parameter)

    def __str__(self):
        return self.nama + ', dari ' + self.organisasi