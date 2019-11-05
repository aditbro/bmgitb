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

from faker import Factory
from random import choice
from datetime import datetime, date
import factory

faker = Factory.create()
func = factory.LazyFunction
fatr = factory.LazyAttribute

class PasienFactory(factory.django.DjangoModelFactory):
    '''Generate random pasien data'''
    class Meta:
        model = Pasien

    no_pasien = func(Pasien.new_id)
    nama = func(faker.name)
    tipe_kartu_identitas = fatr(lambda obj: choice(['KTP', 'KTM', 'SIM']))
    nomor_kartu_identitas = func(faker.pystr)
    tempat_lahir = func(faker.pystr)
    tanggal_lahir = fatr(lambda obj: faker.date_object(end_datetime=date.today()))
    gender = fatr(lambda obj: choice(['laki-laki', 'perempuan']))
    waktu_registrasi = func(datetime.now)
    email = func(faker.email)
    no_telepon = func(faker.msisdn)
    no_hp = func(faker.msisdn)
    golongan_darah = fatr(lambda obj: choice(['A','B','AB','O']))
    rhesus = fatr(lambda obj: choice(['+','-']))
    catatan = func(faker.paragraph)
    alamat = func(faker.address)
    kota = func(faker.city)
    kategori = 'Umum'

    @factory.post_generation
    def generate(self, create, extracted, **kwargs):
        if create:
            self.init_subsidi()

class MahasiswaFactory(PasienFactory):
    '''Generate random mahasiswa data'''
    class Meta:
        model = Mahasiswa

    kategori = 'Mahasiswa'
    nim = func(faker.itin)
    strata = fatr(lambda obj: choice(['S1', 'S2', 'S3']))
    internasional = fatr(lambda obj: choice([True, False]))
    tpb = fatr(lambda obj: choice([True, False]))
    program_studi = func(faker.word)
    fakultas = func(faker.word)

class KaryawanBMGFactory(PasienFactory):
    '''Generate random karyawan bmg data'''
    class Meta:
        model = Karyawan_BMG

    kategori = 'Karyawan BMG'
    nip = func(faker.itin)

class KaryawanITBFactory(PasienFactory):
    '''Generate random karyawan itb data'''
    class Meta:
        model = Karyawan_ITB

    kategori = 'Karyawan ITB'
    nip = func(faker.itin)

class KeluargaKaryawanITBFactory(PasienFactory):
    '''Generate random keluarga karyawan'''
    class Meta:
        model = Keluarga_Karyawan_ITB

    kategori = 'Keluarga Karyawan ITB'
    karyawan = factory.SubFactory(KaryawanITBFactory)

class UmumFactory(PasienFactory):
    '''Generate random keluarga karyawan'''
    class Meta:
        model = Umum

    kategori = 'Umum'

class MitraKerjaSamaFactory(PasienFactory):
    '''Generate random keluarga karyawan'''
    class Meta:
        model = Mitra_Kerja_Sama

    organisasi = func(faker.name)
    kategori = 'Mitra Kerja Sama'
    