# -*- coding: utf-8 -*-
"""Apply all slide edits to slides.html using exact string replacement (v2, verified strings)."""
import io, os, glob

B = [d for d in glob.glob('D:/*صعود*') if not d.startswith('D:/ar')][0]
BA = os.path.join(B, 'build_assets')

def rd(f):
    return io.open(os.path.join(BA, f), encoding='utf-8').read()

def wr(f, s):
    io.open(os.path.join(BA, f), 'w', encoding='utf-8').write(s)

s = rd('slides.html')

# ============================================================
# A) Bismillah removed from slide 21 (aria-label with fa digits)
# ============================================================
old = '<section class="slide title-slide" id="s21" aria-label="اسلاید ۲۱">\n  <img class="bismillah" src="__IMG:bismillah.png__" alt="بسم الله الرحمن الرحیم">\n'
new = '<section class="slide title-slide" id="s21" aria-label="اسلاید ۲۱">\n'
assert old in s, "S21 bismillah not found"
s = s.replace(old, new)
print('A) S21 bismillah removed')

# ============================================================
# B) Slide 1: redesign 7-indicator band (bigger two-line cards)
# ============================================================
start = s.find('<svg viewBox="0 0 1160 170" width="100%" style="max-width:1160px" height="170"')
assert start != -1, "S1 svg not found"
end = s.find('</svg>', start) + len('</svg>')
new_s1_svg = '''<svg viewBox="0 0 1160 186" width="100%" style="max-width:1160px" height="178" role="img" aria-label="شاخص‌های کلیدی صعود">
  <g>
    <rect x="40"  y="16" width="140" height="100" fill="#14545C" rx="12"/>
    <rect x="198" y="16" width="140" height="100" fill="#C0492F" rx="12"/>
    <rect x="356" y="16" width="140" height="100" fill="#1F8A4C" rx="12"/>
    <rect x="514" y="16" width="140" height="100" fill="#1C6B70" rx="12"/>
    <rect x="672" y="16" width="140" height="100" fill="#7A8791" rx="12"/>
    <rect x="830" y="16" width="140" height="100" fill="#C9A22F" rx="12"/>
    <rect x="988" y="16" width="140" height="100" fill="#2F6F9F" rx="12"/>
    <g text-anchor="middle" font-size="14" font-weight="700" fill="#fff">
      <text x="110"  y="50">توسعهٔ انسانی</text>
      <text x="268"  y="50">عدالت اجتماعی</text>
      <text x="426"  y="50">بهداشت و درمان</text>
      <text x="584"  y="50">علم و فناوری</text>
      <text x="742"  y="50">زیرساخت</text>
      <text x="900"  y="50" fill="#3a2c00">حمل‌ونقل</text>
      <text x="1058" y="50">دانشگاه‌ها</text>
    </g>
    <g text-anchor="middle" font-size="15.5" font-weight="700">
      <text x="110"  y="84" fill="#9FD4E8">رتبهٔ ۱۲۰ ← ۶۰</text>
      <text x="268"  y="84" fill="#F2C4B8">فقر: ٪۴۶ ← زیر ٪۱۵</text>
      <text x="426"  y="84" fill="#BFE8CF">امیدبه‌زندگی: ۵۷ ← ۷۶</text>
      <text x="584"  y="84" fill="#B5D8DE">رتبهٔ ۱ جهانی در ریاضی</text>
      <text x="742"  y="84" fill="#D4DAE0">جاده‌ها: ۴/۴ برابری</text>
      <text x="900"  y="84" fill="#7a6414">بار ریلی: ۴/۶ برابری</text>
      <text x="1058" y="84" fill="#C5DDF2">مدارک: ۵۹/۶۴ برابری</text>
    </g>
  </g>
  <rect x="40" y="136" width="1066" height="26" fill="#14545C" rx="6"/>
  <text x="573" y="154" font-size="13.5" font-weight="700" fill="#fff" text-anchor="middle">۲۱ اسلاید | ۸ محور اصلی | آمار از منابع بین‌المللی: بانک جهانی، سازمان ملل، آژانس بین‌المللی انرژی، مجلۀ «ساینس»</text>
</svg>'''
s = s[:start] + new_s1_svg + s[end:]
print('B) S1 band redesigned')

