from main.models import (
    Pasien,
    Mahasiswa,
    Karyawan_BMG,
    Karyawan_ITB,
    Keluarga_Karyawan_ITB,
    Mitra_Kerja_Sama,
    Umum
)

class PasienFetcher():
    def __init__(self, no_pasien):
        self.no_pasien = no_pasien

    def fetch(self):
        self.get_pasien()
        self.get_pasien_with_category_data()
        return self.pasien

    def get_pasien(self):
        self.pasien = Pasien.objects.get(no_pasien=self.no_pasien)

    def get_pasien_with_category_data(self):
        kategori = self.pasien.kategori

        return {
            'Mahasiswa': Mahasiswa,
            'Karyawan BMG': Karyawan_BMG,
            'Karyawan ITB': Karyawan_ITB,
            'Keluarga Karyawan': Keluarga_Karyawan_ITB,
            'Mitra Kerja Sama': Mitra_Kerja_Sama,
            'Umum': Umum
        }.get(kategori).objects.get(no_pasien=self.pasien.no_pasien)