function onHamburgerClickFirst() {
  $('.hamburger,header').addClass("xed");
  $(".hamburger_link").off("click", onHamburgerClickFirst);
  $(".hamburger_link").on("click", onHamburgerClickSecond);
}

function onHamburgerClickSecond() {
  $('.hamburger,header').removeClass("xed");
  $(".hamburger_link").off("click", onHamburgerClickSecond);
  $(".hamburger_link").on("click", onHamburgerClickFirst);
}

$(function() {
    $(".hamburger_link").on("click", onHamburgerClickFirst);
});
