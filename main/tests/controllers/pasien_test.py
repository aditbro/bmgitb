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
from main.tests.factories import ClientFactory, PasienFactory

class PasienControllerTestCase(TestCase):
    '''test pasien controller behaviour'''

    def setUp(self):
        self.user = ClientFactory(username='test', password='test',bagian='admin')

    def test_pasien_create(self):
        new_pasien = PasienFactory.build()
        data = model_to_dict(new_pasien)
        headers = { 'HTTP_ACCESS_TOKEN' : self.user.generate_access_token() }

        response = Request().post(
            '/main/pasien/insert/', data, **headers, content_type='application/json'
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


