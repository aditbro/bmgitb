from django.test import TestCase
from main.models import Klinik, Dokter, Client
   
class KlinikTestCase(TestCase):
    kliniks = [
        {
            'kode' : 'KGi',
            'nama' : 'Klinik Gigi',
            'tarif_kunjungan' : 20000,
            'is_subsidi' : 'False',
            'is_cash' : 'False' 
        },
        {
            'kode' : 'KMa',
            'nama' : 'Klinik Uata',
            'tarif_kunjungan' : 30000,
            'is_subsidi' : 'False',
            'is_cash' : 'False' 
        },
        {
            'kode' : 'KU',
            'nama' : 'Klinik Umum',
            'tarif_kunjungan' : 15000,
            'is_subsidi' : 'False',
            'is_cash' : 'False' 
        },
    ]

    dokters = [
        {
            'kode' : 'DGi-01',
            'nama' : 'Bambang Miharjo',
            'klinik' : 'KGi'
        },
        {
            'kode' : 'DGi-02',
            'nama' : 'Entis Sutisna',
            'klinik' : 'KGi'
        },
        {
            'kode' : 'DMa-01',
            'nama' : 'Retno Marsudi',
            'klinik' : 'KMa'
        },
        {
            'kode' : 'DMa-02',
            'nama' : 'Eric Tohir',
            'klinik' : 'KMa'
        },
        {
            'kode' : 'DU-01',
            'nama' : 'Djoko Susilo',
            'klinik' : 'KU'
        },
        {
            'kode' : 'DU-02',
            'nama' : 'Susi Pudjianto',
            'klinik' : 'KU'
        }
    ]

    def setUp(self):
        for klinik in self.kliniks:
            new_klinik = Klinik(**klinik)
            new_klinik.save()

        for dokter in self.dokters:
            dokter['klinik'] = Klinik.objects.get(kode=dokter['klinik'])
            new_dokter = Dokter(**dokter)
            new_dokter.save()        