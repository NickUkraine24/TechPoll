$(document).ready(function () {
    $("body").popover({
        selector: "[data-toggle='popover']",
        container: "body",
        html: true
    }).click(function () {
        setTimeout(function () {
            $('.hintPopover').popover('hide')
        }, 3000);
    });
});
