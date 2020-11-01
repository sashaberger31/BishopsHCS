function oneScroll() {
  //alert($('#mission').offset() - window.innerHeight)
         if ($(window).scrollTop() >= $('.mission').offset().top - .80*window.innerHeight) {
            $(window).off('scroll',oneScroll);
            $(window).on('scroll',twoScroll);
            setTimeout(function(){
            $('.1_slide_3,.mission').addClass("posed");
          }, 100);


            setTimeout(function(){
            $('.1_slide_2').addClass("posed");
          }, 210);

            setTimeout(function(){
            $('.1_slide_1').addClass("posed");
          }, 330);
         }
     }

function twoScroll() {
              if ($(window).scrollTop() >= $('.works').offset().top - .80*window.innerHeight) {


                  $(window).off('scroll',twoScroll);
                  $(window).on('scroll',threeScroll);

                 setTimeout(function(){
                 $('.2_slide_3,.works').addClass("posed");
               }, 100);


                 setTimeout(function(){
                 $('.2_slide_2').addClass("posed");
               }, 210);

                 setTimeout(function(){
                 $('.2_slide_1').addClass("posed");
               }, 330);
              }
          }

function threeScroll() {
              if ($(window).scrollTop() >= $('.final_wrapper').offset().top - .80*window.innerHeight) {

                  $(window).off('scroll',threeScroll);
                 setTimeout(function(){
                 $('.3_slide_3,.final').addClass("posed");
               }, 100);


                 setTimeout(function(){
                 $('.3_slide_2').addClass("posed");
               }, 210);

                 setTimeout(function(){
                 $('.3_slide_1').addClass("posed");
               }, 330);
              }
          }


$(function(){


  $(window).on('scroll', oneScroll);
  if ($(window).scrollTop() >= $('.mission').offset().top - .80*window.innerHeight) {
     $(window).off('scroll', oneScroll);
     $(window).on('scroll', twoScroll);

     setTimeout(function(){
     $('.1_slide_3,.mission').addClass("posed");
   }, 100);


     setTimeout(function(){
     $('.1_slide_2').addClass("posed");
   }, 210);

     setTimeout(function(){
     $('.1_slide_1').addClass("posed");
   }, 330);
  }

  if ($(window).scrollTop() >= $('.works').offset().top - .80*window.innerHeight) {
          $(window).off('scroll',twoScroll);
          $(window).on('scroll',threeScroll);
          setTimeout(function(){
          $('.2_slide_3,.works').addClass("posed");
        }, 100);


          setTimeout(function(){
          $('.2_slide_2').addClass("posed");
        }, 210);

          setTimeout(function(){
          $('.2_slide_1').addClass("posed");
        }, 330);

      }
      if ($(window).scrollTop() >= $('.final_wrapper').offset().top - .80*window.innerHeight) {

          $(window).off('scroll',threeScroll);
         setTimeout(function(){
         $('.3_slide_3,.final').addClass("posed");
       }, 100);


         setTimeout(function(){
         $('.3_slide_2').addClass("posed");
       }, 210);

         setTimeout(function(){
         $('.3_slide_1').addClass("posed");
       }, 330);
      }

});
