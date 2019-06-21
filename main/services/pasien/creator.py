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
    def __init__(self, )
    def save(self):
        self.save_waktu_registrasi()
        super().save()
        self.no_pasien = 'P-' + str(self.id)
        super().save()
        if(not self.subsidi_initiated):
            self.init_subsidi()
            self.subsidi_initiated = True
            super().save()

    def init_subsidi(self):
        Subsidi_Kunjungan.create_pasien_subsidi_from_parameter(self)
        Subsidi_Obat.create_pasien_subsidi_from_parameter(self)
        Subsidi_Tindakan.create_pasien_subsidi_from_parameter(self)

    def save_waktu_registrasi(self):
        if(not self.waktu_registrasi):
            self.waktu_kunjungan = datetime.now()