# ============================================================
# C) Slide 3 & 6: statrow compact class
# ============================================================
old3 = '<div class="statrow" style="flex-direction:column;height:100%">\n          <div class="stat t"'
assert old3 in s, "S3 statrow not found"
s = s.replace(old3, '<div class="statrow compact" style="flex-direction:column;height:100%;justify-content:center">\n          <div class="stat t"')
print('C1) S3 statrow compact')

old6 = '<div class="statrow" style="flex-direction:column;height:100%;justify-content:space-between">\n          <div class="stat t"'
assert old6 in s, "S6 statrow not found"
s = s.replace(old6, '<div class="statrow compact" style="flex-direction:column;height:100%;justify-content:center">\n          <div class="stat t"')
print('C2) S6 statrow compact')

# ============================================================
# D) Slide 4: fix arrow + lift bar numbers off the line
# ============================================================
# D1: arrow — from above red bar to above green bar, gold color of this chart
old = '<path d="M250 90 C 300 90, 300 160, 300 175" stroke="#C9A227" stroke-width="3" fill="none" marker-end="url(#ah3)"/>'
new = '<path d="M165 56 C 230 40, 305 75, 352 122" stroke="#C9A227" stroke-width="3" fill="none" marker-end="url(#ah3)"/>'
assert old in s, "S4 arrow not found"
s = s.replace(old, new)
print('D1) S4 arrow fixed')

# D2: lift head-to-head bar numbers (clearance above bar tops)
repl4 = [
    ('<text x="160" y="146" font-size="16" font-weight="700" fill="#14545C" text-anchor="middle">۵۱٫۳</text>',
     '<text x="160" y="136" font-size="16" font-weight="700" fill="#14545C" text-anchor="middle">۵۱٫۳</text>'),
    ('<text x="280" y="144" font-size="16" font-weight="700" fill="#5D6B75" text-anchor="middle">۵۲٫۷</text>',
     '<text x="280" y="134" font-size="16" font-weight="700" fill="#5D6B75" text-anchor="middle">۵۲٫۷</text>'),
    ('<text x="400" y="89" font-size="16" font-weight="700" fill="#C0492F" text-anchor="middle">۸۳٫۸</text>',
     '<text x="400" y="79" font-size="16" font-weight="700" fill="#C0492F" text-anchor="middle">۸۳٫۸</text>'),
]
for o, n in repl4:
    assert o in s, "S4 number not found: " + o[:60]
    s = s.replace(o, n)
print('D2) S4 bar numbers lifted')

# ============================================================
# E) Slide 5: move poverty-comparison values further right (off the bars)
# ============================================================
repl5 = [
    ('<text x="400" y="43" font-size="13" font-weight="700" fill="#C0492F">بالای ٪۵۰</text>',
     '<text x="410" y="43" font-size="13" font-weight="700" fill="#C0492F">بالای ٪۵۰</text>'),
    ('<text x="252" y="91" font-size="13" fill="#5D6B75">٪۱۹</text>',
     '<text x="264" y="91" font-size="13" fill="#5D6B75">٪۱۹</text>'),
    ('<text x="226" y="139" font-size="13" fill="#5D6B75">٪۱۵٫۷</text>',
     '<text x="240" y="139" font-size="13" fill="#5D6B75">٪۱۵٫۷</text>'),
    ('<text x="214" y="187" font-size="13" fill="#5D6B75">٪۱۴٫۲</text>',
     '<text x="230" y="187" font-size="13" fill="#5D6B75">٪۱۴٫۲</text>'),
    ('<text x="196" y="235" font-size="13" fill="#14545C">٪۱۲</text>',
     '<text x="212" y="235" font-size="13" fill="#14545C">٪۱۲</text>'),
]
for o, n in repl5:
    assert o in s, "S5 number not found: " + o[:60]
    s = s.replace(o, n)
