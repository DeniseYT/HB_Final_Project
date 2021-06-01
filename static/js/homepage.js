"use strict";

function incrementButton(id) {
    let element = document.getElementById(`incrementText-${id}`);
    let value = element.innerHTML;
    
    ++value;

    console.log(value)
    document.getElementById(`incrementText-${id}`).innerHTML = value;
    // alert('Like button clicked!');
}



function darkMode() {
    document.body.style.background="#A6886D";
}
function lightMode() {
    document.body.style.background="#D9D4C5";
}


















