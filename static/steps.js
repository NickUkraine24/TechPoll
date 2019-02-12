function change_url_previous() {
    // Logic for switch a button
    url = window.location.pathname;
    if (parseInt(url.charAt(url.length-1)) == 1){
        document.getElementById("previousStage").disabled = true;
        var d = document.getElementById("previousStage");
        d.className += " disabled";
    }
    else {
        stage_id = parseInt(url.charAt(url.length - 1)) - 1;
        new_url = url.substr(0, url.length - 1).concat(stage_id);
        window.open(new_url, '_self');
    }
}
