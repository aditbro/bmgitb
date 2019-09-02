$(document).ready(function() {
    fetch_resource_data();
})

document.getElementById("prev-page-btn").addEventListener("click", function() {
    page_number = parseInt(document.getElementById("page-number").innerHTML) - 1
    search_text = document.getElementById("search-bar").value
    if(page_number > 0) {
        fetch_resource_data(page_number, 10, search_text)
    }
})

document.getElementById("next-page-btn").addEventListener("click", function() {
    page_number = parseInt(document.getElementById("page-number").innerHTML) + 1
    search_text = document.getElementById("search-bar").value
    fetch_resource_data(page_number, 10, search_text)
})

document.getElementById("search-bar").addEventListener("keyup", function(event) {
    enterKeyCode = 13
    if (event.keyCode === enterKeyCode) {
        event.preventDefault()
        search_text = document.getElementById("search-bar").value
        fetch_resource_data(page = 1, limit = 10, search_text = search_text)
    }
})

function fetch_resource_data(page = 1, limit = 10, search_text = undefined) {
    console.log(Resource)
    data = { "page": page, "limit": limit,  ...Resource.get_search_dict(search_text)}
    get_query = new URLSearchParams(data).toString()
    url = Resource.url + "?" + get_query
    send_get_request(url, fetch_resource_data_callback)
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

function build_resource_list(json_list) {
    resource_list = []
    
    json_list.forEach(json => {
        resource_list.push(new Resource(json))
    })

    return resource_list
}

function fetch_resource_data_callback(xhttp) {
    if(xhttp.readyState == 4 && xhttp.status == 200) {
        response_data = JSON.parse(xhttp.responseText)
        resource_list = build_resource_list(response_data[Resource.name])
        if(resource_list.length == 0) {
            alert("Data tidak ditemukan")
            return
        }

        table_div = document.getElementById("data-table")
        new_table = build_table(resource_list)
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