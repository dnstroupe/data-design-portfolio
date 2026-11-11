"""Small checks for a buildless portfolio. Run with Python 3."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids=set(); self.links=[]; self.h1=0; self.main=0; self.lang=False; self.viewport=False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='h1': self.h1+=1
        if tag=='main': self.main+=1
        if tag=='html': self.lang=bool(a.get('lang'))
        if tag=='meta' and a.get('name')=='viewport': self.viewport=True
pages={p.name:Page(p.read_text()) for p in ROOT.glob('*.html')}
errors=[]
for name,page in pages.items():
    if not(page.h1==1 and page.main==1 and page.lang and page.viewport): errors.append(f'{name}: page structure')
    for href in page.links:
        u=urlsplit(href)
        if u.scheme or u.netloc: continue
        target=u.path or name
        if not (ROOT/target).is_file(): errors.append(f'{name}: missing {href}')
        if u.fragment and target in pages and u.fragment not in pages[target].ids: errors.append(f'{name}: missing anchor {href}')
def luminance(color):
    rgb=[int(color[i:i+2],16)/255 for i in (1,3,5)]
    v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb]
    return sum(a*b for a,b in zip(v,(.2126,.7152,.0722)))
for fg,bg in [('#f3f5f3','#141c20'),('#b8c7c7','#141c20'),('#a8e0d0','#141c20'),('#11221e','#a8e0d0'),('#243c38','#eaf0ee'),('#435f56','#ffffff'),('#234c3c','#d2e8df')]:
    light,dark=sorted((luminance(fg),luminance(bg)),reverse=True)
    ratio=(light+.05)/(dark+.05)
    print(f'{fg} on {bg}: {ratio:.2f}:1')
    if ratio<4.5: errors.append(f'Contrast below 4.5:1: {fg} on {bg}')
if errors: raise SystemExit('\n'.join(errors))
print(f'Passed: {len(pages)} pages, internal links and anchors, structure, and selected contrast pairs.')
