function darkmode() {
    var flashlight = document.getElementById("flashlight");
    var noflashlight = document.getElementById("noflashlight");
    var body = document.getElementById("body");
    var headline = document.getElementById("headline");
    var speed = document.getElementById("speed");
    var reverb = document.getElementById("reverb");


    if (noflashlight.classList.contains("hidden")) {
        noflashlight.classList.remove("hidden");
        flashlight.classList.add("hidden");
        body.classList.remove("bg-dark");
        headline.classList.remove("white");
        headline.classList.add("black");
        headline.classList.remove("white-shadow");
        headline.classList.add("black-shadow");
        speed.classList.remove("white");
        speed.classList.add("black");
        speed.classList.remove("white-shadow");
        speed.classList.add("black-shadow");
        reverb.classList.remove("white");
        reverb.classList.add("black");
        reverb.classList.remove("white-shadow");
        reverb.classList.add("black-shadow");
    }
    else if (flashlight.classList.contains("hidden")) {
        flashlight.classList.remove("hidden");
        noflashlight.classList.add("hidden");
        body.classList.add("bg-dark");
        headline.classList.remove("black");
        headline.classList.add("white");
        headline.classList.remove("black-shadow");
        headline.classList.add("white-shadow");
        speed.classList.remove("black");
        speed.classList.add("white");
        speed.classList.remove("black-shadow");
        speed.classList.add("white-shadow");
        reverb.classList.remove("black");
        reverb.classList.add("white");
        reverb.classList.remove("black-shadow");
        reverb.classList.add("white-shadow");
    }
}



function updateLink() {
    let link = document.getElementById("link");
    let input = document.getElementById("input");

    if (link.innerHTML != null) {
        input.value.substr(1) = link;
    }
}
window.onload = updateLink();


function updateSliderValue(sliderId, pId) {
    var slider = document.getElementById(sliderId);
    var pTag = document.getElementById(pId);
    pTag.innerHTML = slider.value;
}