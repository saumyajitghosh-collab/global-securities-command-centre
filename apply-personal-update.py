#!/usr/bin/env python3
# GSCC personalisation v1 — 24 Sep 2026
# Market selection + modular pricing, role lens, theme, trigger watchlist,
# custom-research menu. Rewrites auth-gate.js (v3); patches login.html (v3) and index.html.
import sys

GATE_V3 = r'''/* GSCC Auth Gate v3 — session guard + device-tied trial + personalisation.
   - Runs synchronously in <head> of every protected page.
   - Trial is tied to the DEVICE (not the account): a new account after the
     device trial has ended does not restart the clock.
   - Owner ("founder") accounts never expire.
   - Applies the user's saved theme (gscc_prefs) and exposes GSCC_PREFS.
   - Redirects unauthenticated / expired visitors to login.html. */
(function () {
  'use strict';
  var here = window.location.pathname.split('/').pop() || 'index.html';
  if (here === 'login.html' || here === 'auth-gate.js') return;

  var DAY = 86400000, TRIAL_DAYS = 30, NEVER = 4102444800000; /* 2100-01-01 */

  /* ---- device marker (localStorage x2 + cookie; earliest wins) ---- */
  function readM(k) { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) { return null; } }
  function writeM(ts) {
    var v = JSON.stringify({ t: ts });
    try { localStorage.setItem('gscc_did', v); } catch (e) {}
    try { localStorage.setItem('gscc_anc', v); } catch (e) {}
    try { document.cookie = 'prefs_v=' + encodeURIComponent(v) + ';max-age=315360000;path=/;SameSite=Lax'; } catch (e) {}
  }
  function cookieM() {
    try {
      var m = document.cookie.match(/(?:^|;\s*)prefs_v=([^;]+)/);
      return m ? JSON.parse(decodeURIComponent(m[1])) : null;
    } catch (e) { return null; }
  }
  function deviceTs() {
    var a = readM('gscc_did'), b = readM('gscc_anc'), c = cookieM();
    var cands = [a, b, c].filter(function (x) { return x && x.t; }).map(function (x) { return x.t; });
    if (!cands.length) { writeM(Date.now()); return Date.now(); }
    return Math.min.apply(null, cands);
  }
  function deviceTrialEnd() { return deviceTs() + TRIAL_DAYS * DAY; }
  function devicePaidUntil() { var v = parseInt(localStorage.getItem('gscc_paid_until') || '0', 10) || 0; return v; }

  var users = {}, session = null, acct = null;
  try { users = JSON.parse(localStorage.getItem('gscc_users') || '{}'); } catch (e) {}
  try { session = JSON.parse(localStorage.getItem('gscc_session') || 'null'); } catch (e) {}

  var now = Date.now();
  var sessionValid = session && session.uid && session.sessionExpires && session.sessionExpires > now;
  var accessValid = false, daysLeft = 0, plan = null;

  if (sessionValid && users[session.uid]) {
    acct = users[session.uid];
    var until = Math.max(acct.planExpires || 0, devicePaidUntil());
    if (acct.plan === 'owner') { accessValid = true; plan = 'owner'; daysLeft = -1; }
    else if (until > now) {
      accessValid = true;
      plan = acct.plan || 'trial';
      daysLeft = Math.max(0, Math.ceil((until - now) / DAY));
    }
  }

  if (!sessionValid || !accessValid) {
    var target = (!sessionValid) ? 'login.html' : 'login.html#payment';
    document.documentElement.style.display = 'none';
    window.location.replace(target);
    return;
  }

  window.GSCC_AUTH = {
    uid: session.uid,
    plan: plan,
    daysLeft: daysLeft,
    owner: plan === 'owner',
    trial: plan === 'trial',
    logout: function () {
      localStorage.removeItem('gscc_session');
      window.location.replace('login.html');
    }
  };

  /* ---- personalisation (markets, role, theme, watchlist) ---- */
  var THEMES = { classic: ['#C08A2D', '#E3B45C'], teal: ['#2C7A74', '#4FB3AB'], violet: ['#5B4A8A', '#9C8CD6'], emerald: ['#1F7A4D', '#57C28A'] };
  var P = null;
  try { P = JSON.parse(localStorage.getItem('gscc_prefs') || 'null'); } catch (e) {}
  if (!P) P = {};
  var th = THEMES[P.theme] || THEMES.classic;
  try {
    document.documentElement.style.setProperty('--gold', th[0]);
    document.documentElement.style.setProperty('--gold-bright', th[1]);
  } catch (e) {}
  window.GSCC_PREFS = { markets: P.markets || null, role: P.role || '', theme: P.theme || 'classic', watch: P.watch || [] };
})();
'''

