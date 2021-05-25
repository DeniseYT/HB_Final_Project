"use strict";

function incrementButton() {
    var element = document.getElementById('incrementText');
    var value = element.innerHTML;
    
    ++value;

    console.log(value)
    document.getElementById('incrementTextAbout').innerHTML = value;
}
















