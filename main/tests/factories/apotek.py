'''generate random apotek data'''

from main.models import (
    PembelianObatResep,
    PembelianObatOTC,
    PembelianOTC,
    PembelianResep,
    Obat
)
from .pasien import PasienFactory
from faker import Factory
from random import choice
from datetime import datetime, date
import factory
import random

faker = Factory.create()
func = factory.LazyFunction
fatr = factory.LazyAttribute

class ObatFactory(factory.django.DjangoModelFactory):
    '''Generate random obat data'''
    class Meta:
        model = Obat

    kode = func(faker.itin)
    nama = func(faker.itin)
    jumlah_stok = fatr(lambda obj: random.randint(10, 1000))
    satuan = func(faker.currency_code)
    keterangan = func(faker.pystr)
    harga_otc = fatr(lambda obj: random.randint(1000, 100000))
    harga_resep = fatr(lambda obj: random.randint(1000, 100000))

class PembelianObatResepFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian obat data'''
    class Meta:
        model = PembelianObatResep

    jumlah = fatr(lambda obj: random.randint(1, 4))
    obat = factory.SubFactory(ObatFactory)
    tarif = fatr(lambda obj: obj.obat.harga_resep * obj.jumlah)

class PembelianObatOTCFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian obat data'''
    class Meta:
        model = PembelianObatOTC

    jumlah = fatr(lambda obj: random.randint(1, 4))
    obat = factory.SubFactory(ObatFactory)
    tarif = fatr(lambda obj: obj.obat.harga_otc * obj.jumlah)

class PembelianResepFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian resep data'''
    class Meta:
        model = PembelianResep

    tarif = 0
    subsidi = 0
    bayar = 0
    pasien = factory.SubFactory(PasienFactory)
    waktu_pembelian = datetime.now()

    @factory.post_generation
    def generate(self, create, extracted, **kwargs):
        obat = PembelianObatResepFactory.create_batch(random.randint(1, 5))
        self.tarif = sum([x.tarif for x in obat])
        self.subsidi = self.tarif - random.randint(0, self.tarif)
        self.bayar = self.tarif - self.subsidi
        for o in obat:
            self.obat.add(o)

class PembelianOTCFactory(factory.django.DjangoModelFactory):
    '''Generate random pembelian OTC data'''
    class Meta:
        model = PembelianOTC

    tarif = 0
    bayar = 0
    waktu_pembelian = datetime.now()   

    @factory.post_generation
    def generate(self, create, extracted, **kwargs):
        obat = PembelianObatOTCFactory.create_batch(random.randint(1, 5))
        self.tarif = sum([x.tarif for x in obat])
        self.bayar = self.tarif
        for o in obat:
            self.obat.add(o)