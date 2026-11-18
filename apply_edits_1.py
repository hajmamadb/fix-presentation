# -*- coding: utf-8 -*-
import io, os, glob, re, sys

B = [d for d in glob.glob('D:/*\u0635\u0639\u0648\u062f*') if not d.startswith('D:/ar')][0]
BA = os.path.join(B, 'build_assets')

def rd(f):
    return io.open(os.path.join(BA, f), encoding='utf-8').read()

def wr(f, s):
    io.open(os.path.join(BA, f), 'w', encoding='utf-8').write(s)

# ============================================================
# 1) HTML_HEAD: bismillah 1/3, transitions, animations, stat
# ============================================================
head = rd('html_head.html')

# bismillah: 46px -> 15px (1/3)
old = ".title-slide .bismillah{height:46px}"
new = ".title-slide .bismillah{height:15px}"
assert old in head, "bismillah rule not found"
head = head.replace(old, new)

# Slide transitions: replace .slide display rules
old = ".slide{\n  position:absolute; inset:0; width:1280px; height:720px; overflow:hidden;\n  display:none; background:#FBFAF7;\n}\n.slide.active{display:block}"
new = (".slide{\n"
       "  position:absolute; inset:0; width:1280px; height:720px; overflow:hidden;\n"
       "  opacity:0; visibility:hidden; background:#FBFAF7;\n"
       "  transition:opacity .5s ease, visibility 0s linear .5s, transform .55s cubic-bezier(.22,.61,.36,1);\n"
       "  transform:translateX(46px);\n"
       "  z-index:1;\n"
       "}\n"
       ".slide.active{\n"
       "  opacity:1; visibility:visible; z-index:2;\n"
       "  transition:opacity .5s ease, visibility 0s, transform .55s cubic-bezier(.22,.61,.36,1);\n"
       "  transform:translateX(0);\n"
       "}\n"
       ".slide.leaving{\n"
       "  opacity:0; visibility:hidden; z-index:1;\n"
       "  transform:translateX(-46px);\n"
       "  transition:opacity .4s ease, visibility 0s linear .4s, transform .45s cubic-bezier(.22,.61,.36,1);\n"
       "}\n"
       "/* entrance animations for content */\n"
       ".slide.active .body > *{animation:riseIn .55s cubic-bezier(.22,.61,.36,1) both}\n"
       ".slide.active .body > *:nth-child(1){animation-delay:.05s}\n"
       ".slide.active .body > *:nth-child(2){animation-delay:.13s}\n"
       ".slide.active .body > *:nth-child(3){animation-delay:.21s}\n"
       ".slide.active .body > *:nth-child(4){animation-delay:.29s}\n"
       ".slide.active .body > *:nth-child(5){animation-delay:.37s}\n"
       ".slide.active .body > *:nth-child(6){animation-delay:.45s}\n"
       ".slide.active .body .cols .col{animation:riseIn .6s cubic-bezier(.22,.61,.36,1) both;animation-delay:.18s}\n"
       ".slide.active .body .cols .col:nth-child(2){animation-delay:.3s}\n"
       ".slide.active .body .cols .col:nth-child(3){animation-delay:.42s}\n"
       "@keyframes riseIn{\n"
       "  0%{opacity:0;transform:translateY(22px)}\n"
       "  100%{opacity:1;transform:translateY(0)}\n"
       "}\n"
       "@keyframes fadeIn{\n"
       "  0%{opacity:0}\n"
       "  100%{opacity:1}\n"
       "}\n"
       ".slide.active .hband{animation:fadeIn .4s ease both}\n"
       ".slide.active .foot{animation:fadeIn .5s ease .2s both}\n"
       ".slide.active .bismillah{animation:fadeIn .7s ease .3s both}")
assert old in head, "slide display rule not found"
head = head.replace(old, new)

# stat: smaller padding for compact rows
old = ".stat{display:flex;flex-direction:column;align-items:center;text-align:center;padding:14px 8px}"
new = (".stat{display:flex;flex-direction:column;align-items:center;text-align:center;padding:14px 8px}\n"
       ".statrow.compact .stat{padding:9px 8px}\n"
       ".statrow.compact .stat .n{font-size:30px}\n"
       ".statrow.compact .stat .n .u{font-size:16px}\n"
       ".statrow.compact .stat .l{font-size:13px;margin-top:5px;line-height:1.4}")
assert old in head
head = head.replace(old, new)

# Slight global polish: card hover-free, smoother text rendering
old = "svg text{font-family:'Vazirmatn',Tahoma}"
new = ("svg text{font-family:'Vazirmatn',Tahoma}\n"
       "body{-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}\n"
       ".card{transition:box-shadow .3s ease}")
assert old in head
head = head.replace(old, new)

wr('html_head.html', head)
print('html_head.html OK')

# ============================================================
# 2) NOTES_JS: transition support (leaving class + timeout)
# ============================================================
js = rd('notes_js.html')

old = """  function show(i){
    if(i<0||i>=slides.length) return;
    slides[cur].classList.remove('active');
    cur = i;
    slides[cur].classList.add('active');"""
new = """  var transTimer = null;
  function show(i){
    if(i<0||i>=slides.length) return;
    if(transTimer){ clearTimeout(transTimer); transTimer=null; }
    var prev = slides[cur];
    var next = slides[i];
    prev.classList.remove('active');
    prev.classList.add('leaving');
    cur = i;
    next.classList.remove('leaving');
    next.classList.add('active');
    transTimer = setTimeout(function(){ prev.classList.remove('leaving'); transTimer=null; }, 520);"""
assert old in js, "show() head not found"
js = js.replace(old, new)

wr('notes_js.html', js)
print('notes_js.html OK')
