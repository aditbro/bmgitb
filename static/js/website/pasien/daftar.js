$(document).ready(function() {
    fetch_pasien_data();
})

document.getElementById("prev-page-btn").addEventListener("click", function() {
    page_number = parseInt(document.getElementById("page-number").innerHTML) - 1
    if(page_number > 0) {
        fetch_pasien_data(page_number)
    }
})

document.getElementById("next-page-btn").addEventListener("click", function() {
    page_number = parseInt(document.getElementById("page-number").innerHTML) + 1
    fetch_pasien_data(page_number)
})

function fetch_pasien_data(page = 1, limit = 10) {
    data = { "page": page, "limit": limit,  ...Pasien.get_search_dict()}
    get_query = new URLSearchParams(data).toString()
    url = Pasien.url + "?" + get_query
    send_get_request(url, fetch_pasien_data_callback)
    update_page_number(page)
}

function update_page_number(page) {
    page_number = document.getElementById("page-number")
    prev_btn = document.getElementById("prev-page-btn")
    next_btn = document.getElementById("next-page-btn")

    page_number.innerHTML = page

    if(page == 1) {
        prev_btn.className = "disabled";
    } else {
        prev_btn.className = "waves-effect";
    }
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

        table_div = document.getElementById("data-table")
        new_table = build_table(pasien_list)
        table_div.removeChild(table_div.childNodes[0])
        table_div.appendChild(new_table)
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