
$('#phone').mask("(999)-999-9999",{placeholder:""});

function validate(){
    alert(document.getElementById("name").value);
}


function fades(){
    console.log("fuck");
    $('#segment1').fadeIn(500);
    $('#segment2').fadeIn(1500);
    $('#dash').fadeIn(2500);
    $('#segment3').fadeIn(2500);
}
$(function(){fades()});
