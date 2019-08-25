class Pasien {
    static table_columns = ['no_pasien', 'kategori', 'nama', 'nomor_kartu_identitas', 'waktu_registrasi']
    static search_columns = ['no_pasien', 'kategori', 'nama', 'nomor_kartu_identitas']
    static url = "/main/pasien/"

    constructor(json_data) {
        this.data = json_data
        this.resource_url = "/main/pasien/" + json_data["no_pasien"] + "/"
    }

    static get_search_dict(search_text) {
        if (search_text === undefined) return null
        
        var search_dict = {}

        this.table_columns.forEach(function(column, index) {
            search_dict[column] = search_text;
        })

        return search_dict
    }
}