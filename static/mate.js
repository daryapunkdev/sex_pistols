const quotes = [
  "You don't have to be clever to be a punk.",
  "We're not into music, we're into chaos.",
  "I am an antichrist. I am an anarchist.",
  "The only notes I know are the ones that say 'Get out'.",
  "God save the Queen – the fascist regime."
];

function giveMeQuote() {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  document.getElementById("quote").innerText = quotes[randomIndex];
}








function createFallingImage(imageFile, leftPosition) {
  const img = document.createElement("img");
  img.src = "/static/" + imageFile;
  img.className = "falling-object";
  img.style.left = leftPosition;
  document.body.appendChild(img);

  setTimeout(() => {
    img.remove(); // убираем после падения
  }, 5000);
}

setInterval(() => {
  createFallingImage("beer.png", "20%");
  createFallingImage("vodka.png", "60%");
}, 4000);
