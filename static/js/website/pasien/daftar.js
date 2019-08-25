function fetch_pasien_data(page = 1, limit = 10) {
    data = { "page": page, "limit": limit,  ...Pasien.get_search_dict()}
    get_query = new URLSearchParams(data).toString()
    url = Pasien.url + "?" + get_query
    send_get_request(url, fetch_pasien_data_callback)
}

function build_pasien_list(json_list) {
    pasien_list = []
    
    json_list.forEach(json => {
        pasien_list.push(new Pasien(json))
    })

    return pasien_list
}

function fetch_pasien_data_callback(xhttp) {
    if(xhttp.readyState == 4 && xhttp.status == 200) {
        response_data = JSON.parse(xhttp.responseText)
        pasien_list = build_pasien_list(response_data["pasien"])
        table = document.getElementById("data-table")
        build_table(table, pasien_list)
    } else if(xhttp.readyState == 4){
        alert(xhttp.responseText)
    }
}

function send_get_request(url, callback_function) {
    access_token = Cookies.get("access_token")
    xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() { callback_function(this) }
    xhttp.open("GET", url, true);
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8")
    xhttp.setRequestHeader("Access-token", access_token)
    xhttp.send(data)
}

$(document).ready(function() {
    fetch_pasien_data();
})