print('E) S5 bar values moved off the bars')

# ============================================================
# F) Slide 16: replace photo with infographic card
# ============================================================
old16 = '''      <div class="col">
        <div class="imgbox" style="height:100%">
          <img src="__IMG:photo_women.jpg__" alt="دستاوردهای زنان ایرانی" style="height:330px;object-fit:cover">
          <div class="cap">نمای کلی از دستاوردهای زنان در حوزه‌های مختلف</div>
        </div>
      </div>'''
new16 = '''      <div class="col">
        <div class="card" style="height:100%;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(135deg,#14545C 0%,#0E3A40 100%);border:none">
          <div style="color:#fff;font-size:17px;font-weight:700;margin-bottom:14px;text-align:center">دستاوردهای کلان زنان</div>
          <svg viewBox="0 0 400 300" width="100%" height="280" role="img" aria-label="نمای کلی دستاوردهای زنان">
            <text x="200" y="22" font-size="14" font-weight="700" fill="#9FD4E8" text-anchor="middle">قبل از انقلاب ← امروز</text>
            <g font-size="15" font-weight="700" text-anchor="middle">
              <rect x="30" y="40" width="340" height="46" fill="rgba(255,255,255,.08)" rx="10"/>
              <text x="200" y="70" fill="#E8C66A">رشته‌های ورزشی: ۳ ← ۳۸</text>
              <rect x="30" y="96" width="340" height="46" fill="rgba(255,255,255,.08)" rx="10"/>
              <text x="200" y="126" fill="#BFE8CF">مربیان: ۹,۰۰۰ ← ۳۵,۰۰۰</text>
              <rect x="30" y="152" width="340" height="46" fill="rgba(255,255,255,.08)" rx="10"/>
              <text x="200" y="182" fill="#F2C4B8">داوران: ۷,۰۰۰ ← ۱۶,۰۰۰</text>
              <rect x="30" y="208" width="340" height="46" fill="rgba(255,255,255,.08)" rx="10"/>
              <text x="200" y="238" fill="#B5D8DE">ورزشگاه اختصاصی: ۱ ← ۳۰</text>
            </g>
            <text x="200" y="282" font-size="13" fill="rgba(255,255,255,.6)" text-anchor="middle">بیش از ۲,۷۰۰ سازمان مردم‌نهاد امور زنان</text>
          </svg>
        </div>
      </div>'''
assert old16 in s, "S16 photo block not found"
s = s.replace(old16, new16)
print('F) S16 photo -> infographic card')

# ============================================================
# G) Slide 19: replace photo with ranking card
# ============================================================
old19 = '''      <div class="col">
        <div class="imgbox" style="height:100%">
          <img src="__IMG:photo_rank.jpg__" alt="رتبه‌بندی جهانی ایران" style="height:230px;object-fit:cover">
          <div class="cap">نمای کلی از رتبه‌های ایران در شاخص‌های مختلف جهانی</div>
        </div>
      </div>'''
