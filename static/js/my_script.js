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



// スプラッシュの表示回数制限（一日３回まで）

document.addEventListener("DOMContentLoaded",() =>{
  const splash = document.getElementById("splash_container");
  const maxViews = 3;// 1日3回まで
  const today = new Date().toString();// 今日の日付を文字列にする


  const lastShowDate = localStorage.getItem("splashLastShowDate");
  let viewCount = parseInt(localStorage.getItem("splashViewCount")||0);

//次の日になったら更新
  if (lastShowDate !== today){
    viewCount = 0;
    localStorage.setItem("splashLastShowDate",today);
  }
//３回未満なら表示
  if (viewCount <= maxViews){
      splash.style.display = "block";
      localStorage.setItem("splashViewCount", viewCount + 1);
    } else {
      splash.style.display = "none";
  }
})