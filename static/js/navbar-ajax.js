$(document).ready(function() {

/* Application */
	document.getElementById("nav-logout").addEventListener("click", logout);
	function logout() {
		//TODO logout 
	}

	function showProgressBar(){
	    document.getElementById('progress-bar').style.display = "block";
	    document.getElementById('overlay').style.display = "block";
	}

	function hideProgressBar(){
	    document.getElementById('progress-bar').style.display = "none";
	    document.getElementById('overlay').style.display = "none";
	}

	document.getElementById("nav-changePassword").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/change_password")
		hideProgressBar();
	});

	document.getElementById("nav-exit").addEventListener("click", function(){ 
		if (confirm("Apakah Anda yakin untuk menutup aplikasi?")) {	
			logout();
		}
  	});

/* Parameter */
	
	document.getElementById("nav-daftarKelompokPasien").addEventListener("click", function() {
		hideProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarKategoriPasien").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarKota").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarOrganisasi").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarUnitKerja").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarFakultas").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarProgram").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarStrata").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarPelayanan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarTindakanDokter").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarSpesialisDokter").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-daftarSubsidi").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-parameterGlobal").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

/* Data Pendukung */
	document.getElementById("nav-obat").addEventListener("click", function() { 
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
	});
	hideProgressBar();

	document.getElementById("nav-dokter").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-sisaSubsidi").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

/* Pengelolaan Data Pasien */
	document.getElementById("nav-inputDataMahasiswa").addEventListener("click", function(){
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/input_data_mahasiswa")
		hideProgressBar();
	});

	document.getElementById("nav-inputDataPegawaiITB").addEventListener("click", function(){
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/input_data_pegawai_itb")
		hideProgressBar();
	});
	
	document.getElementById("nav-inputDataPegawaiLain").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/input_data_pegawai_lain");
		hideProgressBar();
	});

	document.getElementById("nav-inputDataKeluargaPegawai").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/input_data_keluarga_pegawai")
		hideProgressBar();
	});

	document.getElementById("nav-inputDataPasienUmum").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/input_data_pasien_umum")
		hideProgressBar();
	});

	document.getElementById("nav-daftarPasien").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/daftar_pasien");
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarMahasiswa").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/daftar_mahasiswa");
		hideProgressBar();
	});

	document.getElementById("nav-daftarPegawai").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/data_pasien/daftar_pegawai");
		hideProgressBar();
	});

/* Pendaftaran Pasien */

    document.getElementById("nav-pendaftaranDokter").addEventListener("click", function() {
    	showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/input_data_kunjungan");
		hideProgressBar();
	});
	
	document.getElementById("nav-koreksiKunjungan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/daftar_kunjungan");
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarKunjungan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/daftar_kunjungan")
		hideProgressBar();
	});
	
	document.getElementById("nav-pendaftaranLab").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/input_data_lab");
		hideProgressBar();
	});

	document.getElementById("nav-daftarLab").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/daftar_lab")
		hideProgressBar();
	});
	
	document.getElementById("nav-pendaftaranTindakan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/input_tindakan_langsung")
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarTindakan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/daftar_tindakan_langsung")
		hideProgressBar();
	});
	
	document.getElementById("nav-buatSKS").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/input_sks")
		hideProgressBar();
	});

	document.getElementById("nav-daftarSKS").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/pendaftaran_pasien/daftar_sks")
		hideProgressBar();
	});

	document.getElementById("nav-inputDiagnosis").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

/* Transaksi Apotek */

	document.getElementById("nav-jualResep").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load("/transaksi_apotek/jual_resep")
		hideProgressBar();
	});
	
	document.getElementById("nav-jualOTC").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-koreksiPenjualanObat").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarPenjualanObat").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

/* Report */
	document.getElementById("nav-laporanTransaksiApotek").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-daftarKunjungan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-rekapitulasiKunjungan").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
	
	document.getElementById("nav-laporanDaftarPasien").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});

	document.getElementById("nav-diagnosis").addEventListener("click", function() {
		showProgressBar();
		$("#content").empty();
		$("#content").load()//TODO
		hideProgressBar();
	});
});