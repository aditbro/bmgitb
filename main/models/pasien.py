from django.db import models

_short_length = 100
_medium_length = 255
_long_length = 800

class Pasien(models.Model):
    no_pasien = models.CharField(max_length=_short_length, null=True)
    nama = models.CharField(max_length=_medium_length)
    catatan = models.CharField(max_length=_long_length, null=True)
    tipe_kartu_identitas = models.CharField(max_length=_short_length)
    nomor_kartu_identitas = models.CharField(max_length=_short_length)
    tempat_lahir = models.CharField(max_length=_medium_length)
    tanggal_lahir = models.DateField('tanggal lahir')
    alamat = models.CharField(max_length=_long_length)
    kota = models.CharField(max_length=_short_length)
    active = models.CharField(max_length=_short_length, default='active')
    gender = models.CharField(max_length=_short_length)
    email = models.CharField(max_length=_short_length, null=True)
    no_telepon = models.CharField(max_length=_short_length, null=True)
    no_hp = models.CharField(max_length=_short_length, null=True)
    berat_badan = models.IntegerField('berat badan', null=True)
    tinggi_badan = models.IntegerField('tinggi badan', null=True)
    organisasi = models.CharField(max_length=_short_length, null=True)
    kategori = models.ForeignKey('Kategori_Pasien', on_delete=models.CASCADE)
    golongan_darah = models.CharField(max_length=_short_length, null=True)
    rhesus = models.CharField(max_length=_short_length, null=True)

    def __str__(self):
        return self.no_pasien

class Mahasiswa(models.Model):
    no_pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    nim = models.CharField(max_length=_short_length, unique=True)
    strata = models.CharField(max_length=_short_length)
    internasional = models.CharField(max_length=_short_length)
    tpb = models.CharField(max_length=_short_length)
    program_studi = models.CharField(max_length=_short_length)
    fakultas = models.CharField(max_length=_short_length)

    def __str__(self):
        return self.nim

class Pegawai(models.Model):
    no_pasien = models.OneToOneField('Pasien', on_delete=models.CASCADE)
    nip = models.CharField(max_length=_short_length, unique=True)

    def __str__(self):
        return self.nip

class Kategori_Pasien(models.Model):
    nama = models.CharField(max_length=_short_length)
    kode = models.CharField(max_length=_short_length, primary_key=True)

    def __str__(self):
        return self.nama