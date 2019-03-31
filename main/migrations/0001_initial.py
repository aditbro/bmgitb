# Generated by Django 2.1.7 on 2019-03-31 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('nama', models.CharField(max_length=255)),
                ('kode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis_Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnosis', models.ManyToManyField(to='main.Diagnosis')),
            ],
        ),
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=100, unique=True)),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Klinik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=100, unique=True)),
                ('nama', models.CharField(max_length=100)),
                ('tarif_kunjungan', models.IntegerField()),
                ('is_subsidi', models.CharField(default='False', max_length=100)),
                ('is_cash', models.CharField(default='True', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(blank=True, max_length=100, null=True)),
                ('tarif', models.IntegerField()),
                ('klaim', models.IntegerField()),
                ('cash', models.IntegerField()),
                ('asal', models.CharField(blank=True, max_length=100, null=True)),
                ('waktu_kunjungan', models.DateTimeField(blank=True)),
                ('is_valid', models.BooleanField(blank=True, default=True)),
                ('dokter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dokter')),
                ('klinik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Klinik')),
                ('koreksi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Kunjungan')),
            ],
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('kode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('jumlah_stok', models.IntegerField()),
                ('satuan', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=800)),
                ('harga_otc', models.IntegerField()),
                ('harga_resep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter_Subsidi_Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_pasien', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=800)),
                ('max_subsidi_per_kunjungan', models.IntegerField()),
                ('sisa_subsidi_bulan_ini', models.IntegerField()),
                ('sisa_subsidi_tahunan', models.IntegerField()),
                ('klinik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Klinik')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter_Subsidi_Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_pasien', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=800)),
                ('max_subsidi_per_pembelian', models.IntegerField()),
                ('sisa_subsidi_bulan_ini', models.IntegerField()),
                ('sisa_subsidi_tahunan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter_Subsidi_Tindakan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_pasien', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=100)),
                ('keterangan', models.CharField(blank=True, max_length=800, null=True)),
                ('max_subsidi_per_kunjungan', models.IntegerField()),
                ('sisa_subsidi_bulan_ini', models.IntegerField()),
                ('sisa_subsidi_tahunan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter_Tarif_Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_pasien', models.CharField(max_length=100)),
                ('tarif', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_pasien', models.CharField(blank=True, max_length=100, null=True)),
                ('kategori', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=255)),
                ('tipe_kartu_identitas', models.CharField(max_length=100)),
                ('nomor_kartu_identitas', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField(verbose_name='tanggal lahir')),
                ('gender', models.CharField(max_length=100)),
                ('waktu_registrasi', models.DateTimeField(blank=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('no_telepon', models.CharField(blank=True, max_length=100, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=100, null=True)),
                ('golongan_darah', models.CharField(blank=True, max_length=100, null=True)),
                ('rhesus', models.CharField(blank=True, max_length=100, null=True)),
                ('catatan', models.CharField(blank=True, max_length=800, null=True)),
                ('alamat', models.CharField(blank=True, max_length=800, null=True)),
                ('kota', models.CharField(blank=True, max_length=100, null=True)),
                ('subsidi_initiated', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PembelianObatOTC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Obat')),
            ],
        ),
        migrations.CreateModel(
            name='PembelianObatResep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Obat')),
            ],
        ),
        migrations.CreateModel(
            name='PembelianOTC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarif', models.IntegerField()),
                ('bayar', models.IntegerField()),
                ('waktu_pembelian', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PembelianResep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarif', models.IntegerField()),
                ('subsidi', models.IntegerField()),
                ('bayar', models.IntegerField()),
                ('waktu_pembelian', models.DateTimeField(auto_now_add=True)),
                ('kunjungan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Kunjungan')),
            ],
        ),
        migrations.CreateModel(
            name='Subsidi_Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.CharField(max_length=800)),
                ('max_subsidi_per_kunjungan', models.IntegerField(blank=True, null=True)),
                ('sisa_subsidi_bulan_ini', models.IntegerField(blank=True, null=True)),
                ('sisa_subsidi_tahunan', models.IntegerField(blank=True, null=True)),
                ('klinik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Klinik')),
            ],
        ),
        migrations.CreateModel(
            name='Subsidi_Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=800)),
                ('max_subsidi_per_pembelian', models.IntegerField(blank=True, null=True)),
                ('sisa_subsidi_bulan_ini', models.IntegerField(blank=True, null=True)),
                ('sisa_subsidi_tahunan', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subsidi_Tindakan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(blank=True, max_length=100, null=True)),
                ('keterangan', models.CharField(max_length=800)),
                ('max_subsidi_per_kunjungan', models.IntegerField(blank=True, null=True)),
                ('sisa_subsidi_bulan_ini', models.IntegerField(blank=True, null=True)),
                ('sisa_subsidi_tahunan', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tindakan',
            fields=[
                ('nama', models.CharField(max_length=255)),
                ('kode', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(max_length=800)),
                ('tarif', models.IntegerField()),
                ('is_subsidi', models.CharField(default='False', max_length=100)),
                ('is_cash', models.CharField(default='True', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tindakan_Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.IntegerField()),
                ('klaim', models.IntegerField()),
                ('kunjungan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Kunjungan')),
                ('tindakan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tindakan')),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan_BMG',
            fields=[
                ('pasien_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pasien')),
                ('nip', models.CharField(max_length=100, unique=True)),
            ],
            bases=('main.pasien',),
        ),
        migrations.CreateModel(
            name='Karyawan_ITB',
            fields=[
                ('pasien_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pasien')),
                ('nip', models.CharField(max_length=100, unique=True)),
            ],
            bases=('main.pasien',),
        ),
        migrations.CreateModel(
            name='Keluarga_Karyawan_ITB',
            fields=[
                ('pasien_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pasien')),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Karyawan_ITB')),
            ],
            bases=('main.pasien',),
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('pasien_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pasien')),
                ('nim', models.CharField(max_length=100, unique=True)),
                ('strata', models.CharField(max_length=100)),
                ('internasional', models.CharField(max_length=100)),
                ('tpb', models.CharField(max_length=100)),
                ('program_studi', models.CharField(max_length=100)),
                ('fakultas', models.CharField(max_length=100)),
            ],
            bases=('main.pasien',),
        ),
        migrations.CreateModel(
            name='Mitra_Kerja_Sama',
            fields=[
                ('pasien_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pasien')),
                ('organisasi', models.CharField(max_length=100)),
            ],
            bases=('main.pasien',),
        ),
        migrations.CreateModel(
            name='Umum',
            fields=[
                ('pasien_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pasien')),
            ],
            bases=('main.pasien',),
        ),
        migrations.AddField(
            model_name='subsidi_tindakan',
            name='pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pasien'),
        ),
        migrations.AddField(
            model_name='subsidi_tindakan',
            name='tindakan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tindakan'),
        ),
        migrations.AddField(
            model_name='subsidi_obat',
            name='pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pasien'),
        ),
        migrations.AddField(
            model_name='subsidi_kunjungan',
            name='pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pasien'),
        ),
        migrations.AddField(
            model_name='pembelianresep',
            name='pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pasien'),
        ),
        migrations.AddField(
            model_name='pembelianobatresep',
            name='pembelianResep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PembelianResep'),
        ),
        migrations.AddField(
            model_name='pembelianobatotc',
            name='pembelianOTC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PembelianOTC'),
        ),
        migrations.AddField(
            model_name='parameter_subsidi_tindakan',
            name='tindakan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tindakan'),
        ),
        migrations.AddField(
            model_name='kunjungan',
            name='pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pasien'),
        ),
        migrations.AddField(
            model_name='dokter',
            name='klinik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Klinik'),
        ),
        migrations.AddField(
            model_name='diagnosis_kunjungan',
            name='kunjungan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Kunjungan'),
        ),
    ]
