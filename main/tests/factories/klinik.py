'''generate random kunjungan data'''

from main.models import (
    Klinik,
    Dokter,
    Diagnosis,
    Tindakan
)

from faker import Factory
from random import choice
from datetime import datetime, date
import factory
import random

faker = Factory.create()
func = factory.LazyFunction
fatr = factory.LazyAttribute

class KlinikFactory(factory.django.DjangoModelFactory):
    '''Generate random kunjungan data'''
    class Meta:
        model = Klinik

    kode = func(faker.itin)
    nama = func(faker.itin)
    tarif_kunjungan = fatr(lambda obj: random.randint(1000, 100000))
    is_subsidi = fatr(lambda obj: choice([True, False]))
    is_cash = fatr(lambda obj: choice([True, False]))

class DokterFactory(factory.django.DjangoModelFactory):
    '''Generate random dokter data'''
    class Meta:
        model = Dokter

    kode = func(faker.itin)
    nama = func(faker.name)
    klinik = factory.SubFactory(KlinikFactory)

class TindakanFactory(factory.django.DjangoModelFactory):
    '''Generate random tindakan data'''
    
    class Meta:
        model = Tindakan

    nama = func(faker.pystr)
    kode = func(faker.itin)
    keterangan = func(faker.pystr)
    tarif = fatr(lambda obj: random.randint(10000, 100000))
    is_subsidi = fatr(lambda obj: choice([True, False]))
    