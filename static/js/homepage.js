"use strict";

function incrementButton(id) {
    let element = document.getElementById(`incrementText-${id}`);
    let value = element.innerHTML;
    
    ++value;

    console.log(value)
    document.getElementById(`incrementText-${id}`).innerHTML = value;
    // alert('Like button clicked!');
}



// $('#comment-area').on('submit', (evt) => {
//     evt.preventDefault();
//     alert('Handled with AJAX!');

//     const addComment = {
//         'comment': $('#comment-text').val()
//     };

//     $.post('/add_comment', addComment, (res) => {
//         $('#comment-show').html(res);
//         console.log(res)
        

//     });
// });
















