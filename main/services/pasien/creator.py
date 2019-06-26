from datetime import datetime
from main.models import (
    Pasien,
    Mahasiswa,
    Karyawan_BMG,
    Karyawan_ITB,
    Keluarga_Karyawan_ITB,
    Mitra_Kerja_Sama,
    Umum
)
from main.models import (
    Subsidi_Kunjungan,
    Subsidi_Obat,
    Subsidi_Tindakan
)

class PasienCreator():
    def __init__(self, params):
        self.params = params

    def create(self):
        self.create_pasien()
        self.init_subsidi()
        return self.pasien

    def create_pasien(self):
        self.pasien = self.construct_pasien()
        self.pasien.save()

    def construct_pasien(self):
        kategori = self.params['kategori']
        self.params['no_pasien'] = Pasien.new_id
        
        return {
            'Mahasiswa': Mahasiswa,
            'Karyawan BMG': Karyawan_BMG,
            'Karyawan ITB': Karyawan_ITB,
            'Keluarga Karyawan': Keluarga_Karyawan_ITB,
            'Mitra Kerja Sama': Mitra_Kerja_Sama,
            'Umum': Umum
        }.get(kategori)(**self.params)

    def init_subsidi(self):
        Subsidi_Kunjungan.create_pasien_subsidi_from_parameter(self.pasien)
        Subsidi_Obat.create_pasien_subsidi_from_parameter(self.pasien)
        Subsidi_Tindakan.create_pasien_subsidi_from_parameter(self.pasien)
