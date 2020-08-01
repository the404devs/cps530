//auto-format phone input
//this also makes it not accept letters
$('#phone').mask("(999)-999-9999",{placeholder:""});

//Function to validate name input, make sure it only has letters
function validate(){
    if(document.getElementById('name').value.match(/^[a-zA-Z-,]+(\s{0,1}[a-zA-Z-, ])*$/)){
        return true;
    }
    return false;
}

//Fires when one of the submit buttons is hit
//Given an arg to determine which script to send the form to.
function submit(ext){
    if (validate()){//Validate name input
        $("#form").attr('action', 'cgi-bin/lab6.'+ext);//Set the target of the form
        $("#form").submit();//submit the form to whichever script the user clicked
    }
    else{
        alert("Name is incorrectly formatted.");//Validation failed.
    } 
}
