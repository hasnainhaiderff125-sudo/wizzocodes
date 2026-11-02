# Wizzo Codes: round 1 report

Scope of this round: design and performance fixes, the full blog system, 29 new articles (39 published in total), technical SEO clean-up, and the planning documents. The 100+ article target is a multi-batch job: 39 are live, 75 more are planned in `blog-plan.md`.

## 1. Website improvements
- Headings are bold (700) with tighter spacing; the italic serif accent word and light canvas from the re-skin remain.
- Cards are now solid white with a clear 1px border and 16px radius instead of frosted glass. Backdrop blur was removed everywhere.
- Text contrast measured against the darkest canvas tone: body 7.1:1, secondary text 5.6:1, footer links 14.1:1 (WCAG AA needs 4.5:1).
- Footer watermark is now a tone-on-tone navy at low opacity on the canvas, cropped at the bottom, readable on desktop and mobile.
- Fixed a contrast bug: the "Select Premium" button was navy on navy.
- Navigation label "Guides" is now "Blog".

## 2. Bugs fixed
- Premium plan button was invisible (navy on navy).
- My first re-skin build had backdrop blur on about 13 surfaces and updated a root CSS variable on every scroll frame. Both caused a large scroll slowdown in testing (about 3x frame time at 4x CPU throttle) and are removed.
- A CSS line mangled during that clean-up silently broke most of the skin; found by screenshot and fixed. The stylesheet now has balanced braces and was re-measured.
- Pricing note link under the plans was left-aligned; page-head intro text was misaligned. Both centred.
- Search on the blog missed "Wi-Fi" when typing "wifi"; fixed.

## 3. Responsive
Tested all 52 pages at 320, 360, 375, 390, 414, 430, 480, 768, 820, 1024, 1280, 1366, 1440, 1600 and 1920 wide: zero horizontal overflow, zero JavaScript errors. Mobile menu, plan switcher, FAQ accordions and blog search were exercised in a browser.

