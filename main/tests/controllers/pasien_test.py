'''test pasien controller'''

from django.test import TestCase
from django.test import Client as Request
from django.forms.models import model_to_dict
from main.models import(
    Client,
    Pasien,
    Subsidi_Kunjungan,
    Subsidi_Obat,
    Subsidi_Tindakan
)
from main.tests.factories import(
    PasienFactory,
    ClientFactory,
    MahasiswaFactory
)
from main.services import GetModelList
import json
import pry

class PasienControllerTestCase(TestCase):
    '''test pasien controller behaviour'''

    def setUp(self):
        self.user = ClientFactory(username='test', password='test',bagian='admin')
        self.auth_headers = { 'HTTP_ACCESS_TOKEN' : self.user.generate_access_token() }

    def test_pasien_create(self):
        new_pasien = MahasiswaFactory.build()
        data = model_to_dict(new_pasien)

        response = Request().post(
            '/main/pasien/insert/', data, **self.auth_headers, content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        ''' Test if pasien created '''
        saved_pasien = Pasien.objects.first()
        self.assertEqual(saved_pasien.nama, new_pasien.nama)
        self.assertEqual(
            saved_pasien.nomor_kartu_identitas,
            new_pasien.nomor_kartu_identitas
        )
        self.assertEqual(saved_pasien.kategori, new_pasien.kategori)

    def test_pasien_get(self):
        new_pasien = MahasiswaFactory.create()
        
        response = Request().get(
            '/main/pasien/{}/'.format(new_pasien.no_pasien), **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)

        fetched_pasien = json.loads(response.content)['pasien']
        self.assertEqual(fetched_pasien['no_pasien'], new_pasien.no_pasien)
        self.assertEqual(fetched_pasien['kategori'], new_pasien.kategori)
        self.assertEqual(
            fetched_pasien['nomor_kartu_identitas'],
            new_pasien.nomor_kartu_identitas
        )
        self.assertEqual(fetched_pasien['no_hp'], new_pasien.no_hp)

    def test_list_pasien_without_search_parameter(self):
        pasien_list = MahasiswaFactory.create_batch(20)

        response = Request().get('/main/pasien/', **self.auth_headers)
        self.assertEqual(response.status_code, 200)

        expected_list = GetModelList(Pasien).call()
        fetched_list = json.loads(response.content)['pasien']

        for i in range(len(expected_list)):
            self.assertEqual(fetched_list[i]['id'], expected_list[i].id)
            self.assertEqual(fetched_list[i]['no_pasien'], expected_list[i].no_pasien)
            self.assertEqual(fetched_list[i]['kategori'], expected_list[i].kategori)
            self.assertEqual(fetched_list[i]['nama'], expected_list[i].nama)

    def test_list_pasien_with_search_parameter(self):
        pasien_list = MahasiswaFactory.create_batch(15, golongan_darah='O')
        noise = MahasiswaFactory.create_batch(10, golongan_darah='AB')

        response = Request().get('/main/pasien/?golongan_darah=O', **self.auth_headers)
        self.assertEqual(response.status_code, 200)

        search_dict = {'golongan_darah' : 'O'}
        expected_list = GetModelList(Pasien, search_dict=search_dict).call()
        fetched_list = json.loads(response.content)['pasien']

        for i in range(len(expected_list)):
            self.assertEqual(fetched_list[i]['id'], expected_list[i].id)
            self.assertEqual(fetched_list[i]['no_pasien'], expected_list[i].no_pasien)
            self.assertEqual(fetched_list[i]['kategori'], expected_list[i].kategori)
            self.assertEqual(fetched_list[i]['nama'], expected_list[i].nama)
        


