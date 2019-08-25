from django.urls import path
from main.api import PasienController
from . import api
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="login page"),

    path('pasien/', PasienController().call),
    path('pasien/<str:no_pasien>/', PasienController().call),

    path('klinik/kunjungan/insert/', api.kunjungan.kunjungan_insert, name='insert kunjungan'),
    path('klinik/kunjungan/update/', api.kunjungan.kunjungan_update, name='insert kunjungan'),
    path('klinik/kunjungan/<str:kode_kunjungan>/', api.kunjungan.kunjungan_get, name='get kunjungan'),
    path('klinik/kunjungan/', api.kunjungan.kunjungan_get_list, name='get kunjungan list'),

    path('klinik/tindakan/insert/', api.tindakan.tindakan_kunjungan_insert, name='insert tindakan kunjungan'),
    path('klinik/tindakan/<str:kode_kunjungan>', api.tindakan.tindakan_kunjungan_get_list, name='insert tindakan kunjungan'),

    path('apotek/resep/insert/', api.apotek.pembelian_resep_insert, name='insert pembelian resep'),
    path('apotek/otc/insert/', api.apotek.pembelian_otc_insert, name='insert pembelian resep'),

    path('user/authenticate/', api.user_management.user_authenticate, name='login'),
    path('user/create/', api.user_management.user_insert, name='create user'),
    path('user/profile/', api.user_management.profile_get, name='get user profile'),
]