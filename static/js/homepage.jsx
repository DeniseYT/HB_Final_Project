"use strict";

function myFunction() {

    <p>I am a team player. I am outgoing, dedicated, and open-minded.<span id="dots">...</span><span id="more">
        I get across to people and adjust to changes with ease. I believe that a person should work on developing 
        their professional skills and learning new things all the time.</span></p>


    const dots = document.getElementById("dots");
    const moreText = document.getElementById("more");
    const btnText = document.getElementById("myBtn");
    
    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more"; 
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less"; 
        moreText.style.display = "inline";
    }
    }

<button onclick="myFunction()" id="myBtn">Read more</button>


