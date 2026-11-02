import re,glob,os,json,html,collections,urllib.parse
S='../site'; B='https://wizzocodes.com'
pages={}
for f in glob.glob(S+'/**/*.html',recursive=True):
    rel=os.path.relpath(f,S)
    url='/' if rel=='index.html' else ('/404.html' if rel=='404.html' else '/'+rel[:-10])
    pages[url]=f
bad=[];titles=collections.defaultdict(list);descs=collections.defaultdict(list);h1s=collections.defaultdict(list)
for url,f in pages.items():
    h=open(f).read()
    t=html.unescape(re.search(r'<title>(.*?)</title>',h,re.S).group(1))
    d=html.unescape((re.search(r'<meta name="description" content="([^"]*)"',h) or [0,''])[1])
    h1=html.unescape(re.sub(r'<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',h,re.S).group(1)))
    titles[t].append(url);descs[d].append(url);h1s[h1].append(url)
    can=re.search(r'<link rel="canonical" href="([^"]*)"',h)
    if url!='/404.html':
        if not can or can.group(1)!=B+url: bad.append(('canonical',url,can and can.group(1)))
        if len(d)<70 or len(d)>165: bad.append(('desc-len',url,len(d)))
        if len(t)>75: bad.append(('title-len',url,len(t)))
    if len(re.findall(r'<h1[ >]',h))!=1: bad.append(('h1count',url))
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',h,re.S):
        try: json.loads(m.group(1))
        except Exception as e: bad.append(('jsonld',url,str(e)))
    # links
    for m in re.finditer(r'(?:href|src)="([^"#?]*)(#[^"]*)?[^"]*"',h):
        l=m.group(1)
        if not l or re.match(r'(https?:|mailto:|tel:|data:)',l): continue
        base=os.path.dirname(f) if not url.endswith('/') else f.rsplit('/',1)[0]
        if l.startswith('/'): tgt=S+l
        else: tgt=os.path.normpath(os.path.join(base,l))
        if os.path.isdir(tgt): tgt=os.path.join(tgt,'index.html')
        if not os.path.exists(tgt): bad.append(('broken',url,l))
for name,dct in (('title',titles),('desc',descs),('h1',h1s)):
    for k,v in dct.items():
        if len(v)>1 and not (name=='title' and v==['/404.html']): bad.append(('dup-'+name,k[:60],v))
sm=open(S+'/sitemap.xml').read()
locs=re.findall(r'<loc>([^<]*)</loc>',sm)
for l in locs:
    p=l.replace(B,'')
    if p not in pages: bad.append(('sitemap-missing-page',l))
for url in pages:
    if url!='/404.html' and B+url not in locs: bad.append(('page-not-in-sitemap',url))
print('pages',len(pages),'sitemap urls',len(locs),'dup sitemap',len(locs)-len(set(locs)))
print('ISSUES',len(bad)); [print(b) for b in bad[:40]]
