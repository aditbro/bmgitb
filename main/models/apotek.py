from django.db import models
from django.forms.models import model_to_dict
from .pasien import Pasien
from .subsidi import Subsidi_Obat
from .kunjungan import Kunjungan

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

    def serialize(self):
        return model_to_dict(self)

    def __str__(self):
        return self.nama

class PembelianObatResep(models.Model):
    jumlah = models.IntegerField()
    obat = models.ForeignKey('Obat', on_delete=models.CASCADE)
    tarif = models.IntegerField()

    def serialize(self):
        data = model_to_dict(self)
        data['obat'] = self.obat.serialize()
        
        return data

    def __str__(self):
        return self.obat.nama + ' ' + str(self.jumlah)

class PembelianObatOTC(models.Model):
    jumlah = models.IntegerField()
    obat = models.ForeignKey('Obat', on_delete=models.CASCADE)
    tarif = models.IntegerField()

    def serialize(self):
        data = model_to_dict(self)
        data['obat'] = self.obat.serialize()
        
        return data

    def __str__(self):
        return self.obat.nama + ' ' + str(self.jumlah)

class PembelianOTC(models.Model):
    tarif = models.IntegerField()
    bayar = models.IntegerField()
    obat = models.ManyToManyField(PembelianObatOTC)
    waktu_pembelian = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        data = model_to_dict(self)
        data['waktu_pembelian'] = str(self.waktu_pembelian.strftime("%d %b %Y %H:%M"))
        data['obat'] = self.serialize_obat()

        return data

    def serialize_obat(self):
        data = []
        for o in self.obat.all():
            data.append(o.serialize())
        
        return data

class PembelianResep(models.Model):
    pasien = models.ForeignKey('Pasien', on_delete=models.CASCADE)
    tarif = models.IntegerField()
    subsidi = models.IntegerField()
    bayar = models.IntegerField()
    obat = models.ManyToManyField(PembelianObatResep, blank=True)
    waktu_pembelian = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        data = model_to_dict(self)
        data['waktu_pembelian'] = str(self.waktu_pembelian.strftime("%d %b %Y %H:%M"))
        data['obat'] = self.serialize_obat()
        data['pasien'] = self.pasien.serialize()

        return data

    def serialize_obat(self):
        data = []
        for o in self.obat.all():
            data.append(o.serialize())
        
        return data

    def __str__(self):
        return self.pasien.nama + ' ' + str(self.waktu_pembelian)

