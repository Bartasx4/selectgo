<<<<<<< HEAD
function toggle_element(id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            toggle_class(id, parseInt(this.responseText));
=======
function toggle_element(id, base_class='grid-element') {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            toggle_class(id, parseInt(this.responseText), base_class);
            get_command();
>>>>>>> a4c9c82 (Added options and sliders. Need to add sliders to cookies)
        }
    };
    xhttp.open('POST', '/toggle', true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send('id='+id);
}

<<<<<<< HEAD
function toggle_class(id, status) {
    var element = document.getElementById(id);
    const base_class = 'grid-element';
=======
function toggle_class(id, status, base_class) {
    var element = document.getElementById(id);
>>>>>>> a4c9c82 (Added options and sliders. Need to add sliders to cookies)
    toggle_data[id] = status;
    switch (status) {
        case 0:
            element.setAttribute('class', base_class);
            break;
        case 1:
            element.setAttribute('class', base_class+' show');
            break;
        case 2:
            element.setAttribute('class', base_class+' hide');
            break;
    }
}

function set_toggle(data) {
    for (let id in toggle_data) {
        if (toggle_data[id] > 0) {
            toggle_class(id, toggle_data[id]);
        }
    }
}