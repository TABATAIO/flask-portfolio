$(function () {
    $('a[href^="#"]').click(function () {
      var href = $(this).attr("href");
      var target = $(href == "#" || href == "" ? "html" : href);
      var position = target.offset().top;
      var speed = 500;
      $("html, body").animate(
        {
          scrollTop: position,
        },
        speed,
        "swing"
      );
      return false;
    });
  });
  
var bar = new ProgressBar.Path('#namelogo', {
    easing: 'easeInOut',
    duration: 3000
  });

$(window).on('load',function(){
  $('.splash_container').delay(3500).fadeOut('slow');
})
  



bar.set(0);
bar.animate(-1.0);  