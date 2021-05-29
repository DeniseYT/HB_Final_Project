"use strict";

function incrementButton(id) {
    let element = document.getElementById(`incrementText-${id}`);
    let value = element.innerHTML;
    
    ++value;

    console.log(value)
    document.getElementById(`incrementText-${id}`).innerHTML = value;
    // alert('Like button clicked!');
}



















