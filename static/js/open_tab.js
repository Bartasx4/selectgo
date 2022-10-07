function open_tab(evt, generation) {
    // Declare all variables
    var i, tabcontent, tablinks;
    var hide = false;
    if (document.getElementById(generation).style.display == "block"){
        hide = true;
    }

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tab-generation");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    if (hide == false){
        document.getElementById(generation).style.display = "block";
        evt.currentTarget.className += " active";
    }
}