import re, os, sys, html, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from places_data import UK, CA

SITE = os.environ.get('SITE', '../site')
PUB = os.environ.get('PUB', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'published.json'))
BASE = 'https://wizzocodes.com'
DATE = '2026-11-02'

def esc(s): return html.escape(s, quote=True)
def rd(p): return open(os.path.join(SITE, p), encoding='utf-8').read()
def wr(p, s):
    os.makedirs(os.path.dirname(os.path.join(SITE, p)), exist_ok=True)
    open(os.path.join(SITE, p), 'w', encoding='utf-8').write(s)

titles = {p['slug']: p['title'] for p in json.load(open(PUB))}
TPL2 = rd('blog/iptv-on-fire-tv/index.html')   # depth 2 template
TPL1 = rd('blog/index.html')                    # depth 1 template
CTA = {2: re.search(r'<section class="cta">.*?</section>', TPL2, re.S).group(0),
       1: re.search(r'<section class="cta">.*?</section>', TPL1, re.S).group(0)}

def h1_html(text, color):
    ws = text.split(); out = []
    for i, w in enumerate(ws):
        inner = '<span class="ac %s">%s</span>' % (color, esc(w)) if i == len(ws) - 1 else '<span>%s</span>' % esc(w)
        out.append('<span class="w" style="--i:%d">%s</span>' % (i, inner))
    return ' '.join(out)

def head(tpl, tpl_url, url, title, desc, kws, lang, alts, crumbs, name, extra_type='WebPage'):
    h = tpl
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(title), h, 1)
    for pat in (r'(<meta name="description" content=")[^"]*', r'(<meta property="og:description" content=")[^"]*', r'(<meta name="twitter:description" content=")[^"]*'):
        h = re.sub(pat, lambda m: m.group(1) + esc(desc), h, 1)
    for pat in (r'(<meta property="og:title" content=")[^"]*', r'(<meta name="twitter:title" content=")[^"]*'):
        h = re.sub(pat, lambda m: m.group(1) + esc(title), h, 1)
    h = re.sub(r'(<meta name="keywords" content=")[^"]*', lambda m: m.group(1) + esc(kws), h, 1)
    h = h.replace(tpl_url, url)
    h = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*', '', h)
    tags = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % a for a in alts)
    h = h.replace('<link rel="canonical" href="%s">' % url, '<link rel="canonical" href="%s">%s' % (url, tags), 1)
    h = h.replace('<html lang="en-GB">', '<html lang="%s">' % lang, 1)
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "/#org", "name": "Wizzo Codes", "url": BASE + "/", "logo": BASE + "/icon-512.png",
         "contactPoint": {"@type": "ContactPoint", "telephone": "+447392924862", "contactType": "customer support", "availableLanguage": "English"}},
        {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#website", "name": "Wizzo Codes", "url": BASE + "/", "publisher": {"@id": BASE + "/#org"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items},
        {"@context": "https://schema.org", "@type": extra_type, "name": name, "url": url, "description": desc, "inLanguage": lang, "isPartOf": {"@id": BASE + "/#website"}, "dateModified": DATE}]
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>', h, 1, flags=re.S)
    return h

