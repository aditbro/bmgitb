'''generate random kunjungan data'''

from main.models import (
    Kunjungan
)
from .pasien import PasienFactory
from .klinik import KlinikFactory, DokterFactory

from faker import Factory
from random import choice
from datetime import datetime, date
import factory
import random

faker = Factory.create()
func = factory.LazyFunction
fatr = factory.LazyAttribute

class KunjunganFactory(factory.django.DjangoModelFactory):
    '''Generate random kunjungan data'''
    class Meta:
        model = Kunjungan

    kode = func(Kunjungan.new_id)
    pasien = factory.SubFactory(PasienFactory)
    dokter = factory.SubFactory(DokterFactory)
    klinik = fatr(lambda obj: obj.dokter.klinik)
    tarif = fatr(lambda obj: random.randint(1000, 100000))
    klaim = 0
    cash = fatr(lambda obj: obj.tarif)
    koreksi = None
    asal = func(faker.address)
    is_valid = True
    waktu_kunjungan = datetime.now()
