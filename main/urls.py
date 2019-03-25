from django.urls import path
from . import api

app_name = 'main'
urlpatterns = [
    path('pasien/insert/', api.pasien.pasien_insert, name='insert pasien'),
    path('pasien/update/', api.pasien.pasien_update, name='update pasien'),
    path('pasien/<str:no_pasien>/', api.pasien.pasien_get, name='get pasien'),
    path('pasien/', api.pasien.pasien_get_list, name='get pasien list'),
    # path('pasien/pegawai/insert/', api.pasien.pegawai_insert, name='insert pegawai'),
    # path('mahasiswa/', api.pasien.mahasiswa_get_list, name='get mahasiswa list'),
    # path('pegawai/', api.pasien.pegawai_get_list, name='get pegawai list'),

    # path('klinik/kunjungan/insert/', api.klinik.kunjungan_insert, name='insert kunjungan'),
    # path('klinik/kunjungan/<str:kode_kunjungan>/', api.klinik.kunjungan_get, name='insert kunjungan'),
    # path('klinik/kunjungan/update/<str:kode_kunjungan>/', api.klinik.kunjungan_update, name='insert kunjungan'),
    # path('klinik/kunjungan/delete/<str:kode_kunjungan>/', api.klinik.kunjungan_delete, name='delete kunjungan')
]