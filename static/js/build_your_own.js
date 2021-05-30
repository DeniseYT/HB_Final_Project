"use strict";

$('#about-div').on('submit', (evt) => {
    evt.preventDefault();
    alert('Handled with AJAX!');

    const addAbout = {
        'about': $('#about').val()
    };

    $.post('/add_about', addAbout, (res) => {
        $('#about-show').html(res);
        console.log(res)
    });
});


$('#experience-div').on('submit', (evt) => {
    evt.preventDefault();
    alert('Handled with AJAX!');

    const addExperience = {
        'experience': $('#experience').val()
    };

    $.post('/add_experience', addExperience, (res) => {
        $('#experience-show').html(res);
        console.log(res)
    });
});


$('#project-div').on('submit', (evt) => {
    evt.preventDefault();
    alert('Handled with AJAX!');

    const addProject = {
        'project': $('#project').val()
    };

    $.post('/add_project', addProject, (res) => {
        $('#project-show').html(res);
        console.log(res)
    });
});


$('#skill-div').on('submit', (evt) => {
    evt.preventDefault();
    alert('Handled with AJAX!');

    const addSkill = {
        'skill': $('#skill').val()
    };

    $.post('/add_skill', addSkill, (res) => {
        $('#skill-show').html(res);
        console.log(res)
    });
});


$('#education-div').on('submit', (evt) => {
    evt.preventDefault();
    alert('Handled with AJAX!');

    const addEducation = {
        'education': $('#education').val()
    };

    $.post('/add_education', addEducation, (res) => {
        $('#education-show').html(res);
        console.log(res)
    });
});


$('#contact-div').on('submit', (evt) => {
    evt.preventDefault();
    alert('Handled with AJAX!');

    const addContact = {
        'contact': $('#contact').val()
    };

    $.post('/add_contact', addContact, (res) => {
        $('#contact-show').html(res);
        console.log(res)
    });
});


