$(window).on('load', function () {
    $( '#fromDate').datepicker();
    $( '#toDate').datepicker();

});
     
function validate(){
    
    inputText = document.getElementById('toDate').value;
    inputText2 = document.getElementById('fromDate').value;
    
    if(!/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(inputText)){
        alert("Incorrect Date format")
        return false;
    }
    else if(!/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(inputText2)){
        alert("Incorrect Date format")
        return false;
    }
    else
        return true;
}