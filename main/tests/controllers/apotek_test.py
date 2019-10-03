from django.test import TestCase
from django.test import Client as Request
from django.forms.models import model_to_dict
from main.models import(
    PembelianResep,
    PembelianOTC
)
from main.tests.factories import(
    PembelianOTCFactory,
    PembelianResepFactory,
    ObatFactory,
    ClientFactory,
    PasienFactory,
    ParameterSubsidiObatFactory
)
from main.services import GetModelList
import datetime
import json
import pry

class ApotekControllerTestCase(TestCase):
    '''test apotek controller behaviour'''

    def setUp(self):
        self.user = ClientFactory(username='test', password='test',bagian='admin')
        self.auth_headers = { 'HTTP_ACCESS_TOKEN' : self.user.generate_access_token() }

    def test_pembelian_create(self):
        param_subsidi_obat = ParameterSubsidiObatFactory.create(kategori_pasien='Mahasiswa')
        new_pasien = PasienFactory.create(kategori='Mahasiswa')
        new_pembelian = PembelianResepFactory.create(pasien=new_pasien)
        data = new_pembelian.serialize()
        data['pasien'] = data['pasien']['no_pasien']
        data['waktu_pembelian'] = datetime.datetime.now()
        for i in range(len(data['obat'])):
            data['obat'][i]['obat'] = data['obat'][i]['obat']['kode']
            
        response = Request().post(
            '/main/apotek/resep/', data, **self.auth_headers, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        saved_pembelian = PembelianResep.objects.first()
        saved_pembelian = saved_pembelian.serialize()
        saved_pembelian.pop('id')
        saved_pembelian.pop('obat')
        new_pembelian = new_pembelian.serialize()
        new_pembelian.pop('obat')
        new_pembelian.pop('id')
        self.assertEqual(saved_pembelian, new_pembelian)

    def test_pembelian_get(self):
        new_pembelian = PembelianResepFactory.create()
        
        response = Request().get(
            '/main/apotek/resep/{}/'.format(new_pembelian.id), **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)

        fetched_pembelian = json.loads(response.content)['pembelian']
        expected_pembelian = new_pembelian.serialize()
        self.assertEqual(fetched_pembelian, expected_pembelian)

    def test_list_pembelian_without_search_parameter(self):
        PembelianResepFactory.create_batch(20)

        response = Request().get('/main/apotek/resep/', **self.auth_headers)
        self.assertEqual(response.status_code, 200)

        expected_list = GetModelList(PembelianResep).call()
        fetched_list = json.loads(response.content)['pembelian']

        for i in range(len(expected_list)):
            self.assertEqual(fetched_list[i], expected_list[i].serialize())

    def test_list_kunjungan_with_search_parameter(self):
        new_pasien = PasienFactory.create()
        kunjungan_list = PembelianResepFactory.create_batch(15, pasien=new_pasien)
        noise = PembelianResepFactory.create_batch(15)

        response = Request().get('/main/apotek/resep/?pasien__nama={}'.format(new_pasien.nama), **self.auth_headers)
        self.assertEqual(response.status_code, 200)

        search_dict = {'pasien__nama' : new_pasien.nama}
        expected_list = GetModelList(PembelianResep, search_dict=search_dict).call()
        fetched_list = json.loads(response.content)['pembelian']

        for i in range(len(expected_list)):
            self.assertEqual(fetched_list[i], expected_list[i].serialize())
