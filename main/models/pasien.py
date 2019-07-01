from django.db import models
from django.forms.models import model_to_dict
from .subsidi import Subsidi_Kunjungan, Subsidi_Obat, Subsidi_Tindakan
from datetime import datetime
from faker import Faker

_short_length = 100
_medium_length = 255
_long_length = 800

class Pasien(models.Model):
    no_pasien = models.CharField(max_length=_short_length, null=True, blank=True)
    kategori = models.CharField(max_length=_short_length)
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
        pasien['tanggal_lahir'] = str(self.tanggal_lahir)

        return pasien

class Mahasiswa(Pasien):
    nim = models.CharField(max_length=_short_length, unique=True)
    strata = models.CharField(max_length=_short_length)
    internasional = models.CharField(max_length=_short_length)
    tpb = models.CharField(max_length=_short_length)
    program_studi = models.CharField(max_length=_short_length)
    fakultas = models.CharField(max_length=_short_length)

class Karyawan_BMG(Pasien):
    nip = models.CharField(max_length=_short_length, unique=True)

class Karyawan_ITB(Pasien):
    nip = models.CharField(max_length=_short_length, unique=True)

class Keluarga_Karyawan_ITB(Pasien):
    karyawan = models.ForeignKey('Karyawan_ITB', on_delete=models.CASCADE)

class Umum(Pasien):
    pass

class Mitra_Kerja_Sama(Pasien):
    organisasi = models.CharField(max_length=_short_length)

    def __str__(self):
        return self.nama + ', dari ' + self.organisasi