new19 = '''      <div class="col">
        <div class="card" style="height:100%;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(135deg,#1F8A4C 0%,#14545C 100%);border:none">
          <div style="color:#fff;font-size:17px;font-weight:700;margin-bottom:12px;text-align:center">ایران در رده‌بندی‌های جهانی</div>
          <svg viewBox="0 0 400 330" width="100%" height="300" role="img" aria-label="رتبه‌های کلیدی ایران">
            <g font-size="14" font-weight="700" text-anchor="middle">
              <rect x="40" y="8" width="320" height="46" fill="rgba(255,255,255,.12)" rx="10"/>
              <text x="200" y="37" fill="#fff">توسعهٔ انسانی — رتبهٔ ۶۰</text>
              <rect x="40" y="62" width="320" height="46" fill="rgba(255,255,255,.12)" rx="10"/>
              <text x="200" y="91" fill="#E8C66A">ریاضیات — رتبهٔ ۱ دنیا</text>
              <rect x="40" y="116" width="320" height="46" fill="rgba(255,255,255,.12)" rx="10"/>
              <text x="200" y="145" fill="#BFE8CF">ژنتیک و سلول — رتبهٔ ۲</text>
              <rect x="40" y="170" width="320" height="46" fill="rgba(255,255,255,.12)" rx="10"/>
              <text x="200" y="199" fill="#fff">داروسازی — رتبهٔ ۱۱</text>
              <rect x="40" y="224" width="320" height="46" fill="rgba(255,255,255,.12)" rx="10"/>
              <text x="200" y="253" fill="#F2C4B8">اختراعات — رتبهٔ ۷</text>
              <rect x="40" y="278" width="320" height="46" fill="rgba(255,255,255,.12)" rx="10"/>
              <text x="200" y="307" fill="#B5D8DE">برق ارزان — رتبهٔ ۳</text>
            </g>
          </svg>
        </div>
      </div>'''
assert old19 in s, "S19 photo block not found"
s = s.replace(old19, new19)
print('G) S19 photo -> ranking card')

# ============================================================
# H) Slide 20: fix overlap — limit cols, move bar inside body
# ============================================================
old20a = '''    <h2 class="tag"><span class="chip">نتیجه‌گیری</span> چرا همهٔ پتانسیل‌ها محقق نشد؟</h2>
    <div class="cols">
      <div class="col">
        <div class="card" style="height:100%">
          <div class="kpi-head" style="color:var(--red)">موانع بیرونی (۸ مورد)</div>'''
new20a = '''    <h2 class="tag"><span class="chip">نتیجه‌گیری</span> چرا همهٔ پتانسیل‌ها محقق نشد؟</h2>
    <div class="cols" style="height:calc(100% - 84px)">
      <div class="col">
        <div class="card" style="height:100%">
          <div class="kpi-head" style="color:var(--red)">موانع بیرونی (۸ مورد)</div>'''
assert old20a in s, "S20 cols head not found"
s = s.replace(old20a, new20a)
print('H1) S20 cols height limited')

# H2: use find-between-anchors (multi-line exact match fails on whitespace)
# The bottom-bar block in S20 starts after the </div> that closes .cols,
# and ends just before <div class="foot"> that opens S20's foot.
s20 = s.find('id="s20"')
assert s20 != -1, "S20 section not found"
# find the bottom bar opening (the margin-top:12px div)
bar_open = s.find('<div style="margin-top:12px;display:flex;justify-content:center">', s20)
assert bar_open != -1, "S20 bottom bar open not found"
# the bar is preceded by the closing </div> of .cols — capture from there
# walk back to find that closing </div>
close_col = s.rfind('</div>', s20, bar_open)
assert close_col != -1, "S20 cols closing not found"
# the foot of S20
foot_pos = s.find('<div class="foot">', bar_open)
assert foot_pos != -1, "S20 foot not found"
new20b = '''</div>
    <div style="margin-top:10px">
      <svg viewBox="0 0 1160 68" width="100%" style="max-width:1160px" height="64" role="img" aria-label="توزیع موانع بیرونی و درونی">
        <text x="580" y="14" font-size="14" font-weight="700" fill="#14545C" text-anchor="middle">وزن موانع در تحقق پتانسیل‌ها</text>
        <rect x="270" y="26" width="520" height="32" fill="#C0492F" rx="7"/>
        <rect x="790" y="26" width="270" height="32" fill="#C9A22F" rx="7"/>
        <text x="530" y="48" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">موانع بیرونی: ۸ مورد — ۶۰٪</text>
        <text x="925" y="48" font-size="14" font-weight="700" fill="#fff" text-anchor="middle">موانع درونی: ۴ دسته — ۴۰٪</text>
      </svg>
    </div>
  </div>
  '''
s = s[:close_col] + new20b + s[foot_pos:]
print('H2) S20 bar moved inside body')

wr('slides.html', s)
print()
print('ALL SLIDE EDITS APPLIED OK')
