$(window).on('load', function () {
    $( "#datepicker" ).datepicker();
});
  
setTimeout(function() {
    jQuery('#message').fadeOut('slow');

},3000);
//after 3 secs
     
function validate(){
    inputText = document.getElementById("datepicker").value;

    if(!/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(inputText)){
        alert("Incorrect Date format")
        return false;
    }
    else
        return true;
}