// Demo only: every button shows a note. Nothing is sent, stored or remembered.
(function () {
  "use strict";
  var note = document.getElementById("demo-note");
  var buttons = document.querySelectorAll("[data-demo]");
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function () {
      note.hidden = false;
    });
  }
  var email = document.getElementById("email");
  email.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      note.hidden = false;
    }
  });
})();
