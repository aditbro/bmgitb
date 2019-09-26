from django.db import transaction
from main.models import(
    Kunjungan,
    Pasien,
    Dokter,
    Klinik,
    Diagnosis,
    Diagnosis_Kunjungan,
    Tindakan_Kunjungan
)

class KunjunganCreator():
    def __init__(self, params):
        self.kunjungan_params = params.get('kunjungan')
        self.tindakan_params = params.get('tindakan')
        self.diagnosis_params = params.get('diagnosis')

        self.kunjungan = None
        self.tindakan_kunjungan = []
        self.diagnosis_kunjungan = []

    def cal(self):
        with transaction.atomic():
            self.create_kunjungan()
            if(self.tindakan_params):
                self.insert_tindakan()
            if(self.diagnosis_params):
                self.insert_diagnosis()

    def create_kunjungan(self):
        self.kunjungan_params['kode'] = Kunjungan.new_id()
        self.kunjungan_params['pasien'] = Pasien.objects.get(no_pasien=self.kunjungan_params['pasien'])
        self.kunjungan_params['klinik'] = Klinik.objects.get(kode=self.kunjungan_params['klinik'])
        self.kunjungan_params['dokter'] = Dokter.objects.get(kode=self.kunjungan_params['dokter'])
        self.kunjungan_params['cash'] = self.kunjungan_params['tarif']
        self.kunjungan_params['klaim'] = 0

        self.kunjungan = Kunjungan.objects.create(**self.kunjungan_params)

    def insert_tindakan(self):
        for tindakan in self.tindakan_params:
            tindakan['tindakan'] = Tindakan.objects.get(kode=tindakan.pop('kode'))
            tindakan['kunjungan'] = self.kunjungan

            self.tindakan_kunjungan.append(Tindakan_Kunjungan.objects.create(**tindakan))

    def insert_diagnosis(self):
        for diagnosis in self.diagnosis_params:
            diagnosis['diagnosis'] = Diagnosis.objects.get(kode=diagnosis.pop('kode'))
            diagnosis['kunjungan'] = self.kunjungan

            self.diagnosis_kunjungan.append(Diagnosis_Kunjungan.objects.create(**diagnosis))