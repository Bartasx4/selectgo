function load(url, myFunction, data='', method='POST') {
    var dfrd1 = $.Deferred();
    var xhttp = new XMLHttpRequest();
    var element = new Object();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myFunction(this.responseText);
            dfrd1.resolve();
        }
    };
    xhttp.open(method, url, true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send(data);
    return $.when(dfrd1).done(function(){
    }).promise();
}