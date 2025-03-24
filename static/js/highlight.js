document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".section");
    let index = 0;
    let isScrolling = false;

    const scrollToSection = (index) => {
        window.scrollTo({
            top: sections[index].offsetTop,
            behavior: "smooth"
        });
    };

    window.addEventListener("wheel", (event) => {
        event.preventDefault(); // スクロール無効化
        if (isScrolling) return;
        isScrolling = true;

        if (event.deltaY > 0) {
            index = Math.min(index + 1, sections.length - 1);
        } else {
            index = Math.max(index - 1, 0);
        }

        scrollToSection(index);
        
        setTimeout(() => { isScrolling = false; }, 1000);
    }, { passive: false }); // `passive: false` を指定して `preventDefault()` を適用
});


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
  