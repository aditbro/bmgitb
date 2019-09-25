'''test subsidi model'''

from django.test import TestCase
from django.forms.models import model_to_dict
from main.models import(
    Subsidi_Kunjungan,
    Subsidi_Obat,
    Subsidi_Tindakan,
    Parameter_Subsidi_Tindakan,
    Parameter_Subsidi_Kunjungan,
    Parameter_Subsidi_Obat
)
from main.tests.factories import(
    ParameterSubsidiKunjunganFactory,
    ParameterSubsidiObatFactory,
    ParameterSubsidiTindakanFactory,
    PasienFactory
)
import pry
import random

class SubsidiTestCase(TestCase):
    def test_substract_when_subsidi_suffice(self):
        parameter_subsidi = ParameterSubsidiObatFactory.create(kategori_pasien='Mahasiswa')
        pasien = PasienFactory.create(kategori='Mahasiswa')
        Subsidi_Obat.create_from_parameter(pasien)

        subsidi = Subsidi_Obat.objects.first()

        subsidi.substract(subsidi.max_subsidi_per_kunjungan)
        
        sisa_subsidi = subsidi.sisa_subsidi_bulan_ini
        expected_sisa = parameter_subsidi.sisa_subsidi_bulan_ini - parameter_subsidi.max_subsidi_per_kunjungan
        self.assertEqual(sisa_subsidi, expected_sisa)

    def test_substract_when_subsidi_not_suffice(self):
        ParameterSubsidiObatFactory.create(kategori_pasien='Mahasiswa')
        pasien = PasienFactory.create(kategori='Mahasiswa')
        Subsidi_Obat.create_from_parameter(pasien)

        subsidi = Subsidi_Obat.objects.first()

        with self.assertRaises(Exception):
            subsidi.substract(subsidi.max_subsidi_per_kunjungan + 1000)

    def test_subsidi_tindakan_creation(self):
        parameter_subsidi_list = ParameterSubsidiTindakanFactory.create_batch(random.randint(1, 10), kategori_pasien='Mahasiswa')
        pasien = PasienFactory.create(kategori='Mahasiswa')
        
        Subsidi_Tindakan.create_from_parameter(pasien)

        for parameter_subsidi in parameter_subsidi_list:
            subsidi = Subsidi_Tindakan.objects.get(
                pasien__no_pasien=pasien.no_pasien,
                tindakan__kode=parameter_subsidi.tindakan.kode
            )
            self.assertEqual(subsidi.sisa_subsidi_bulan_ini, parameter_subsidi.sisa_subsidi_bulan_ini)
            self.assertEqual(subsidi.sisa_subsidi_tahunan, parameter_subsidi.sisa_subsidi_tahunan)
            self.assertEqual(subsidi.max_subsidi_per_kunjungan, parameter_subsidi.max_subsidi_per_kunjungan)

    def test_subsidi_obat_creation(self):
        parameter_subsidi = ParameterSubsidiObatFactory.create(kategori_pasien='Mahasiswa')
        pasien = PasienFactory.create(kategori='Mahasiswa')
        
        Subsidi_Obat.create_from_parameter(pasien)

        subsidi = Subsidi_Obat.objects.get(pasien__no_pasien=pasien.no_pasien)
        self.assertEqual(subsidi.sisa_subsidi_bulan_ini, parameter_subsidi.sisa_subsidi_bulan_ini)
        self.assertEqual(subsidi.sisa_subsidi_tahunan, parameter_subsidi.sisa_subsidi_tahunan)
        self.assertEqual(subsidi.max_subsidi_per_kunjungan, parameter_subsidi.max_subsidi_per_kunjungan)

    def test_subsidi_kunjungan_creation(self):
        parameter_subsidi_list = ParameterSubsidiKunjunganFactory.create_batch(random.randint(1, 10), kategori_pasien='Mahasiswa')
        pasien = PasienFactory.create(kategori='Mahasiswa')
        
        Subsidi_Kunjungan.create_from_parameter(pasien)

        for parameter_subsidi in parameter_subsidi_list:
            subsidi = Subsidi_Kunjungan.objects.get(
                pasien__no_pasien=pasien.no_pasien,
                klinik__kode=parameter_subsidi.klinik.kode
            )
            self.assertEqual(subsidi.sisa_subsidi_bulan_ini, parameter_subsidi.sisa_subsidi_bulan_ini)
            self.assertEqual(subsidi.sisa_subsidi_tahunan, parameter_subsidi.sisa_subsidi_tahunan)
            self.assertEqual(subsidi.max_subsidi_per_kunjungan, parameter_subsidi.max_subsidi_per_kunjungan)

