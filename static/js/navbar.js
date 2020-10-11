var index=0;
var current=true
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    var element=document.querySelector('nav');
    var clicked=true
    
    // 20 is an arbitrary number here, just to make you think if you need the prevScrollpos variable:
    if (currentScrollPos > 0) {
        console.log('asagidadi');
        if(current){
            // $('nav').show();
            $('nav').removeClass('oddAnimation').addClass('evenAnimation');
        }
        current=false
    }
    else{
        console.log('yuxaridadi');

        if(!current){
            $('nav').addClass('oddAnimation');
        }
        current=true
    }
}