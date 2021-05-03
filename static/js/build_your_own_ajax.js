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


// jQuery + AJAX
$('#submit').on('submit', (evt) => {
    evt.preventDefault();

    const formInputs = {
        'about': $('#about').val(),
        'experience': $('#experience').val(),
        'project': $('#project').val(),
        'skill': $('#skill').val(),
        'education': $('#education').val(),
        'contact': $('#contact').val()
    };

    $.post('/build', formInputs, (res) => {
        $('#about-div').html(res.about);
        $('#experience-div').html(res.experience);
        $('#project-div').html(res.project);
        $('#skill-div').html(res.skill);
        $('#education-div').html(res.education);
        $('#contact-div').html(res.contact);
    });
});





