(function () {
  "use strict";
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var q = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };

  /* Scroll-linked values: background drift and footer wordmark rise (desktop only, no motion if reduced). */
  var ftr = d.querySelector(".ftr");
  var fb = d.querySelector(".fbig");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY || 0;
    if (ftr && fb) {
      var r = ftr.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = Math.max(0, Math.min(1, (vh - r.top) / (vh + r.height)));
      fb.style.setProperty("--fy", ((1 - p) * 70).toFixed(1));
    }
    ticking = false;
  }
  if (!reduce) {
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
    }, { passive: true });
    onScroll();
  }


  /* Blog search: filters the already-rendered list, so every article stays crawlable. */
  var bq = d.querySelector("[data-blog-filter]");
  if (bq) {
    var rows = q("[data-blog-list] li[data-t]");
    var cats = q("[data-blog-list] .bcat");
    var cnt = d.querySelector("[data-blog-count]");
    bq.addEventListener("input", function () {
      var v = bq.value.trim().toLowerCase(), n = 0;
      rows.forEach(function (r) { var m = !v || r.getAttribute("data-t").indexOf(v) > -1; r.hidden = !m; if (m) n++; });
      cats.forEach(function (c) { c.hidden = !q("li[data-t]:not([hidden])", c).length; });
      if (cnt) cnt.textContent = v ? n + (n === 1 ? " article found" : " articles found") : "";
    });
  }

  if (!("IntersectionObserver" in window)) return;

  /* Staggered blur-to-sharp reveal for cards. Content stays visible if this script fails. */
  var sel = ".pcard,.st li,.cols3>div,.frow,.dlist li,.glist li,.faq details,.ps-list li,.next,.plink li,.xrow";
  var items = q(sel).filter(function (el) { return !el.closest(".env,.arc"); });
  root.classList.add("skin-ready");
  if (reduce) {
    items.forEach(function (el) { el.classList.add("sk", "sk-in"); });
    if (ftr) ftr.classList.add("f-in");
    return;
  }
  var groups = new Map();
  items.forEach(function (el) {
    var p = el.parentElement;
    var i = groups.get(p) || 0;
    groups.set(p, i + 1);
    el.style.setProperty("--sd", Math.min(i, 6) * 90 + "ms");
    el.classList.add("sk");
  });
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("sk-in"); io.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  items.forEach(function (el) { io.observe(el); });

  /* Footer columns settle into place. */
  if (ftr) {
    var fo = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) { ftr.classList.add("f-in"); fo.disconnect(); }
    }, { threshold: 0.15 });
    fo.observe(ftr);
  }
})();