def place_page(pl, kind, n):
    uk = kind == 'uk'
    hubname = 'UK cities' if uk else 'Canada'
    hubpath = '/uk/' if uk else '/ca/'
    nm = pl['name']
    url = '%s%s%s/' % (BASE, hubpath, pl['slug'])
    title = 'IPTV Subscription in %s | Wizzo Codes' % nm
    desc = ('IPTV in %s: %s. Plans from £4 with WhatsApp support.' % (nm, pl['hook']))
    if len(desc) > 160: desc = desc[:157].rsplit(' ', 1)[0] + '...'
    kws = 'IPTV %s, best IPTV in %s, IPTV subscription %s, IPTV %s' % (nm, nm, nm, 'UK' if uk else 'Canada')
    lang = 'en-GB' if uk else 'en-CA'
    alts = [('en-gb' if uk else 'en-ca', url)]
    crumbs = [('Home', BASE + '/'), (hubname, BASE + hubpath), (nm, url)]
    h = head(TPL2, BASE + '/blog/iptv-on-fire-tv/', url, title, desc, kws, lang, alts, crumbs, 'IPTV in ' + nm)
    guides = ''.join('<li><a href="../../blog/%s/">%s</a></li>' % (g, esc(titles[g])) for g in pl['guides'] if g in titles)
    country = 'the UK' if uk else 'Canada'
    cur = ('Prices are in pounds sterling and are totals for the length you choose.' if uk else
           'Prices are shown in pounds sterling, so your payment method converts from Canadian dollars. Check the final amount before you confirm.')
    secs = [
      ('Choosing IPTV in %s' % nm, [pl['intro'], 'People searching for the best IPTV in %s usually want the same few things: a service that works on their own device, stays steady in the evening, comes with honest support and has clear terms. What counts as best depends on your home, your screen and your connection, so we do not claim it for ourselves. Instead, we encourage you to test any service, ours included, on your own setup before you commit.' % nm]),
      ('Streaming at home in %s' % nm, [pl['home']]),
      ('Sport and viewing in %s' % nm, [pl['sport']]),
      ('A practical tip for %s viewers' % nm, [pl['tip']]),
      ('How Wizzo Codes works for %s viewers' % nm,
        ['Wizzo Codes is an online service. We do not have an office or a shop in %s, and everything happens over WhatsApp and the internet. You choose a plan and a length, request a free trial if you wish, receive your sign-in details privately and install a player app on your device. %s Plans start from £4 for one month. See the <a href="../../plans/">plans page</a> and <a href="../../how-it-works/">how it works</a>.' % (nm, cur),
         'You are responsible for making sure that what you watch is lawful for you to view where you live. We are independent and not affiliated with any broadcaster, league or device maker.'])]
    toc = ''.join('<li><a href="#s%d">%s</a></li>' % (i, esc(t)) for i, (t, _) in enumerate(secs))
    body = ''.join('<h2 id="s%d">%s</h2>%s' % (i, esc(t), ''.join('<p>%s</p>' % (p if '<a ' in p else esc(p)) for p in ps)) for i, (t, ps) in enumerate(secs))
    main = ('<main id="main"><section class="phead"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a> / <a href="../">%s</a> / <span aria-current="page">%s</span></nav>'
            '<p class="eyebrow">IPTV in %s</p><h1 class="rvw">%s</h1><p class="lead">%s</p></div></section>'
            '<section class="sec "><div class="wrap" data-reveal><div class="prose-wrap"><nav class="toc" aria-label="On this page"><p>On this page</p><ul>%s</ul></nav><div class="prose">%s</div></div>'
            '<aside class="next"><h2>Helpful guides</h2><ul>%s</ul><p>Back to <a href="../">IPTV in %s</a>, or <a href="../../contact/">ask a question on WhatsApp</a>.</p></aside></div></section>%s</main>') % (
        esc(hubname), esc(nm), esc(pl['nation']), h1_html('IPTV in ' + nm, 'bgm'[n % 3]), esc(desc), toc, body, guides, 'UK cities' if uk else 'Canada', CTA[2])
    h = re.sub(r'<main id="main">.*?</main>', lambda m: main, h, 1, flags=re.S)
    wr('%s/%s/index.html' % (hubpath.strip('/'), pl['slug']), h)
    return len(re.findall(r"[A-Za-z0-9£']+", re.sub(r'<[^>]+>', ' ', body)))

