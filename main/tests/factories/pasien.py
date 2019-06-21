'''generate random user data'''

from main.helper.randomizer import (
    random_string,
    random_int,
    random_bool
)

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

def generate_pasiens(amount, kategori='Pasien'):
    '''Generate random pasien data'''
    fake = Faker()
    pasiens = []
    for _ in range(amount):
        pasiens.append(
            Pasien(
                no_pasien = Pasien.new_id,
                kategori = kategori,
                nama = fake.name(),
                tipe_kartu_identitas = choice(['KTP', 'KTM', 'SIM']),
                nomor_kartu_identitas = fake.pystr,
                tempat_lahir = fake.pystr,
                tanggal_lahir = fake.date_object(end_datetime=date.today()),
                gender = choice(['laki-laki', 'perempuan']),
                waktu_registrasi = datetime.now(),
                email = fake.email(),
                no_telepon = fake.msisdn(),
                no_hp = fake.msisdn(),
                golongan_darah = choice(['A','B','AB','O']),
                rhesus = choice(['+','-']),
                catatan = fake.paragraph(),
                alamat = fake.address(),
                kota = fake.city(),
            ).save()
        )
    return pasiens