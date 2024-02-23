document.getElementById('pull-chain').addEventListener('click', function() {
console.log("Check");
var image = document.getElementById('light');
if (image.style.display == 'none') {
    image.style.display = 'block';
} else {
    image.style.display = 'none';
}
});

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}  