## 4. Performance
Measured with Lighthouse 12 (local server, Lighthouse's simulated throttling) and a frame-time test while scrolling (4x CPU throttle, headless Chromium):

| Page | Perf | A11y | Best practices | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| Original home, mobile | 95 | 100 | 100 | 100 | 2.2 s | 0 | 190 ms |
| New home, mobile | 97 | 100 | 100 | 100 | 2.6 s | 0.001 | 40 ms |
| New article, mobile | 98 | 100 | 100 | 100 | 2.1 s | 0.001 | 80 ms |
| New home, desktop | 100 | 100 | 100 | 100 | 0.6 s | 0.001 | 0 ms |

- The mobile home LCP (2.6 s) is just over the 2.5 s target in this run; the original was 2.2 s. Worth re-checking on your live host.
- Scroll frame time on the new home page is level with the original (about 28 ms vs 30 ms average at 4x throttle). I could not reproduce your laptop lag directly. In isolation tests, box shadows and the large section entrance animation were the most expensive items, so shadows are lighter and the big section scale animation is switched off.
- The scroll-linked background drift now runs on the browser's scroll timeline (no JavaScript per frame).
- Not measured: INP (needs real interactions on real devices), and real-device laptop performance.

## 5. Animations
All existing animations are kept (hero card float, word-by-word headline reveal, plan switcher, envelope FAQ carousel, device arc). Added: staggered blur-in on cards, and the footer settle. All respect reduced motion and stay visible if JavaScript fails.

## 6. SEO
- `/guides/` moved to `/blog/` with 301 redirects (`_redirects`), canonicals, breadcrumbs, schema and the sitemap all updated.
- Checked across all 53 HTML pages: unique title, description and H1 on every page; one H1 per page; every canonical is the page's own HTTPS URL with trailing slash; all JSON-LD parses; no broken internal links; the sitemap (52 URLs) matches the real pages exactly.
- Each article has BlogPosting and BreadcrumbList schema, a table of contents, related articles, publish date and reading time.
- No FAQPage or review schema was added (the site has no qualifying content and no reviews).
- robots.txt already allows everything and points to the sitemap.

## 7. Blog
**114 articles are live** (10 earlier guides plus 104 new, written in two batches). Full list: `blog-plan.md`.
- Honest depth note: the 104 new articles average about 245 words (shortest about 150, longest about 630). Each answers one focused question with practical steps, but this is shorter than the 800 to 1,500 words in your brief. If you want ranking depth, the best next step is a depth pass: pick the 20 articles that match your highest value searches and expand them to 800+ words with more examples. I would rather you decide that than have me pad.
- The blog has category chips (14 categories), search that ignores hyphens, featured articles, table of contents, related articles and article plus breadcrumb schema.
- No featured images were added (no real photos available; no stock or generated filler).

## 8. International SEO
- **UK (primary):** /uk/ hub plus 20 city pages (London, Manchester, Birmingham, Leeds, Liverpool, Glasgow, Edinburgh, Bristol, Sheffield, Nottingham, Leicester, Newcastle, Cardiff, Coventry, Bradford, Southampton, Oxford, Cambridge, Brighton, Belfast). Each city page is 310 to 410 words with its own housing, Wi-Fi, sport and tip content.
- **Canada (secondary):** /ca/ landing page plus 6 city pages (Toronto, Montreal, Vancouver, Calgary, Edmonton, Ottawa).
- **hreflang:** the home page (en-GB) and /ca/ (en-CA) point to each other, with x-default on the home page. City pages are self-referencing only, because they have no counterpart.
- **No false claims:** every city page says plainly that Wizzo Codes is an online service with no office in that city, and none claims local reviews or local service.
- **"Best IPTV in <city>":** this phrase appears in each page body and keywords, framed honestly (what "best" depends on). It is not in titles, because an unqualified "best" cannot be proved.
- Prices stay in pounds sterling. The Canada pages say so and explain the conversion at payment.

## 9. Backlinks
`backlink-strategy.md`.

## 10. Testing results
- Site audit across **156 HTML pages**: 0 issues. Unique title, description and H1 on every page; one H1 each; every canonical is the page's own URL; all structured data parses; no broken internal links; sitemap (155 URLs) matches the pages exactly.
- Overflow sweep: 11 representative pages (home, plans, FAQ, blog index, two articles, both hubs, three city pages) at 15 widths from 320 to 1920: 0 failures. An earlier sweep covered all 52 pages that existed then.
- Lighthouse (mobile, local server): home 97 (repeat runs; one cold run scored 76, an outlier), UK city page 98, Canada hub 98, blog index 94 to 98, article 98; accessibility 98 to 100 (a heading-order warning was found and fixed); best practices 100; SEO 100. Largest contentful paint ran 2.1 to 2.8 s, so the 2.5 s target is borderline on the home page and blog index in this environment.
- Behaviour tests passed: mobile menu, plan switcher, FAQ, blog search, reduced motion, no-JS rendering.
- Not tested: real devices, Safari and Firefox, a live host, INP, sending messages through the WhatsApp links.

## 11. Deployment
1. Deploy the contents of the `site/` folder to your current host, the same way you deployed before (the `_headers` and `_redirects` files are used by Netlify and Cloudflare Pages style hosts; no build step is needed).
2. Check `https://wizzocodes.com/guides/iptv-on-fire-tv/` redirects to `/blog/iptv-on-fire-tv/`.
3. In Google Search Console, resubmit `https://wizzocodes.com/sitemap.xml` and inspect `/blog/` and two articles.
4. Asset versions are `?v=3` for skin files; bump the number whenever you change them.
5. To add articles later: add them to `tools/articles_*.py`, open a terminal inside the `tools/` folder and run `python3 build_blog.py`, then `python3 build_places.py`, then `python3 qa.py` (the builders regenerate the blog index, related links, city pages and sitemap).

## Open decisions for you
- Do you want a depth pass on your top 20 articles (800+ words each)?
- Which extra cities should come next (UK and Canada)?
- Do you want a dedicated Canada plan or price page, or is GBP pricing with a conversion note enough?
