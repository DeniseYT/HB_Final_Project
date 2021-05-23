"use strict";


console.log("hi jsx is connecting")

const userProfileData = [
  {
    about: 'This is about me',
    experience: 'This is my experience',
    project: 'This is my project',
    skill: 'This is my skill',
    education: 'This is my education',
    contact: 'This is my contact'
  }
];

function UserProfileAbout(props) {
  return (
    <div id="about-div">
      <h3>{props.about}</h3>
    </div>
  );
}

function UserProfileExperience(props) {
    return (
      <div id="experience-div">
        <h2>{props.experience}</h2>
      </div>
    );
  }

// function TradingCardContainer(props) {
//   const tradingCards = [];

//   for (const currentCard of tradingCardData) {
//     tradingCards.push(
//       <TradingCard
//         name={currentCard.name}
//         skill={currentCard.skill}
//         imgUrl={currentCard.imgUrl}
//       />
//     );
//   }

//   return (
//     <React.Fragment>
//       {tradingCards}
//     </React.Fragment>
//   );
// }

ReactDOM.render(
  <UserProfileAbout />,
  document.getElementById('about-div'),
  document.getElementById('experience-div')
);