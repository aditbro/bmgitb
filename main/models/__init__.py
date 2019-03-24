#Pasien
from .pasien import Pasien
from .pasien import Mahasiswa
from .pasien import Karyawan_BMG
from .pasien import Karyawan_ITB
from .pasien import Keluarga_Karyawan_ITB
from .pasien import Umum
from .pasien import Mitra_Kerja_Sama

#klinik
from .klinik import Kunjungan
from .klinik import Diagnosis
from .klinik import Klinik
from .klinik import Dokter
from .klinik import Tindakan

#apotek
from .apotek import Obat
from .apotek import PembelianOTC
from .apotek import PembelianResep

#subsidi
from .subsidi import Subsidi_Tindakan
from .subsidi import Subsidi_Obat
from .subsidi import Subsidi_Kunjungan
from .subsidi import Parameter_Subsidi_Kunjungan
from .subsidi import Parameter_Subsidi_Obat
from .subsidi import Parameter_Subsidi_Tindakan