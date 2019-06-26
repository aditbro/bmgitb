'''generate random user data'''

from main.models import (
    Pasien,
    Mahasiswa,
    Umum,
    Keluarga_Karyawan_ITB,
    Karyawan_BMG,
    Karyawan_ITB,
    Mitra_Kerja_Sama
)

from faker import Faker
from random import choice
from datetime import datetime, date
from factory.django import DjangoModelFactory

class PasienFactory(DjangoModelFactory):
    '''Generate random pasien data'''
    class Meta:
        model = Pasien

    no_pasien = Pasien.new_id()
    kategori = choice(['Umum', 'Mahasiswa', 'Karyawan BMG', 'Mitra Kerja Sama'])
    nama = Faker().name()
    tipe_kartu_identitas = choice(['KTP', 'KTM', 'SIM'])
    nomor_kartu_identitas = Faker().pystr()
    tempat_lahir = Faker().pystr()
    tanggal_lahir = Faker().date_object(end_datetime=date.today())
    gender = choice(['laki-laki', 'perempuan'])
    waktu_registrasi = datetime.now()
    email = Faker().email()
    no_telepon = Faker().msisdn()
    no_hp = Faker().msisdn()
    golongan_darah = choice(['A','B','AB','O'])
    rhesus = choice(['+','-'])
    catatan = Faker().paragraph()
    alamat = Faker().address()
    kota = Faker().city()