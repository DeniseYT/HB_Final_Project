"use strict";


console.log("hi jsx is connecting")

const userProfileData = [
  {
    about: 'I am a driven professional currently transitioning into full stack web development.',
    experience: 'Background with Linguist/localization-turned-software engineer.',
    project: 'My personal project is to create an interactive, responsive, and modern display for people to share their story.',
    skill: 'JavaScript/jQuery, AJAX, React, HTML/Jinja, CSS/Bootstrap, Python/Flask, SQL/PostgreSQL, SQLAlchemy',
    education: 'Hackbright Academy - Software Engineering Program',
    contact: 'Please leave me a message or connect at Linkedin & GitHub!'
  }
];

const colorStyle = {
  backgroundColor: "#A6886D"
}


function UserProfileAbout(props) {
  return (
    <div id="about-show">
      <p>{userProfileData[0].about}</p>
    </div>
  );
}

function UserProfileExperience(props) {
    return (
      <div id="experience-show">
        <p>{userProfileData[0].experience}</p>
      </div>
    );
  }

function UserProfileProject(props) {
  return (
    <div id="project-show">
      <p>{userProfileData[0].project}</p>
    </div>
  );
}

function UserProfileSkill(props) {
  return (
    <div id="skill-show">
      <p>{userProfileData[0].skill}</p>
    </div>
  );
}

function UserProfileEducation(props) {
  return (
    <div id="education-show">
      <p>{userProfileData[0].education}</p>
    </div>
  );
}

function UserProfileContact(props) {
  return (
    <div id="contact-show">
      <p>{userProfileData[0].contact}</p>
    </div>
  );
}



ReactDOM.render(
  <UserProfileAbout />,
  document.getElementById('about-show'),
);

ReactDOM.render(
    <UserProfileExperience />,
    document.getElementById('experience-show')
  );

ReactDOM.render(
  <UserProfileProject />,
  document.getElementById('project-show'),
);

ReactDOM.render(
  <UserProfileSkill />,
  document.getElementById('skill-show'),
);

ReactDOM.render(
  <UserProfileEducation />,
  document.getElementById('education-show'),
);

ReactDOM.render(
  <UserProfileContact />,
  document.getElementById('contact-show'),
);