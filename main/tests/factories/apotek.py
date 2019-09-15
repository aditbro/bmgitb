'''generate random apotek data'''

from main.models import (
    PembelianObatResep,
    PembelianObatOTC,
    PembelianOTC,
    PembelianResep,
    Obat
)

from faker import Factory
from random import choice
from datetime import datetime, date
import factory
import random

faker = Factory.create()
func = factory.LazyFunction
fatr = factory.LazyAttribute

class ObatFac

class PembelianObatResepFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian obat data'''
    class Meta:
        model = PembelianObatResep

    jumlah = fatr(lambda obj: random.randint(1, 4))
    obat = factory.SubFactory(ObatFactory)
    tarif = fatr(lambda obj: obj.obat.)

class PembelianResepFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian resep data'''
    class Meta:
        model = PembelianResep

    obat = fatr(lambda obj: PembelianObatFactory.create_batch(random.randint(1, 5)))
    tarif = fatr(lambda obj: sum([x.tarif for x in obj.obat]))
    subsidi = fatr(lambda obj: obj.tarif - random.randint(0, obj.tarif))
    bayar = fatr(lambda obj: obj.tarif)
    waktu_pembelian = datetime.now()

class PembelianOTCFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian OTC data'''
    class Meta:
        model = PembelianOTC

    tarif = fatr(lambda obj: random.randint(1000, 100000))
    bayar = fatr(lambda obj: obj.tarif)
    obat = fatr(lambda obj: PembelianObatFactory.create_batch(random.randint(1, 5)))
    waktu_pembelian = datetime.now()    

    