# Generated by Django 2.2 on 2019-09-25 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190925_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter_subsidi_obat',
            old_name='max_subsidi_per_pembelian',
            new_name='max_subsidi_per_kunjungan',
        ),
    ]
