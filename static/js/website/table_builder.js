function build_table(object_list) {
    table = document.createElement("table")
    table_header = build_table_header(object_list[0])
    table_body = build_table_body(object_list)

    table.appendChild(table_header)
    table.appendChild(table_body)

    return table
}

function build_table_header(object) {
    thead = document.createElement("thead")
    tr = document.createElement("tr")

    object.constructor.table_columns.forEach(column => {
        th = document.createElement("th")
        th.innerHTML = column.replace(/_/g, " ")
        tr.appendChild(th)
    })

    thead.appendChild(tr)

    return thead
}

function build_table_body(object_list) {
    tbody = document.createElement("tbody")

    object_list.forEach(object => {
        tr = document.createElement("tr")
        tr.onclick = function() { window.location.href = object.data_page_url }

        object.constructor.table_columns.forEach(column => {
            td = document.createElement("td")
            td.innerHTML = object.data[column]
            
            tr.appendChild(td)
        })

        tbody.appendChild(tr)
    })

    return tbody
}