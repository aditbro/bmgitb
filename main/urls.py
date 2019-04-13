from django.urls import path
from . import api
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="login page"),

    path('pasien/insert/', api.pasien.pasien_insert, name='insert pasien'),
    path('pasien/update/', api.pasien.pasien_update, name='update pasien'),
    path('pasien/<str:no_pasien>/', api.pasien.pasien_get, name='get pasien'),
    path('pasien/', api.pasien.pasien_get_list, name='get pasien list'),

    path('klinik/kunjungan/insert/', api.kunjungan.kunjungan_insert, name='insert kunjungan'),
    path('klinik/kunjungan/update/', api.kunjungan.kunjungan_update, name='insert kunjungan'),
    path('klinik/kunjungan/<str:kode_kunjungan>/', api.kunjungan.kunjungan_get, name='get kunjungan'),
    path('klinik/kunjungan/', api.kunjungan.kunjungan_get_list, name='get kunjungan list'),

    path('klinik/tindakan/insert/', api.tindakan.tindakan_kunjungan_insert, name='insert tindakan kunjungan'),
    path('klinik/tindakan/<str:kode_kunjungan>', api.tindakan.tindakan_kunjungan_get_list, name='insert tindakan kunjungan'),

    path('apotek/resep/insert/', api.apotek.pembelian_resep_insert, name='insert pembelian resep'),
    path('apotek/otc/insert/', api.apotek.pembelian_otc_insert, name='insert pembelian resep')
]