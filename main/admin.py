from django.contrib import admin
from main.models import *

# Register your models here.

#subsidi
admin.site.register(Parameter_Subsidi_Kunjungan)
admin.site.register(Parameter_Subsidi_Obat)
admin.site.register(Parameter_Subsidi_Tindakan)
admin.site.register(Subsidi_Kunjungan)
admin.site.register(Subsidi_Obat)
admin.site.register(Subsidi_Tindakan)

#pasien
admin.site.register(Pasien)
admin.site.register(Mahasiswa)
admin.site.register(Karyawan_BMG)
admin.site.register(Karyawan_ITB)
admin.site.register(Keluarga_Karyawan_ITB)
admin.site.register(Umum)
admin.site.register(Mitra_Kerja_Sama)

#kunjungan
admin.site.register(Kunjungan)
admin.site.register(Diagnosis_Kunjungan)
admin.site.register(Tindakan_Kunjungan)
admin.site.register(Parameter_Tarif_Kunjungan)

#apotek
admin.site.register(Obat)
admin.site.register(PembelianOTC)
admin.site.register(PembelianResep)

#klinik
admin.site.register(Klinik)
admin.site.register(Tindakan)
admin.site.register(Dokter)
admin.site.register(Diagnosis)