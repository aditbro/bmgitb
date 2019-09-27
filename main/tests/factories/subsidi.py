'''generate random parameter subsidi data'''

from .klinik import TindakanFactory, KlinikFactory
from main.models import (
    Pasien,
    Tindakan,
    Klinik,
    Parameter_Subsidi_Tindakan,
    Parameter_Subsidi_Obat,
    Parameter_Subsidi_Kunjungan
)

from faker import Factory
from random import choice
from datetime import datetime, date
import factory
import random

faker = Factory.create()
func = factory.LazyFunction
fatr = factory.LazyAttribute

class ParameterSubsidiTindakanFactory(factory.django.DjangoModelFactory):
    '''generate random parameter subsidi tindakan'''

    class Meta:
        model = Parameter_Subsidi_Tindakan

    kategori_pasien = fatr(lambda obj: choice(Pasien.get_kategori_choices()))
    kode = func(faker.itin)
    keterangan = func(faker.pystr)
    tindakan = factory.SubFactory(TindakanFactory)
    max_subsidi_per_kunjungan = fatr(lambda obj: random.randint(1000, 100000))
    sisa_subsidi_bulan_ini = fatr(lambda obj: random.randint(obj.max_subsidi_per_kunjungan, 3 * obj.max_subsidi_per_kunjungan))
    sisa_subsidi_tahunan = fatr(lambda obj: random.randint(obj.sisa_subsidi_bulan_ini, 4 * obj.sisa_subsidi_bulan_ini))

class ParameterSubsidiObatFactory(factory.django.DjangoModelFactory):
    '''generate random parameter subsidi obat'''

    class Meta:
        model = Parameter_Subsidi_Obat

    kategori_pasien = fatr(lambda obj: choice(Pasien.KATEGORI_CHOICES))
    kode = func(faker.itin)
    keterangan = func(faker.pystr)
    max_subsidi_per_kunjungan = fatr(lambda obj: random.randint(1000, 100000))
    sisa_subsidi_bulan_ini = fatr(lambda obj: random.randint(obj.max_subsidi_per_kunjungan, 3 * obj.max_subsidi_per_kunjungan))
    sisa_subsidi_tahunan = fatr(lambda obj: random.randint(obj.sisa_subsidi_bulan_ini, 4 * obj.sisa_subsidi_bulan_ini))

class ParameterSubsidiKunjunganFactory(factory.django.DjangoModelFactory):
    '''generate random parameter subsidi obat'''

    class Meta:
        model = Parameter_Subsidi_Kunjungan

    kategori_pasien = fatr(lambda obj: choice(Pasien.KATEGORI_CHOICES))
    kode = func(faker.itin)
    klinik = factory.SubFactory(KlinikFactory)
    keterangan = func(faker.pystr)
    max_subsidi_per_kunjungan = fatr(lambda obj: random.randint(1000, 100000))
    sisa_subsidi_bulan_ini = fatr(lambda obj: random.randint(obj.max_subsidi_per_kunjungan, 3 * obj.max_subsidi_per_kunjungan))
    sisa_subsidi_tahunan = fatr(lambda obj: random.randint(obj.sisa_subsidi_bulan_ini, 4 * obj.sisa_subsidi_bulan_ini))