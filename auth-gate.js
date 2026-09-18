/* GSCC Auth Gate — client-side session guard for static hosting.
   Runs synchronously in <head> of every protected page.
   Redirects unauthenticated / expired visitors to login.html. */
(function () {
  'use strict';
  var here = window.location.pathname.split('/').pop() || 'index.html';
  if (here === 'login.html' || here === 'auth-gate.js') return;

  var users = {}, session = null, acct = null;
  try { users = JSON.parse(localStorage.getItem('gscc_users') || '{}'); } catch (e) {}
  try { session = JSON.parse(localStorage.getItem('gscc_session') || 'null'); } catch (e) {}

  var now = Date.now();
  var sessionValid = session && session.uid && session.sessionExpires && session.sessionExpires > now;
  var accessValid = false, daysLeft = 0, plan = null;

  if (sessionValid && users[session.uid]) {
    acct = users[session.uid];
    if (acct.planExpires && acct.planExpires > now) {
      accessValid = true;
      daysLeft = Math.max(0, Math.ceil((acct.planExpires - now) / 86400000));
      plan = acct.plan || 'trial';
    }
  }

  if (!sessionValid || !accessValid) {
    // No valid session or access expired -> to the gate.
    var target = (!sessionValid) ? 'login.html' : 'login.html#payment';
    document.documentElement.style.display = 'none';
    window.location.replace(target);
    return;
  }

  // Expose session info for pages (badge, countdown, logout).
  window.GSCC_AUTH = {
    uid: session.uid,
    plan: plan,
    daysLeft: daysLeft,
    trial: plan === 'trial',
    logout: function () {
      localStorage.removeItem('gscc_session');
      window.location.replace('login.html');
    }
  };
})();
