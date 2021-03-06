from django.db import transaction
from main.models import(
    Kunjungan,
    Pasien,
    Dokter,
    Klinik,
    Diagnosis,
    Diagnosis_Kunjungan,
    Tindakan_Kunjungan,
    Subsidi_Tindakan,
    Tindakan
)
import pry

class KunjunganCreator():
    def __init__(self, params):
        self.kunjungan_params = params.get('kunjungan')
        self.tindakan_params = self.kunjungan_params.pop('tindakan')
        self.diagnosis_params = self.kunjungan_params.pop('diagnosis')

        self.kunjungan = None
        self.tindakan_kunjungan = []
        self.diagnosis_kunjungan = []

    def call(self):
        with transaction.atomic():
            self.create_kunjungan()
            if(self.tindakan_params):
                self.insert_tindakan()
                self.reduce_subsidi_tindakan()
            if(self.diagnosis_params):
                self.insert_diagnosis()
        
        return self.kunjungan

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
            tindakan['tindakan'] = Tindakan.objects.get(kode=tindakan.pop('tindakan'))
            tindakan['kunjungan'] = self.kunjungan

            self.tindakan_kunjungan.append(Tindakan_Kunjungan.objects.create(**tindakan))

    def insert_diagnosis(self):
        for diagnosis in self.diagnosis_params:
            diagnosis['diagnosis'] = Diagnosis.objects.get(kode=diagnosis.pop('diagnosis'))
            diagnosis['kunjungan'] = self.kunjungan

            self.diagnosis_kunjungan.append(Diagnosis_Kunjungan.objects.create(**diagnosis))

    def reduce_subsidi_tindakan(self):
        for tindakan in self.tindakan_kunjungan:
            if(tindakan.klaim > 0):
                subsidi_tindakan = Subsidi_Tindakan.objects.get(
                    pasien__no_pasien=self.kunjungan.pasien.no_pasien,
                    tindakan__kode=tindakan.tindakan.kode
                )
                subsidi_tindakan.substract(tindakan.klaim)