def P(old, new):
    return (old, new)

LOGIN = [

# 1. CSS additions
P('@media(max-width:520px){.card{padding:28px 22px 22px}',
'''/* Personalisation */
.cfg-head{font-family:'Fraunces',serif;font-size:19px;color:#fff;margin-bottom:4px}
.cfg-sub{font-size:12.5px;color:var(--muted);margin-bottom:6px}
.mk-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.mk{display:flex;align-items:center;gap:9px;background:rgba(14,27,44,.55);border:1.5px solid var(--line);border-radius:9px;padding:10px 12px;cursor:pointer;font-size:13.5px;color:var(--text);transition:all .15s}
.mk:hover{border-color:rgba(192,138,45,.5)}
.mk:has(input:checked){border-color:var(--gold);background:rgba(192,138,45,.08)}
.mk input{width:auto;accent-color:var(--gold)}
.mk.sm{font-size:11px;font-family:'IBM Plex Mono',monospace;padding:7px 10px}
.watch-grid{display:grid;grid-template-columns:1fr;gap:6px;max-height:220px;overflow-y:auto;padding-right:4px}
.role-row,.theme-row{display:flex;gap:8px;flex-wrap:wrap}
.rpill{background:rgba(14,27,44,.6);border:1.5px solid var(--line);color:var(--muted);font-family:'Public Sans',sans-serif;font-size:12.5px;font-weight:600;padding:8px 14px;border-radius:18px;cursor:pointer;transition:all .15s}
.rpill:hover{color:var(--text)}
.rpill.on{border-color:var(--gold);color:var(--gold-bright);background:rgba(192,138,45,.1)}
.swatch{width:34px;height:34px;border-radius:50%;border:2.5px solid transparent;cursor:pointer;transition:all .15s}
.swatch.on{border-color:#fff;transform:scale(1.12)}
.cfg-total{background:rgba(44,122,116,.1);border:1px solid rgba(79,179,171,.3);border-radius:10px;padding:11px 14px;font-size:13px;color:var(--muted);margin-top:10px}
.cfg-total b{color:var(--gold-bright)}
.research-menu{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:10px 0 4px}
.research-menu a{background:rgba(14,27,44,.55);border:1px solid var(--line);border-radius:9px;padding:10px 12px;font-size:12.5px;color:var(--text);text-decoration:none;transition:all .15s}
.research-menu a:hover{border-color:var(--gold);color:var(--gold-bright)}

@media(max-width:520px){.card{padding:28px 22px 22px}'''),

# 2. welcome view: config button
P('''    <div style="display:flex;gap:10px;margin-top:10px">
      <button class="btn ghost" style="margin-top:0" id="w-settings">Account settings</button>''',
'''    <div style="display:flex;gap:10px;margin-top:10px;flex-wrap:wrap">
      <button class="btn ghost" style="margin-top:0" id="w-config">⚙ Markets & personalisation</button>
      <button class="btn ghost" style="margin-top:0" id="w-settings">Account settings</button>'''),

# 3. configure view before settings
P('''  <!-- ============ SETTINGS ============ -->''',
'''  <!-- ============ CONFIGURE ============ -->
  <div class="view" id="v-configure">
    <div class="tabs" style="visibility:hidden"><button>&nbsp;</button><button>&nbsp;</button></div>
    <div class="cfg-head">Personalise your Command Centre</div>
    <p class="cfg-sub">Choose the markets you cover — your price follows your selection. Add or remove markets anytime; the payment adjusts. Everything else (role lens, theme, watchlist) is included.</p>
    <label>Markets in my plan</label>
    <div class="mk-grid" id="mk-grid"></div>
    <div class="cfg-total" id="cfg-total"></div>
    <label>My role lens <span style="text-transform:none;letter-spacing:0">— how the brief and dashboard frame the data</span></label>
    <div class="role-row" id="role-row"></div>
    <label>Theme</label>
    <div class="theme-row" id="theme-row"></div>
    <label>Trigger watchlist</label>
    <div class="watch-grid" id="watch-grid"></div>
    <div class="msg err" id="cf-msg"></div>
    <button class="btn" id="cf-save">Save my configuration</button>
    <div class="foot">Modular ₹999/mo per market · Professional ₹2,999/mo (all markets + Executive View) · Team ₹11,999/mo (5 seats).<br>Custom research is menu-priced per request — see Account settings.</div>
  </div>

  <!-- ============ SETTINGS ============ -->'''),

# 4. settings: configure row
P('''    <div class="settings-row"><div class="sr-l">Change password''',
'''    <div class="settings-row"><div class="sr-l">Markets & personalisation<small>Markets, role lens, theme, watchlist — your price follows your selection</small></div><button class="link-btn" id="st-config">Configure</button></div>
    <div class="settings-row"><div class="sr-l">Change password'''),

# 5. settings: custom research menu before admin zone
P('''    <div id="admin-zone" style="display:none">''',
'''    <div class="cfg-head" style="color:var(--teal-bright);font-size:16px;margin-top:24px">✦ Custom research · menu pricing per request</div>
    <div class="research-menu">
      <a href="mailto:saumyajit.ghosh@gmail.com?subject=GSCC%20Research%3A%20Account%20deep-dive%20(%E2%82%B94%2C999)&body=Account%20to%20research%3A%0A%0AWhat%20I%20need%20by%20end%20of%20week%3A%0A">Named-account deep dive — ₹4,999</a>
      <a href="mailto:saumyajit.ghosh@gmail.com?subject=GSCC%20Research%3A%20Competitor%20brief%20(%E2%82%B97%2C999)&body=Competitor%20to%20profile%3A%0A%0ADecision%20context%3A%0A">Competitor positioning brief — ₹7,999</a>
      <a href="mailto:saumyajit.ghosh@gmail.com?subject=GSCC%20Research%3A%20Regulatory%20timeline%20(%E2%82%B95%2C999)&body=Regulator%20%2F%20topic%3A%0A%0AMarkets%20of%20interest%3A%0A">Regulatory timeline brief — ₹5,999</a>
      <a href="mailto:saumyajit.ghosh@gmail.com?subject=GSCC%20Research%3A%20Bespoke%20question%20(from%20%E2%82%B92%2C999)&body=My%20question%3A%0A%0AWhy%20now%3A%0A">Bespoke question — from ₹2,999</a>
    </div>
    <div class="tb-note" style="margin-top:6px">Each request is scoped and quoted before work begins; payment by UPI on acceptance. Professional and Team subscribers include the priority request line (two per quarter) — these menu prices apply to additional or standalone requests.</div>

    <div id="admin-zone" style="display:none">'''),

# 6. payment: modular plan card
P('''        <div class="p-note">For desks and pursuit teams. Yearly team plan ₹1,19,999 (save 17%).</div>
      </div>
    </div>''',
'''        <div class="p-note">For desks and pursuit teams. Yearly team plan ₹1,19,999 (save 17%).</div>
      </div>
      <div class="plan" data-plan="modular" data-days="30">
        <div class="p-name">Modular · Build your own</div>
        <div class="p-price">₹999 <small>/ market / month</small></div>
        <div class="p-note">Pay only for the markets in your configuration — add or remove anytime, the price adjusts. Weekly Brief personalised to your markets, CSV exports, role lens and watchlist included.</div>
      </div>
    </div>'''),

# 7. premium list note
P('· early access to new analytical tools as they ship.</div>',
'''· early access to new analytical tools as they ship. <b>Modular:</b> ₹999/month per market — the Brief personalised to your markets. <b>Custom research:</b> menu-priced per request, from Account settings.</div>'''),

# 8. show() gains v-configure
P("""function show(id){['v-welcome','v-signin','v-create','v-payment','v-settings'].forEach(function(v){V(v).classList.toggle('on',v===id)})}""",
"""function show(id){['v-welcome','v-signin','v-create','v-payment','v-settings','v-configure'].forEach(function(v){V(v).classList.toggle('on',v===id)})}"""),

# 9. personalisation JS block before eye toggles
P('''/* ---------- Eye toggles ---------- */''',
'''/* ---------- Personalisation (markets, role, theme, watchlist) ---------- */
var MARKETS=['india','apac','rails','europe','namerica','mideast'];
var MKNAME={india:'🇮🇳 India',apac:'🌏 APAC',rails:'🧬 New Rails & Digital',europe:'🇪🇺 Europe',namerica:'🇺🇸 North America',mideast:'🕌 Middle East'};
var ROLES=[['sales','Sales'],['presales','Presales & Solutions'],['ops','Operations & Servicing'],['tech','Technology'],['leadership','Leadership']];
var THEMES={classic:['#C08A2D','#E3B45C'],teal:['#2C7A74','#4FB3AB'],violet:['#5B4A8A','#9C8CD6'],emerald:['#1F7A4D','#57C28A']};
var TRIGNAMES=['SIF_SCALE_ACCELERATION','NEW_SIF_MANAGER','NEW_CUSTODIAN_ENTRANT','ETF_RECORD_FLOWS','ADGM_GROWTH_SURGE','QFI_REMOVAL_COMPLETED','HSBC_EU_CUSTODY_EXIT','JAPAN_RECORD_AUM','AI_COST_CURVE_RESET','KINEXYS_SCALE','REC_TOKENISED_BOND','DORA_ENFORCEMENT','AIFMD_II_LPD','SEC_CUSTODY_RULE','PIF_INTERNATIONALISATION','T_PLUS_ONE_AFTERMATH'];
function getPrefs(){try{var p=JSON.parse(localStorage.getItem('gscc_prefs')||'null');return p||{}}catch(e){return{}}}
function savePrefs(p){localStorage.setItem('gscc_prefs',JSON.stringify(p))}
function applyTheme(t){var th=THEMES[t]||THEMES.classic;document.documentElement.style.setProperty('--gold',th[0]);document.documentElement.style.setProperty('--gold-bright',th[1])}
function updTotal(){
  var n=V('mk-grid').querySelectorAll('input:checked').length;
  V('cfg-total').innerHTML='Modular price: <b>₹'+(n===0?0:n*999).toLocaleString('en-IN')+'/month</b> for '+n+' market'+(n===1?'':'s')+' · Professional (all markets + Executive View): <b>₹2,999/month</b>'+(n>2?' — better value':'');
}
function renderConfigure(){
  var p=getPrefs(),sel=(p.markets&&p.markets.length)?p.markets:MARKETS.slice();
  V('mk-grid').innerHTML=MARKETS.map(function(m){return '<label class="mk"><input type="checkbox" data-mk="'+m+'"'+(sel.indexOf(m)>-1?' checked':'')+'><span>'+MKNAME[m]+'</span></label>'}).join('');
  V('role-row').innerHTML=ROLES.map(function(r){return '<button class="rpill'+(p.role===r[0]?' on':'')+'" data-role="'+r[0]+'">'+r[1]+'</button>'}).join('');
  V('theme-row').innerHTML=Object.keys(THEMES).map(function(k){return '<button class="swatch'+((p.theme||'classic')===k?' on':'')+'" data-th="'+k+'" title="'+k+'" style="background:'+THEMES[k][0]+'"></button>'}).join('');
  V('watch-grid').innerHTML=TRIGNAMES.map(function(t){return '<label class="mk sm"><input type="checkbox" data-tr="'+t+'"'+(((p.watch)||[]).indexOf(t)>-1?' checked':'')+'><span>'+t+'</span></label>'}).join('');
  updTotal();
  V('mk-grid').querySelectorAll('input').forEach(function(i){i.onchange=updTotal});
  V('role-row').querySelectorAll('button').forEach(function(b){b.onclick=function(){V('role-row').querySelectorAll('button').forEach(function(x){x.classList.remove('on')});b.classList.add('on')}});
  V('theme-row').querySelectorAll('button').forEach(function(b){b.onclick=function(){V('theme-row').querySelectorAll('button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');applyTheme(b.getAttribute('data-th'))}});
  show('v-configure');
}
V('cf-save').onclick=function(){
  var mk=[].map.call(V('mk-grid').querySelectorAll('input:checked'),function(i){return i.getAttribute('data-mk')});
  var roleB=V('role-row').querySelector('.rpill.on'),thB=V('theme-row').querySelector('.swatch.on');
  var watch=[].map.call(V('watch-grid').querySelectorAll('input:checked'),function(i){return i.getAttribute('data-tr')});
  var m=V('cf-msg');m.className='msg';
  if(!mk.length){m.className='msg err';m.textContent='Select at least one market — or choose Professional for everything.';return}
  savePrefs({markets:mk,role:roleB?roleB.getAttribute('data-role'):'',theme:thB?thB.getAttribute('data-th'):'classic',watch:watch});
  location.href='index.html';
};
V('w-config').onclick=renderConfigure;
V('st-config').onclick=renderConfigure;

/* ---------- Eye toggles ---------- */'''),

# 10. boot: apply theme
P('''/* ---------- Boot ---------- */
var st=accountState();''',
'''/* ---------- Boot ---------- */
var st=accountState();
applyTheme(getPrefs().theme);'''),

# 11. boot hash: configure
P("if(location.hash==='#payment'&&st.mode!=='active'){show('v-payment')}",
"""if(location.hash==='#payment'&&st.mode!=='active'){show('v-payment')}
if(location.hash==='#configure'&&st.mode==='active'){renderConfigure()}"""),

# 12. founder create redirect
P('''        saveUsers(users);startSession(uid);location.href='index.html';''',
  '''        saveUsers(users);startSession(uid);location.href='login.html#configure';'''),

# 13. trial create redirect
P('''    saveUsers(users);startSession(uid);location.href='index.html';''',
  '''    saveUsers(users);startSession(uid);location.href='login.html#configure';'''),

# 14. upi-open modular price
P('''  var sel=document.querySelector('.plan.sel'),am=sel?sel.getAttribute('data-price'):'';''',
'''  var sel=document.querySelector('.plan.sel'),am=sel?sel.getAttribute('data-price'):'';
  if(sel&&sel.getAttribute('data-plan')==='modular'){var mkp=(getPrefs().markets||MARKETS);am=String(999*Math.max(1,mkp.length));}'''),

# 15. pay-go modular handling
P('''  var sel=document.querySelector('.plan.sel'),days=parseInt(sel.getAttribute('data-days'),10),plan=sel.getAttribute('data-plan');''',
'''  var sel=document.querySelector('.plan.sel'),days=parseInt(sel.getAttribute('data-days'),10)||30,plan=sel.getAttribute('data-plan');
  if(plan==='modular'){days=30;}'''),

# 16. record modular markets
P('''  a.plan=plan;a.planExpires=Date.now()+days*DAY;a.txnRef=ref;a.txnAt=Date.now();''',
'''  a.plan=plan;a.planExpires=Date.now()+days*DAY;a.txnRef=ref;a.txnAt=Date.now();
  if(plan==='modular'){a.markets=(getPrefs().markets||MARKETS).slice();}'''),
]

