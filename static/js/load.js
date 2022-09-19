function load(url, myFunction, data='', method='POST') {
    var dfrd1 = $.Deferred();
    var xhttp = new XMLHttpRequest();
    var element = new Object();
    setTimeout(function(){
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                myFunction(this.responseText);
            }
        };
        xhttp.open(method, url, true);
        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.send(data);
        dfrd1.resolve();
    }, 2000);
    return dfrd1.promise();
   }