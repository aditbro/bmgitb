'''Generate random klinik related data'''
from .randomizer import (
    random_string,
    random_int,
    random_bool
)

def generate_klinik(amount):
    '''Generate random klinik dict data'''
    kliniks = []
    for _ in range(amount):
        kliniks.append({
            'kode' : random_string(10),
            'nama' : random_string(10),
            'tarif_kunjungan' : random_int(0, 1000000),
            'is_subsidi' : str(random_bool()),
        })

        if kliniks[-1]['is_subsidi'] == 'True':
            kliniks[-1]['is_cash'] = 'False'
        else:
            kliniks[-1]['is_cash'] = 'True'

    return kliniks

def generate_dokter(amount):
    '''Generate random dokter dict data'''
    kliniks = generate_klinik(amount)
    dokters = []

    for _ in range(amount):
        dokters.append({
            'kode' : random_string(10),
            'nama' : random_string(10),
            'klinik' : kliniks[random_int(0, amount)]['kode']
        })

    return kliniks, dokters

def generate_diagnosis(amount):
    '''Generate random diagnosis data'''
    diagnosis_list = []

    for _ in range(amount):
        diagnosis_list.append({
            'nama' : random_string(10),
            'kode' : random_string(10),
            'keterangan' : random_string(20)
        })

    return diagnosis_list

def generate_tindakan(amount):
    '''Generate random tindakan'''
    tindakans = []

    for _ in range(amount):
        tindakans.append({
            'kode' : random_string(10),
            'nama' : random_string(10),
            'keterangan' : random_string(20),
            'tarif' : random_int(10_000, 20_000),
            'is_subsidi' : random_bool()
        })

        if tindakans[-1]['is_subsidi'] == 'True':
            tindakans[-1]['is_cash'] = 'False'
        else:
            tindakans[-1]['is_cash'] = 'True'

    return tindakans