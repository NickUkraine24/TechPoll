function change_url_previous() {
    url = window.location.pathname;
    if (parseInt(url.charAt(url.length-1)) == 1){
        document.getElementById("previousStage").disabled = true;
        // var elem = document.getElementById('previousStage');
        // elem.parentNode.removeChild(elem);
        // return false;
        var d = document.getElementById("previousStage");
        d.className += " disabled";
    }
    else {
        stage_id = parseInt(url.charAt(url.length - 1)) - 1;
        new_url = url.substr(0, url.length - 1).concat(stage_id);
        window.open(new_url, '_self');
    }
}

function change_url_next() {
    url = window.location.pathname;
    stage_id = parseInt(url.charAt(url.length-1)) + 1;
    new_url = url.substr(0, url.length-1).concat(stage_id);
    window.open(new_url, '_self');
}
