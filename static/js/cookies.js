function save_cookie() {
    var xhttp = new XMLHttpRequest();
    var element = new Object();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

        }
    };
    xhttp.open('POST', '/save-cookie', true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send();
    return true;
}