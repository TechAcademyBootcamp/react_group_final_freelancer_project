function close_bar(id){
    var y=document.getElementById(`edit-bar-${id}`).classList.contains('open-edit-bar')
    var bars=document.querySelectorAll('.edit-bar')
    for(var x=0; x < bars.length; x++)
    {
        bars[x].classList.remove('open-edit-bar');
    }
    if (y==true){
        document.getElementById(`edit-bar-${id}`).classList.remove('open-edit-bar')
    }
    else{
        document.getElementById(`edit-bar-${id}`).classList.add('open-edit-bar')
    }
}