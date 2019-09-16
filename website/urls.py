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
]