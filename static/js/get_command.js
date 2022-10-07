function get_command() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('command-line').value = this.responseText;
            return this.responseText
        }
    };
    xhttp.open('POST', '/get-command', true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send();
}

function copy_to_clipboard() {
    var copyText = document.getElementById("command-line");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    alert("Skopiowano");
}