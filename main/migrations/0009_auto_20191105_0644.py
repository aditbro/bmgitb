# Generated by Django 2.2 on 2019-11-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190926_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='internasional',
            field=models.BooleanField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='tpb',
            field=models.BooleanField(max_length=100),
        ),
    ]
