from django.db import models
from django.forms.models import model_to_dict
from .subsidi import Subsidi_Kunjungan, Subsidi_Obat, Subsidi_Tindakan
from datetime import datetime
from faker import Faker
import pry

_short_length = 100
_medium_length = 255
_long_length = 800

class Pasien(models.Model):
    KATEGORI_CHOICES = [
        ('Mahasiswa', 'Mahasiswa'),
        ('Karyawan BMG', 'Karyawan BMG'),
        ('Karyawan ITB', 'Karyawan ITB'),
        ('Keluarga Karyawan ITB', 'Keluarga Karyawan ITB'),
        ('Umum', 'Umum'),
        ('Mitra Kerja Sama', 'Mitra Kerja Sama')
    ]
    no_pasien = models.CharField(max_length=_short_length, null=True, blank=True)
    kategori = models.CharField(max_length=_short_length, choices=KATEGORI_CHOICES)
    nama = models.CharField(max_length=_medium_length)
    tipe_kartu_identitas = models.CharField(max_length=_short_length)
    nomor_kartu_identitas = models.CharField(max_length=_short_length)
    tempat_lahir = models.CharField(max_length=_medium_length)
    tanggal_lahir = models.DateField('tanggal lahir')
    gender = models.CharField(max_length=_short_length)
    waktu_registrasi = models.DateTimeField(auto_now_add=True, blank=True)
    email = models.CharField(max_length=_short_length, null=True, blank=True)
    no_telepon = models.CharField(max_length=_short_length, null=True, blank=True)
    no_hp = models.CharField(max_length=_short_length, null=True, blank=True)
    golongan_darah = models.CharField(max_length=_short_length, null=True, blank=True)
    rhesus = models.CharField(max_length=_short_length, null=True, blank=True)
    catatan = models.CharField(max_length=_long_length, null=True, blank=True)
    alamat = models.CharField(max_length=_long_length, null=True, blank=True)
    kota = models.CharField(max_length=_short_length, null=True, blank=True)

    @classmethod
    def new_id(cls):
        return 'P-' + Faker().uuid4(cast_to=str)[:8]

    def __str__(self):
        return self.nama

    def serialize(self):
        pasien = model_to_dict(self)
        pasien['no_pasien'] = self.no_pasien
        pasien['tanggal_lahir'] = str(self.tanggal_lahir)
        pasien['waktu_registrasi'] = str(self.waktu_registrasi.strftime("%d %b %Y %H:%M"))

        return pasien

    def serialize_subsidi(self):
        subsidi = {}
        subsidi['obat'] = [x.serialize() for x in self.subsidi_obat_set.all()]
        subsidi['tindakan'] = [x.serialize() for x in self.subsidi_tindakan_set.all()]
        subsidi['kunjungan'] = [x.serialize() for x in self.subsidi_tindakan_set.all()]

        return subsidi

    def init_subsidi(self):
        Subsidi_Kunjungan.create_from_parameter(self)
        Subsidi_Obat.create_from_parameter(self)
        Subsidi_Tindakan.create_from_parameter(self)
    
    def get_child_data(self):
        if(self.kategori == 'Umum'):
            return self
        return getattr(self, self.kategori.lower().replace(' ', '_'))

    @classmethod
    def get_kategori_choices(cls):
        return [
            'Mahasiswa',
            'Karyawan BMG',
            'Karyawan ITB',
            'Keluarga Karyawan ITB',
            'Umum',
            'Mitra Kerja Sama'
        ]

class Mahasiswa(Pasien):
    STRATA_CHOICES = [
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3')
    ]
    nim = models.CharField(max_length=_short_length, unique=True)
    strata = models.CharField(max_length=_short_length)
    internasional = models.BooleanField(max_length=_short_length)
    tpb = models.BooleanField(max_length=_short_length)
    program_studi = models.CharField(max_length=_short_length)
    fakultas = models.CharField(max_length=_short_length)

class Karyawan_BMG(Pasien):
    nip = models.CharField(max_length=_short_length, unique=True)

class Karyawan_ITB(Pasien):
    nip = models.CharField(max_length=_short_length, unique=True)

class Keluarga_Karyawan_ITB(Pasien):
    karyawan = models.ForeignKey('Karyawan_ITB', on_delete=models.CASCADE)

    def serialize(self):
        pasien = super().serialize()
        pasien['nip'] = self.karyawan.nip

        return pasien

class Umum(Pasien):
    pass

class Mitra_Kerja_Sama(Pasien):
    organisasi = models.CharField(max_length=_short_length)

    def __str__(self):
        return self.nama + ', dari ' + self.organisasi