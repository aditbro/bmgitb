from django.contrib import admin
from main.models import Parameter_Subsidi_Kunjungan, Parameter_Subsidi_Obat, Parameter_Subsidi_Tindakan
from main.models import Klinik

# Register your models here.
admin.site.register(Parameter_Subsidi_Kunjungan)
admin.site.register(Parameter_Subsidi_Obat)
admin.site.register(Parameter_Subsidi_Tindakan)

admin.site.register(Klinik)