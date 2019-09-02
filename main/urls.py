from django.urls import path
from main.api import(
    PasienController,
    KunjunganController
)
from . import api
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="login page"),

    path('pasien/', PasienController().call),
    path('pasien/<str:no_pasien>/', PasienController().call),

    path('klinik/kunjungan/', KunjunganController().call, name='insert kunjungan'),
    path('klinik/kunjungan/<str:kode_kunjungan>/', KunjunganController().call, name='get kunjungan'),

    path('klinik/tindakan/insert/', api.tindakan.tindakan_kunjungan_insert, name='insert tindakan kunjungan'),
    path('klinik/tindakan/<str:kode_kunjungan>', api.tindakan.tindakan_kunjungan_get_list, name='insert tindakan kunjungan'),

    path('apotek/resep/insert/', api.apotek.pembelian_resep_insert, name='insert pembelian resep'),
    path('apotek/otc/insert/', api.apotek.pembelian_otc_insert, name='insert pembelian resep'),

    path('user/authenticate/', api.user_management.user_authenticate, name='login'),
    path('user/create/', api.user_management.user_insert, name='create user'),
    path('user/profile/', api.user_management.profile_get, name='get user profile'),
]