from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.main, name='index'),
    path('login/', views.login, name='login'),
    
    path('pasien/daftar/', views.daftar_pasien, name='daftar pasien'),
    path('kunjungan/daftar/', views.daftar_kunjungan, name='daftar kunjungan'),
    path('apotek/resep/daftar/', views.daftar_pembelian_resep, name='daftar pembelian resep'),
    path('apotek/resep/otc/', views.daftar_pembelian_otc, name='daftar pembelian otc'),

    path('pasien/data/<str:no_pasien>/', views.data_pasien, name='data pasien'),
    path('kunjungan/data/<int:id>/', views.data_kunjungan, name='data pasien'),
    path('apotek/resep/data/<int:id>/', views.data_pembelian_resep, name='data pembelian resep'),
    path('apotek/otc/data/<int:id>/', views.data_pembelian_otc, name='data pembelian otc'),

    path('pasien/registrasi/', views.form_insert_pasien, name='registrasi pasien')
]