$(document).ready( function() {


    $(".ouch").click( function(event) {
           alert("You clicked me! ouch!");
});
    $("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });

$("#about-btn").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
 });
});

$('.rango_add').click(function(){
    var catid = $(this).attr('data-catid');
    var url = $(this).attr('data-url');
    var title = $(this).attr('data-title');
    var me = $(this)
    $.get('/rango/auto_add_page/', {category_id:catid, url: url, title:title}, function()
    {$.('#pages').html(data);
    me.hide();
    });
});




