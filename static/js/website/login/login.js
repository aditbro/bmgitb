document.getElementById("login-btn").addEventListener("click", login)

function login() {
    data = JSON.stringify(getLoginData())
    xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() { verify_login(this) }
    xhttp.open("POST", "/main/user/authenticate/", true);
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8")
    xhttp.send(data)
}

function getLoginData() {
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    return {
        "username" : username,
        "password" : password
    }
}

function verify_login(xhttp) {
    if(xhttp.readyState == 4 && xhttp.status == 200) {
        token = JSON.parse(xhttp.responseText)["access_token"]
        saveAccessTokenToCookie(token)
        moveToMainPage()
    } else if(xhttp.readyState == 4){
        alert(xhttp.responseText)
    }
}

function saveAccessTokenToCookie(token) {
    Cookies.set('access_token', token)
    console.log(token)
}

function moveToMainPage() {
    window.location.href = '/'
}