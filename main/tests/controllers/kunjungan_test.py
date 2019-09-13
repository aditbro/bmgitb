'''test kunjungan controller'''

from django.test import TestCase
from django.test import Client as Request
from django.forms.models import model_to_dict
from main.models import(
    Kunjungan,
    Client
)
from main.tests.factories import(
    KunjunganFactory,
    DokterFactory,
    ClientFactory,
    MahasiswaFactory
)
from main.services import GetModelList
import json
import pry

class KunjunganControllerTestCase(TestCase):
    '''test kunjungan controller behaviour'''

    def setUp(self):
        self.user = ClientFactory(username='test', password='test',bagian='admin')
        self.auth_headers = { 'HTTP_ACCESS_TOKEN' : self.user.generate_access_token() }

    def test_kunjungan_create(self):
        new_pasien = MahasiswaFactory.create()
        new_dokter = DokterFactory.create()
        new_kunjungan = KunjunganFactory.build(pasien=new_pasien, dokter=new_dokter)
        data = new_kunjungan.serialize()
        data['pasien'] = data['pasien']['no_pasien']
        data['klinik'] = data['klinik']['kode']
        data['dokter'] = data['dokter']['kode']

        response = Request().post(
            '/main/klinik/kunjungan/', data, **self.auth_headers, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        ''' Test if pasien created '''
        saved_kunjungan = Kunjungan.objects.first()
        self.assertEqual(saved_kunjungan.pasien.no_pasien, new_kunjungan.pasien.no_pasien)

    def test_kunjungan_get(self):
        new_kunjungan = KunjunganFactory.create()
        
        response = Request().get(
            '/main/klinik/kunjungan/{}/'.format(new_kunjungan.kode), **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)

        fetched_kunjungan = json.loads(response.content)['kunjungan']
        expected_kunjungan = new_kunjungan.serialize()
        self.assertEqual(fetched_kunjungan['id'], expected_kunjungan['id'])

    def test_list_kunjungan_without_search_parameter(self):
        KunjunganFactory.create_batch(20)

        response = Request().get('/main/klinik/kunjungan/', **self.auth_headers)
        self.assertEqual(response.status_code, 200)

        expected_list = GetModelList(Kunjungan).call()
        fetched_list = json.loads(response.content)['kunjungan']

        for i in range(len(expected_list)):
            self.assertEqual(fetched_list[i], expected_list[i].serialize())

    def test_list_kunjungan_with_search_parameter(self):
        new_pasien = MahasiswaFactory.create()
        kunjungan_list = KunjunganFactory.create_batch(15, pasien=new_pasien)
        noise = KunjunganFactory.create_batch(15)

        response = Request().get('/main/klinik/kunjungan/?pasien__nama={}'.format(new_pasien.nama), **self.auth_headers)
        self.assertEqual(response.status_code, 200)

        search_dict = {'pasien__nama' : new_pasien.nama}
        expected_list = GetModelList(Kunjungan, search_dict=search_dict).call()
        fetched_list = json.loads(response.content)['kunjungan']

        for i in range(len(expected_list)):
            self.assertEqual(fetched_list[i], expected_list[i].serialize())