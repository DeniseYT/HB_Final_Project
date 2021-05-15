"use strict";

// JS DOM + AJAX post request
// function formInputs(evt) {
//     evt.preventDefault();

//     const about = document.getElementById('about').value
//     const experience = document.getElementById('experience').value
//     const project = document.getElementById('project').value
//     const skill = document.getElementById('skill').value
//     const education = document.getElementById('education').value
//     const contact = document.getElementById('contact').value

//     $.post('/build', formInput, (res) => {
//         $('#about-div').html(res.about);
//         $('#experience-div').html(res.experience);
//         $('#project-div').html(res.project);
//         $('#skill-div').html(res.skill);
//         $('#education-div').html(res.education);
//         $('#contact-div').html(res.contact);
//     });
// }

// $('#submit').on('submit', formInputs);


// JS + AJAX
// document.querySelector('#contact')
//     .addEventListener('submit', (evt) => {
//         evt.preventDefault();

//         const formInputs = 
//         document.querySelector('#about').value;
//         document.querySelector('#experience').value;
//         document.querySelector('#project').value;
//         document.querySelector('#skill').value;
//         document.querySelector('#education').value;
//         document.querySelector('#contact').value;

//         $.post('/build', formInputs, (res) => {
//             document.querySelector('#about-div').innerHTML = res.about;
//             document.querySelector('#experience-div').innerHTML = res.experience;
//             document.querySelector('#project-div').innerHTML = res.project;
//             document.querySelector('#skill-div').innerHTML = res.skill;
//             document.querySelector('#education-div').innerHTML = res.education;
//             document.querySelector('#contact-div').innerHTML = res.contact;
//         });
//     });


// jQuery + AJAX
$('#submit').on('submit', (evt) => {
    // evt.preventDefault();

    const formInputs = {
        'about': $('#about').val(),
        'experience': $('#experience').val(),
        'project': $('#project').val(),
        'skill': $('#skill').val(),
        'education': $('#education').val(),
        'contact': $('#contact').val()
    };

    $.post('/build', formInputs, (res) => {
        alert(res);
        // $('#about-div').html(res.about);
        // $('#experience-div').html(res.experience);
        // $('#project-div').html(res.project);
        // $('#skill-div').html(res.skill);
        // $('#education-div').html(res.education);
        // $('#contact-div').html(res.contact);
    });
});

// jQuery + AJAX
$('#like-btn').on('like', (evt) => {
    // evt.preventDefault();

    const likeBtnClick = {
        'like': $('#like-show').val(),
    };

    $.post('/build', likeBtnClick, (res) => {
        alert(res);
        $('#like-show').html(res.like);
    });
});


$('#comment-btn').on('comment', (evt) => {
    // evt.preventDefault();

    const commentBtnClick = {
        'comment': $('#comment-show').val(),
    };

    $.post('/build', commentBtnClick, (res) => {
        alert(res);
        $('#comment-show').html(res.comment);
    });
});


