from django.db import models
from .pasien import Pasien
from .subsidi import Subsidi_Obat

_short_length = 100
_medium_length = 255
_long_length = 800

class Obat(models.Model):
    kode = models.CharField(max_length=_short_length, primary_key=True)
    nama = models.CharField(max_length=_short_length)
    jumlah_stok = models.IntegerField()
    satuan = models.CharField(max_length=_short_length)
    keterangan = models.CharField(max_length=_long_length)
    harga_otc = models.IntegerField()
    harga_resep = models.IntegerField()

    def __str__(self):
        return self.nama

class PembelianObatOTC(models.Model):
    pembelianOTC = models.ForeignKey('PembelianOTC', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    obat = models.ForeignKey('Obat', on_delete=models.CASCADE)

class PembelianObatResep(models.Model):
    pembelianResep = models.ForeignKey('PembelianResep', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    obat = models.ForeignKey('Obat', on_delete=models.CASCADE)

class PembelianOTC(models.Model):
    tarif = models.IntegerField()
    bayar = models.IntegerField()
    waktu_pembelian = models.DateTimeField(auto_now_add=True)

class PembelianResep(models.Model):
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    kunjungan = models.ForeignKey('Kunjungan', on_delete=models.CASCADE)
    tarif = models.IntegerField()
    subsidi = models.IntegerField()
    bayar = models.IntegerField()
    waktu_pembelian = models.DateTimeField(auto_now_add=True)

    def save(self):
        super().save()
        self.reduce_subsidi_pasien()

    def reduce_subsidi_pasien(self):
        subsidi_pasien = Subsidi_Obat.objects.filter(pasien__id=self.pasien.id)[0]
        if(subsidi_pasien):
            subsidi_pasien.sisa_subsidi_bulan_ini -= self.klaim
            subsidi_pasien.sisa_subsidi_tahunan -= self.klaim

            if(subsidi_pasien.sisa_subsidi_bulan_ini < 0 or subsidi_pasien.sisa_subsidi_tahunan < 0) :
                raise Exception('Sisa subsidi pasien kurang untuk tindakan {}'.format(self.tindakan.nama))

            subsidi_pasien.save()

