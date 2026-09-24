/* GSCC Auth Gate v3 — session guard + device-tied trial + personalisation.
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