INDEX = [

P('<a class="module-card apac" href="india-asset-servicing-briefing.html">',
  '<a class="module-card apac" href="india-asset-servicing-briefing.html" data-market="india">'),
P('<a class="module-card apac" href="apac-asset-servicing-kb.html">',
  '<a class="module-card apac" href="apac-asset-servicing-kb.html" data-market="apac">'),
P('<a class="module-card apac" href="new-rails-dlt-ai-apac.html">',
  '<a class="module-card apac" href="new-rails-dlt-ai-apac.html" data-market="rails">'),
P('<a class="module-card eu" href="europe-asset-servicing-kb.html">',
  '<a class="module-card eu" href="europe-asset-servicing-kb.html" data-market="europe">'),
P('<a class="module-card na" href="north-america-asset-servicing-kb.html">',
  '<a class="module-card na" href="north-america-asset-servicing-kb.html" data-market="namerica">'),
P('<a class="module-card me" href="middle-east-asset-servicing-kb.html">',
  '<a class="module-card me" href="middle-east-asset-servicing-kb.html" data-market="mideast">'),
P('<a class="exec-card" href="executive-view.html">',
  '<a class="exec-card" href="executive-view.html" data-market="exec">'),

# your-edition container before module grid
P('  <div class="module-grid">',
'''  <div class="your-edition" id="your-edition" style="display:none"></div>

  <div class="module-grid">'''),

# personalisation style+script before </body>
P('</body>',
'''<style>
.your-edition{margin:14px 0 4px;background:rgba(192,138,45,.08);border:1px solid rgba(192,138,45,.3);border-radius:12px;padding:14px 18px}
.ye-kicker{font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-bright)}
.ye-markets{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.ye-markets span{background:rgba(14,27,44,.55);border:1px solid rgba(192,138,45,.35);border-radius:14px;padding:4px 12px;font-size:12.5px;color:var(--text)}
.ye-lens{font-size:13px;color:var(--muted);margin-top:8px}
.ye-watch{margin-top:8px;font-size:11.5px;color:var(--muted)}
.ye-watch span{display:inline-block;background:rgba(44,122,116,.15);border:1px solid rgba(79,179,171,.3);border-radius:4px;padding:2px 7px;margin:2px 4px 0 0;font-family:'IBM Plex Mono',monospace;font-size:9.5px;color:var(--teal-bright)}
.ye-more{font-size:12px;color:var(--muted);margin-top:8px}
.ye-more a{color:var(--gold-bright)}
</style>
<script>
(function(){
  var P=null;try{P=JSON.parse(localStorage.getItem('gscc_prefs')||'null')}catch(e){}
  var el0=document.getElementById('your-edition');
  if(!P||!P.markets){if(el0){el0.style.display='block';el0.innerHTML='<div class="ye-kicker">Personalise</div><div class="ye-lens">Choose your markets, role lens, theme and trigger watchlist — <a href="login.html#configure">configure your edition</a>.</div>'}return}
  var TH={classic:['#C08A2D','#E3B45C'],teal:['#2C7A74','#4FB3AB'],violet:['#5B4A8A','#9C8CD6'],emerald:['#1F7A4D','#57C28A']};
  if(P.theme&&TH[P.theme]){document.documentElement.style.setProperty('--gold',TH[P.theme][0]);document.documentElement.style.setProperty('--gold-bright',TH[P.theme][1])}
  var el=el0;if(!el)return;
  var ALL=['india','apac','rails','europe','namerica','mideast'];
  var NAME={india:'🇮🇳 India',apac:'🌏 APAC',rails:'🧬 New Rails',europe:'🇪🇺 Europe',namerica:'🇺🇸 North America',mideast:'🕌 Middle East'};
  var LENS={sales:'Mandate-flow lens: who is moving, and why.',presales:'Trigger-first lens: what is buyable now.',ops:'Run-the-bank lens: regulatory and operational load.',tech:'Rails-first lens: DLT, AI and new infrastructure.',leadership:'Board lens: allocation, thesis and triggers.'};
  var known=P.markets.filter(function(m){return ALL.indexOf(m)>-1});
  if(!known.length)return;
  document.querySelectorAll('.module-card').forEach(function(c){if(known.indexOf(c.getAttribute('data-market'))<0)c.style.display='none'});
  var hidden=ALL.length-known.length;
  el.innerHTML='<div class="ye-kicker">Your edition</div><div class="ye-markets">'+known.map(function(m){return '<span>'+NAME[m]+'</span>'}).join('')+'</div>'+
    (P.role&&LENS[P.role]?'<div class="ye-lens">'+LENS[P.role]+'</div>':'')+
    ((P.watch&&P.watch.length)?'<div class="ye-watch"><b style="color:var(--teal-bright)">Watchlist:</b> '+P.watch.map(function(w){return '<span>'+w+'</span>'}).join('')+'</div>':'')+
    (hidden>0?'<div class="ye-more">'+hidden+' more module'+(hidden>1?'s':'')+' available — <a href="login.html#configure">add markets anytime</a></div>':'<div class="ye-more"><a href="login.html#configure">Adjust markets, role lens, theme or watchlist</a></div>');
  el.style.display='block';
})();
</script>
</body>'''),

# modular pricing card after Team plan
P('''        <li>Quarterly market brief (PDF)</li>
      </ul>
      <a class="p-btn ghost" href="login.html">Start free month</a>
    </div>
  </div>''',
'''        <li>Quarterly market brief (PDF)</li>
      </ul>
      <a class="p-btn ghost" href="login.html">Start free month</a>
    </div>
    <div class="plan">
      <div class="p-name">Modular · Build your own</div>
      <div class="p-price">₹999 <small>/ market / month</small></div>
      <div class="p-save">Pay only for the markets you cover</div>
      <ul>
        <li>Choose your markets — add or remove anytime, price adjusts</li>
        <li>The Weekly Brief, personalised to your markets</li>
        <li>Role lens, theme & trigger watchlist</li>
        <li>CSV data exports</li>
        <li>All modules à la carte = ₹5,994 — beyond two markets, Professional is better value</li>
      </ul>
      <a class="p-btn ghost" href="login.html#configure">Configure my markets</a>
    </div>
  </div>'''),
]

# ---- auth-gate.js: full rewrite ----
with open('auth-gate.js', 'w', encoding='utf-8') as f:
    f.write(GATE_V3)
print('auth-gate.js: v3 written,', len(GATE_V3), 'chars')

# ---- patch login.html and index.html ----
ok = True
for fname, patches in (('login.html', LOGIN), ('index.html', INDEX)):
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
