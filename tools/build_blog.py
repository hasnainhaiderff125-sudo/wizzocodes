import re, os, sys, html, glob, json
sys.path.insert(0, os.path.dirname(__file__))
from articles_b1 import A as NEW1
from articles_b2a import A as NEW2a
from articles_b2b import A as NEW2b
from articles_b2c import A as NEW2c
NEW = NEW1 + NEW2a + NEW2b + NEW2c
B1 = set(a['slug'] for a in NEW1)
from articles_b1_extra import X as EXTRA
from articles_b2_extra1 import X as E1
from articles_b2_extra2 import X as E2
from articles_b2_extra3 import X as E3
EXTRA = dict(EXTRA); EXTRA.update(E1); EXTRA.update(E2); EXTRA.update(E3)

SITE = '../site'
BASE = 'https://wizzocodes.com'
TODAY = '2026-11-02'
import datetime
def longdate(d):
    x = datetime.date.fromisoformat(d); return '%d %s %d' % (x.day, x.strftime('%B'), x.year)

CATMAP = {'The basics': 'IPTV for Beginners', 'Devices and setup': 'IPTV Setup & Installation',
          'Troubleshooting': 'IPTV Troubleshooting', 'Buying advice': 'IPTV Subscription Guides',
          'Safety and privacy': 'IPTV Security & Privacy'}
CAT_ORDER = ['IPTV for Beginners', 'IPTV Setup & Installation', 'IPTV Devices', 'IPTV Applications',
             'IPTV Troubleshooting', 'IPTV Sports', 'IPTV Features & Technology', 'IPTV Subscription Guides',
             'IPTV Comparisons', 'IPTV Streaming Quality', 'IPTV Security & Privacy', 'IPTV UK Guides',
             'IPTV Canada Guides', 'IPTV FAQs']

def esc(s): return html.escape(s, quote=True)
def rd(p): return open(os.path.join(SITE, p), encoding='utf-8').read()
def wr(p, s):
    os.makedirs(os.path.dirname(os.path.join(SITE, p)), exist_ok=True)
    open(os.path.join(SITE, p), 'w', encoding='utf-8').write(s)

# ---- existing posts (moved guides) ----
existing = []
for d in sorted(glob.glob(SITE + '/blog/*/index.html')):
    slug = d.split('/')[-2]
    h = open(d, encoding='utf-8').read()
    if 'data-gen="1"' in h:
        continue
    eb = re.search(r'class="eyebrow">([^<]*)', h).group(1)
    cat = CATMAP.get(eb, eb)
    title = html.unescape(re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S).group(1))
    title = html.unescape(re.sub(r'<[^>]+>', '', title))
    desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    mins = int(re.search(r'(\d+) min read', h).group(1))
    if eb in CATMAP:
        h = h.replace('class="eyebrow">%s<' % eb, 'class="eyebrow">%s<' % cat)
        open(d, 'w', encoding='utf-8').write(h)
    existing.append(dict(slug=slug, title=title, desc=desc, cat=cat, mins=mins, date='2026-10-14', kw='', kw2=[], gen=False))

# template pieces from an existing page
TPL = rd('blog/iptv-on-fire-tv/index.html')
CTA = re.search(r'<section class="cta">.*?</section>', TPL, re.S).group(0)

def link(s, slug_self):
    m = {'plans': '../../plans/', 'devices': '../../compatible-devices/', 'howitworks': '../../how-it-works/',
         'faq': '../../faq/', 'contact': '../../contact/'}
    names = {'plans': 'plans page', 'devices': 'compatible devices page', 'howitworks': 'how it works',
             'faq': 'FAQ', 'contact': 'contact page'}
    allslugs = {p['slug']: p for p in existing + NEWP}
    def rep(mo):
        k = mo.group(1)
        if k.startswith('post:'):
            sl = k[5:]
            if sl not in allslugs: raise SystemExit('BAD LINK %s in %s' % (sl, slug_self))
            return '<a href="../%s/">%s</a>' % (sl, esc(allslugs[sl]['title']))
        if k in m:
            return '<a href="%s">%s</a>' % (m[k], names[k])
        raise SystemExit('BAD TOKEN %s' % k)
    return re.sub(r'\{([a-z:\-0-9]+)\}', rep, s)

