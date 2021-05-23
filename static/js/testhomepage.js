"use strict";

console.log("connecting")

// $('#comment-btn').on('click', () => {
//     alert('Handled with jQuery!');
// })

const button = document.getElementById('like-btn');

function addLike() {
    let value = $('#like-show').val();
    value = Number(value);
    value = value + 1
}

button.addEventListener('click', addComment);