def hub(kind):
    uk = kind == 'uk'
    items = UK if uk else CA
    path = '/uk/' if uk else '/ca/'
    url = BASE + path
    if uk:
        title = 'IPTV in UK Cities: Local Setup Tips, Plans from £4 | Wizzo Codes'
        desc = 'IPTV subscription tips for 20 UK cities, from London to Belfast: home Wi-Fi advice, sport viewing and a free trial. Plans from £4 with WhatsApp support.'
        h1 = 'IPTV across UK cities.'
        alts = [('en-gb', url)]
        crumbs = [('Home', BASE + '/'), ('UK cities', url)]
        lang = 'en-GB'
        lead = 'Where you live changes how you stream: the age of your building, your broadband and the sport you follow. Pick your city for practical, specific advice.'
        intro = ['Wizzo Codes is an online IPTV subscription service for viewers across the UK, with plans from £4 for one month. We do not have local offices, and these pages do not claim any. Each city page covers the housing, Wi-Fi and viewing questions that matter locally, and links to plain-English guides.']
    else:
        title = 'IPTV Subscription in Canada: Free Trial, Plans in GBP | Wizzo Codes'
        desc = 'IPTV subscription for Canadian viewers: devices, time zones, data caps and payment in pounds sterling, plus city guides and a free trial on request.'
        h1 = 'IPTV subscription for Canadian viewers.'
        alts = [('en-ca', url), ('en-gb', BASE + '/'), ('x-default', BASE + '/')]
        crumbs = [('Home', BASE + '/'), ('Canada', url)]
        lang = 'en-CA'
        lead = 'We serve viewers in Canada as well as the UK. Here is what to check about devices, time zones, data caps and payment before you subscribe.'
        intro = ['Our main market is the UK, and we also serve customers in Canada. Plans start from £4 for one month. Prices are shown in pounds sterling, so your payment method converts the amount from Canadian dollars. You can pay with PayPal, Binance Pay or Wise, and we offer a free trial on request so that you can test on your own connection.',
                 'Before you subscribe, check these four things: your device and system version (see our compatible devices page), the stability of your internet at your usual viewing time, any data cap on your plan, and your device time zone so that the programme guide matches your local time. You are responsible for making sure that what you watch is lawful in your province.']
    cards = ''.join('<li data-t="%s"><span class="cat">%s</span><div><h3><a href="%s/">IPTV in %s</a></h3><p>%s</p></div><span class="rt">%s</span><span class="go"><svg class="arr" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></li>' % (
        esc(p['name'].lower()), esc(p['nation']), p['slug'], esc(p['name']), esc(p['hook'][0].upper() + p['hook'][1:] + '.'), esc(p['nation'])) for p in items)
    h = head(TPL1, BASE + '/blog/', url, title, desc, 'IPTV subscription ' + ('UK cities, best IPTV UK' if uk else 'Canada, IPTV Canada, best IPTV in Canada'), lang, alts, crumbs, h1.rstrip('.'), 'CollectionPage')
    blogcards = ''
    related = ['iptv-uk-broadband-guide', 'uk-tv-licence-and-iptv', 'iptv-for-live-sports-tips'] if uk else ['canadian-broadband-for-iptv', 'iptv-in-canada-what-to-know', 'canada-time-zones-and-live-guides', 'iptv-payment-and-currency-canada']
    rel = ''.join('<li><a href="../blog/%s/">%s</a></li>' % (g, esc(titles[g])) for g in related if g in titles)
    main = ('<main id="main"><section class="phead"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> / <span aria-current="page">%s</span></nav><p class="eyebrow">%s</p>'
            '<h1 class="rvw">%s</h1><p class="lead">%s</p></div></section>'
            '<section class="sec "><div class="wrap" data-reveal><div class="prose" style="max-width:68ch;margin:0 auto 2.5rem">%s</div><h2 class="sr">Choose your city</h2><ul class="glist">%s</ul>'
            '<aside class="next"><h2>Related guides</h2><ul>%s</ul></aside></div></section>%s</main>') % (
        'UK cities' if uk else 'Canada', 'IPTV by city' if uk else 'IPTV in Canada', h1_html(h1, 'b'), esc(lead), ''.join('<p>%s</p>' % esc(p) for p in intro), cards, rel, CTA[1])
    h = re.sub(r'<main id="main">.*?</main>', lambda m: main, h, 1, flags=re.S)
    wr(path.strip('/') + '/index.html', h)

counts = {}
for n, p in enumerate(UK): counts['uk/' + p['slug']] = place_page(p, 'uk', n)
for n, p in enumerate(CA): counts['ca/' + p['slug']] = place_page(p, 'ca', n)
hub('uk'); hub('ca')

# footer links, footer sentence and hreflang on the home page
for f in glob.glob(SITE + '/**/*.html', recursive=True):
    h = open(f, encoding='utf-8').read(); o = h
    m = re.search(r'<li><a href="([^"]*)plans/">IPTV plans</a></li>', h)
    if m and 'IPTV in UK cities' not in h:
        pre = m.group(1)
        h = h.replace('<li><a href="%sfaq/">FAQ</a></li>' % pre, '<li><a href="%sfaq/">FAQ</a></li><li><a href="%suk/">IPTV in UK cities</a></li><li><a href="%sca/">IPTV in Canada</a></li>' % (pre, pre, pre), 1)
    h = h.replace('IPTV subscription plans for the United Kingdom. Free trial', 'IPTV subscription plans for the United Kingdom and Canada. Free trial')
    if f.endswith('/site/index.html') or os.path.abspath(f) == os.path.abspath(SITE + '/index.html'):
        if 'hreflang="en-ca"' not in h:
            h = h.replace('<link rel="alternate" hreflang="x-default" href="https://wizzocodes.com/">', '<link rel="alternate" hreflang="en-ca" href="https://wizzocodes.com/ca/"><link rel="alternate" hreflang="x-default" href="https://wizzocodes.com/">', 1)
    if h != o: open(f, 'w', encoding='utf-8').write(h)

# sitemap
sm = rd('sitemap.xml')
sm = re.sub(r'<url><loc>https://wizzocodes\.com/(?:uk|ca)/[^<]*</loc><lastmod>[^<]*</lastmod></url>\n?', '', sm)
urls = ['<url><loc>%s/%s/</loc><lastmod>%s</lastmod></url>' % (BASE, x, DATE) for x in ['uk', 'ca'] + sorted(counts)]
sm = sm.replace('</urlset>', '\n'.join(urls) + '\n</urlset>')
wr('sitemap.xml', sm)
print('places', len(counts), 'words min %d max %d avg %d' % (min(counts.values()), max(counts.values()), sum(counts.values()) / len(counts)))
