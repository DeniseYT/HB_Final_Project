"use strict";

function incrementButton() {
    var element = document.getElementById('incrementText');
    var value = element.innerHTML;
    
    ++value;

    console.log(value)
    document.getElementById('incrementText').innerHTML = value;
    // alert('Like button clicked!');
}


// $('#comment-btn').on('click', () => {
//     alert('Handled with jQuery!');
// })

// function commentFunction() {
// var element = document.getElementById('comment-text');
// var value = element.innerHTML;
// console.log(value)
// document.getElementById('comment-show').innerHTML = value;
// }
















