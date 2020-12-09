$(document).ready(function(){
    $('.collapsible').collapsible();
    $("select").formSelect();
    $('.carousel').carousel();
    setInterval(function() {
        $(".carousel").carousel("next");
    }, 3000);
});