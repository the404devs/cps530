function fades(){
    /* I'm too lazy to animate all of the segements,
    so I just animate the first one. 
    Since the css sets the first one to display:inline, 
    nobody will ever know the difference.
    
    Unless they read my code, that is*/
    $('#segment1').animate({'margin-left':'250px'},2000);
    $('#segment1').animate({'margin-left':'0px'},2000);
    window.setTimeout(function() { fades() }, 4000);
}
$(function(){fades()});