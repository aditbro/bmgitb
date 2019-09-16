class Kunjungan {
    static name = "kunjungan"
    static table_columns = ['kode', 'nama_pasien', 'nama_dokter', 'waktu_kunjungan']
    static search_columns = ['kode', 'pasien__nama', 'dokter__nama']
    static url = "/main/klinik/kunjungan/"

    constructor(json_data) {
        this.data = json_data
        this.data['nama_pasien'] = this.data['pasien']['nama']
        this.data['nama_dokter'] = this.data['dokter']['nama']
        this.resource_url = "/main/klinik/kunjungan/" + json_data["kode"] + "/"
        this.data_page_url = "/kunjungan/" + json_data["kode"] + "/"
    }

    static get_search_dict(search_text) {
        if (search_text === undefined) return null
        
        var search_dict = {}

        this.search_columns.forEach(function(column, index) {
            search_dict[column] = search_text;
        })

        return search_dict
    }
}