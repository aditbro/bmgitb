class PembelianOTC {
    static name = "pembelian"
    static table_columns = ['tarif', 'waktu_pembelian']
    static search_columns = ['obat__obat__kode', 'tarif']
    static url = "/main/apotek/otc/"

    constructor(json_data) {
        this.data = json_data
        this.data['nama_pasien'] = this.data['pasien']['nama']
        this.resource_url = "/main/apotek/otc/" + json_data["id"] + "/"
        this.data_page_url = "/apotek/otc/" + json_data["id"] + "/"
    }

    static get_search_dict(search_text) {
        console.log(search_text)
        if (!search_text) return null
        
        var search_dict = {}

        this.search_columns.forEach(function(column, index) {
            search_dict[column] = search_text;
        })

        return search_dict
    }
}