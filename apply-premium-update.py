#!/usr/bin/env python3
# GSCC premium tier update — 24 Sep 2026
# Executive View: Weekly Brief nav link + CSV exports. Index: premium copy.
import sys

def P(old, new):
    return (old, new)

PATCHES = {

'executive-view.html': [
    P('<a href="#evidence">Evidence</a>',
      '<a href="#evidence">Evidence</a>\n    <a href="weekly-brief.html" style="color:var(--gold-bright)">★ Weekly Brief</a>'),
    P('different definitions — see module Evidence sections).</p>',
      'different definitions — see module Evidence sections).</p>\n  <div class="card" style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:18px">\n    <h3 style="margin:0">Premium utilities</h3>\n    <span style="font-size:12px;color:var(--muted)">Part of the paid tier — with the Weekly Brief</span>\n    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-left:auto">\n      <button class="preset" style="cursor:pointer" onclick="exportMatrix()">Export matrix (CSV)</button>\n      <button class="preset" style="cursor:pointer" onclick="exportTriggers()">Export triggers (CSV)</button>\n      <a class="preset" style="color:var(--gold-bright);border-color:rgba(192,138,45,.5);text-decoration:none" href="weekly-brief.html">★ Weekly Brief</a>\n    </div>\n  </div>'),
    P('/* ===== nav active state on scroll ===== */',
      '/* ===== premium CSV exports ===== */\n'
      'function stripTags(s){return String(s).replace(/<[^>]+>/g,\'\')}\n'
      'function dlCSV(name, rows){\n'
      '  var csv = rows.map(function(r){return r.map(function(v){return \'"\' + String(v).replace(/"/g,\'""\') + \'"\'}).join(\',\')}).join(\'\\r\\n\');\n'
      '  var a=document.createElement(\'a\');\n'
      '  a.href=URL.createObjectURL(new Blob([\'\\ufeff\'+csv],{type:\'text/csv\'}));\n'
      '  a.download=name;a.click();\n'
      '}\n'
      'function exportMatrix(){\n'
      '  var rows=[[\'Region\',\'Fund AUM\',\'Growth YoY\',\'Competition (1-10)\',\'Regulatory burden (1-10)\',\'Digital maturity (1-10)\',\'Entry difficulty (1-10)\',\'Priority score\']];\n'
      '  MDATA.forEach(function(r){rows.push([r.name,r.aum,r.growth,r.comp,r.reg,r.dig,r.entry,r.prio])});\n'
      '  dlCSV(\'gscc-cross-region-matrix.csv\',rows);\n'
      '}\n'
      'function exportTriggers(){\n'
      '  var rows=[[\'Trigger\',\'Status\',\'Region\',\'Event\',\'Recommended response\',\'Source\']];\n'
      '  TRIGGERS.forEach(function(t){rows.push([t.n,t.s,t.reg,stripTags(t.d),stripTags(t.p),t.m])});\n'
      '  dlCSV(\'gscc-mandate-triggers.csv\',rows);\n'
      '}\n'
      '\n/* ===== nav active state on scroll ===== */'),
],

'index.html': [
    P('<li>All 7 regional & thematic modules</li>',
      '<li>All 7 regional & thematic modules</li>\n        <li>The Weekly Brief — premium intelligence edition</li>\n        <li>CSV data exports (matrix, triggers)</li>'),
    P('<span>BOARD Q&A</span>',
      '<span>BOARD Q&A</span><span>WEEKLY BRIEF</span>'),
],
}

ok = True
for fname, patches in PATCHES.items():
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
    except FileNotFoundError:
        print(f'FAIL: {fname} not found'); ok = False; continue
    applied = 0
    for i, (old, new) in enumerate(patches):
        if new in c and old not in c:
            print(f'  skip (already applied): {fname} #{i}')
            continue
        if old not in c:
            print(f'FAIL: {fname} patch #{i}: old string not found'); ok = False; continue
        c = c.replace(old, new, 1)
        applied += 1
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{fname}: {applied}/{len(patches)} patches applied')

sys.exit(0 if ok else 1)