def words(t): return len(re.findall(r"[A-Za-z0-9£']+", re.sub(r'<[^>]+>', ' ', t)))
def slugify(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

NEWP = []
def p_slug_in_b1(a): return a['slug'] in B1
for a in NEW:
    p = dict(a); p['gen'] = True; p['date'] = '2026-11-01' if p_slug_in_b1(a) else TODAY
    ex = EXTRA.get(p['slug'], [])
    p['sections'] = list(p['sections'][:-1]) + ex + [p['sections'][-1]]
    NEWP.append(p)

# validate content rules
errs = []
slugs = set(p['slug'] for p in existing)
for p in NEWP:
    if p['slug'] in slugs: errs.append('dup slug ' + p['slug'])
    slugs.add(p['slug'])
    if p['cat'] not in CAT_ORDER: errs.append('bad cat %s %s' % (p['slug'], p['cat']))
    if len(p['desc']) > 160: errs.append('desc long %s %d' % (p['slug'], len(p['desc'])))
    blob = p['title'] + p['desc'] + p['lead'] + json.dumps(p['sections'])
    if '\u2014' in blob or '\u2013' in blob: errs.append('dash in ' + p['slug'])

# body building + reading time
for p in NEWP:
    body = '<p>%s</p>\n' % link(esc(p['lead']).replace('&#x27;', "'"), p['slug']) if False else ''
    toc = []; parts = []
    for h2, paras in p['sections']:
        sid = slugify(h2)
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, esc(h2)))
        parts.append('<h2 id="%s">%s</h2>' % (sid, esc(h2)))
        for q in paras:
            if isinstance(q, tuple):
                parts.append('<ul class="ticks">' + ''.join('<li>%s</li>' % link(esc(i), p['slug']) for i in q[1]) + '</ul>')
            else:
                parts.append('<p>%s</p>' % link(q if '<' in q else esc(q), p['slug']))
    p['toc'] = ''.join(toc)
    p['body'] = '<p>%s</p>\n' % link(esc(p['lead']), p['slug']) + '\n'.join(parts)
    p['mins'] = max(2, round(words(p['body']) / 200))
    p['words'] = words(p['body'])

allp = existing + NEWP

# related: same category first, then keyword overlap
def toks(p): return set(re.findall(r'[a-z0-9]+', (p['title'] + ' ' + p.get('kw', '') + ' ' + ' '.join(p.get('kw2', []))).lower())) - {'iptv', 'to', 'the', 'a', 'and', 'for', 'of', 'in', 'on', 'with', 'what', 'is', 'how'}
for p in NEWP:
    sc = []
    for q in allp:
        if q['slug'] == p['slug']: continue
        s = (3 if q['cat'] == p['cat'] else 0) + len(toks(p) & toks(q))
        sc.append((-s, q['slug']))
    sc.sort()
    p['related'] = [x[1] for x in sc[:3]]
bytitle = {p['slug']: p for p in allp}

def head_for(p):
    h = TPL
    url = '%s/blog/%s/' % (BASE, p['slug'])
    title = '%s | Wizzo Codes' % p['title']
    kws = ', '.join([p['kw']] + p['kw2'])
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(title), h, 1)
    h = re.sub(r'(<meta name="description" content=")[^"]*', r'\g<1>' + esc(p['desc']).replace('\\', ''), h, 1)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*', r'\g<1>' + esc(p['desc']), h, 1)
    h = re.sub(r'(<meta name="twitter:description" content=")[^"]*', r'\g<1>' + esc(p['desc']), h, 1)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', r'\g<1>' + esc(title), h, 1)
    h = re.sub(r'(<meta name="twitter:title" content=")[^"]*', r'\g<1>' + esc(title), h, 1)
    h = re.sub(r'(<meta name="keywords" content=")[^"]*', r'\g<1>' + esc(kws), h, 1)
    h = h.replace('https://wizzocodes.com/blog/iptv-on-fire-tv/', url)
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "/#org", "name": "Wizzo Codes", "url": BASE + "/", "logo": BASE + "/icon-512.png",
         "contactPoint": {"@type": "ContactPoint", "telephone": "+447392924862", "contactType": "customer support", "availableLanguage": "English", "areaServed": "GB"}, "areaServed": "GB"},
        {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#website", "name": "Wizzo Codes", "url": BASE + "/", "inLanguage": "en-GB", "publisher": {"@id": BASE + "/#org"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p['title'], "item": url}]},
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p['title'], "description": p['desc'], "inLanguage": "en-GB",
         "datePublished": p['date'], "dateModified": p['date'], "articleSection": p['cat'], "wordCount": p['words'],
         "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "image": BASE + "/og-image.png",
         "author": {"@type": "Organization", "name": "Wizzo Codes", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "Wizzo Codes", "logo": {"@type": "ImageObject", "url": BASE + "/icon-512.png"}}}]
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>', h, 1, flags=re.S)
    return h

def h1_html(title, color):
    ws = title.split()
    out = []
    for i, w in enumerate(ws):
        inner = '<span class="ac %s">%s</span>' % (color, esc(w)) if i == len(ws) - 1 else '<span>%s</span>' % esc(w)
        out.append('<span class="w" style="--i:%d">%s</span>' % (i, inner))
    return ' '.join(out)

