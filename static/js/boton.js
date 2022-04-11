
function processcooling(){
    cooling1.btncooling1.disabled = true;
    if(btncooling1.disabled == true){
        setTimeout(function(){
            btncooling1.removeAttribute('disabled');
            cooling1.btncooling1.value = 'Cerrar';
            cooling1.btncooling1.close = true;
        }, 3000);
        return false;
    }
}


cooling1.btncooling1.getEventListener("click", function(){
    return processcooling();
}, false);

