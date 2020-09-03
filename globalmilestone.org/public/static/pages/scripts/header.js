function onHamburgerClickFirst() {
  $('.hamburger,header,.hamburger_parent').addClass("xed");
  $(".hamburger_parent").off("click", onHamburgerClickFirst);
  $(".hamburger_parent").on("click", onHamburgerClickSecond);
}

function onHamburgerClickSecond() {
  $('.hamburger,header,.hamburger_parent').removeClass("xed");
  $(".hamburger_parent").off("click", onHamburgerClickSecond);
  $(".hamburger_parent").on("click", onHamburgerClickFirst);
}

$(function() {
    $(".hamburger_parent").on("click", onHamburgerClickFirst)
});