for n, p in enumerate(NEWP):
    h = head_for(p)
    rel = ''.join('<li><a href="../%s/">%s</a></li>' % (s, esc(bytitle[s]['title'])) for s in p['related'])
    main = ('<main id="main"><section class="phead" data-gen="1"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a> / <a href="../">Blog</a> / <span aria-current="page">%s</span></nav>'
            '<p class="eyebrow">%s</p><h1 class="rvw">%s</h1><p class="lead">%s</p>'
            '<p class="byline">By Wizzo Codes <span aria-hidden="true">|</span> Published %s <span aria-hidden="true">|</span> %d min read</p></div></section>'
            '<section class="sec "><div class="wrap" data-reveal><div class="prose-wrap"><nav class="toc" aria-label="On this page"><p>On this page</p><ul>%s</ul></nav>'
            '<div class="prose">%s</div></div>'
            '<aside class="next"><h2>Related articles</h2><ul>%s</ul><p>Ready to choose? See the <a href="../../plans/">plans from £4</a> or <a href="../../contact/">request a free trial on WhatsApp</a>. Back to the <a href="../">Wizzo Codes blog</a>.</p></aside></div></section>%s</main>') % (
        esc(p['title']), esc(p['cat']), h1_html(p['title'], 'bgm'[n % 3]), esc(p['desc']), longdate(p['date']), p['mins'], p['toc'], p['body'], rel, CTA)
    h = re.sub(r'<main id="main">.*?</main>', lambda m: main, h, 1, flags=re.S)
    wr('blog/%s/index.html' % p['slug'], h)

# ---- blog index ----
idx = rd('blog/index.html')
by = {}
for p in allp: by.setdefault(p['cat'], []).append(p)
chips = ''.join('<a class="chip" href="#c-%s">%s <span>%d</span></a>' % (slugify(c), esc(c), len(by[c])) for c in CAT_ORDER if c in by)
feat_slugs = ['how-iptv-works', 'iptv-vs-cable-tv', 'iptv-free-trial-what-to-test']
feat = ''.join('<a class="fcard" href="%s/"><span class="cat">%s</span><h3>%s</h3><p>%s</p><span class="rt">%d min read</span></a>' % (
    s, esc(bytitle[s]['cat']), esc(bytitle[s]['title']), esc(bytitle[s]['desc']), bytitle[s]['mins']) for s in feat_slugs if s in bytitle)
sections = []
for c in CAT_ORDER:
    if c not in by: continue
    rows = ''.join('<li data-t="%s"><span class="cat">%s</span><div><h3><a href="%s/">%s</a></h3><p>%s</p></div><span class="rt">%d min read</span><span class="go"><svg class="arr" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></li>' % (
        esc((lambda t: t + ' ' + t.replace('-', ''))((p['title'] + ' ' + p['desc'] + ' ' + p['cat'] + ' ' + p.get('kw', '')).lower())), esc(p['cat']), p['slug'], esc(p['title']), esc(p['desc']), p['mins']) for p in by[c])
    sections.append('<section class="bcat" id="c-%s"><h2>%s</h2><ul class="glist">%s</ul></section>' % (slugify(c), esc(c), rows))
main = ('<main id="main"><section class="phead"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> / <span aria-current="page">Blog</span></nav><p class="eyebrow">Blog</p>'
        '<h1 class="rvw">%s</h1><p class="lead">Plain-English help for before and after you subscribe, written for UK viewers. %d articles so far, with more added in regular batches.</p></div></section>'
        '<section class="sec "><div class="wrap" data-reveal><h2 class="sr">Featured articles</h2><div class="bfeat">%s</div>'
        '<div class="bsearch"><label class="sr" for="bq">Search articles</label><input id="bq" type="search" placeholder="Search articles" autocomplete="off" data-blog-filter><p class="small" data-blog-count aria-live="polite"></p></div>'
        '<nav class="chips" aria-label="Categories">%s</nav><div data-blog-list>%s</div></div></section>%s</main>') % (
    h1_html('IPTV guides and setup advice.', 'b'), len(allp), feat, chips, ''.join(sections),
    re.search(r'<section class="cta">.*?</section>', idx, re.S).group(0))
idx = re.sub(r'<main id="main">.*?</main>', lambda m: main, idx, 1, flags=re.S)
wr('blog/index.html', idx)

# ---- sitemap ----
sm = rd('sitemap.xml')
sm = re.sub(r'<url><loc>https://wizzocodes\.com/blog/[^<]*</loc><lastmod>[^<]*</lastmod></url>\n?', '', sm)
urls = ['<url><loc>%s/blog/</loc><lastmod>%s</lastmod></url>' % (BASE, TODAY)] + [
    '<url><loc>%s/blog/%s/</loc><lastmod>%s</lastmod></url>' % (BASE, p['slug'], p['date']) for p in allp]
sm = sm.replace('</urlset>', '\n'.join(urls) + '\n</urlset>')
wr('sitemap.xml', sm)

# ---- topic plan export ----
rows = [('published', p['slug'], p['title'], p['cat'], p.get('kw', ''), '; '.join(p.get('kw2', [])), p['date']) for p in allp]
json.dump([dict(status=r[0], slug=r[1], title=r[2], category=r[3], primary_keyword=r[4], secondary=r[5], date=r[6]) for r in rows], open('./published.json', 'w'), indent=1)
print('existing', len(existing), 'new', len(NEWP), 'total', len(allp))
print('ERRORS' if errs else 'content checks ok', errs)
print('words per new article: min %d max %d avg %d' % (min(p['words'] for p in NEWP), max(p['words'] for p in NEWP), sum(p['words'] for p in NEWP) / len(NEWP)))
