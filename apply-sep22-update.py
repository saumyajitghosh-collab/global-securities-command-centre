#!/usr/bin/env python3
# GSCC data update — 22 Sep 2026 refresh
import sys

def P(old, new):
    return (old, new)

PATCHES = {

'india-asset-servicing-briefing.html': [
    P('<span class="val" data-count="85.76">0<em>₹ lakh cr</em></span>',
      '<span class="val" data-count="87.08">0<em>₹ lakh cr</em></span>'),
    P('₹85.76 <span>lakh cr</span></div><div class="l">Mutual fund AUM (~US$1 trillion). Grew from ₹15.18 lakh cr a decade ago — roughly 5.6x.</div><div class="asof">AMFI · Jul 31, 2026</div>',
      '₹87.08 <span>lakh cr</span></div><div class="l">Mutual fund AUM (~US$1 trillion). +₹1.3 lakh cr in August alone; record SIP ₹32,297 cr.</div><div class="asof">AMFI · Aug 31, 2026</div>'),
    P('~59 AMCs; AUM ₹85.76 lakh cr (Jul 2026), on course for ₹100 lakh cr within a couple of years if SIP momentum holds.',
      '~59 AMCs; AUM ₹87.08 lakh cr (Aug 2026, +1.5% MoM on record SIP flows of ₹32,297 cr), on course for ₹100 lakh cr within a couple of years.'),
    P('<span class="bl">MF AUM Jul 2026</span>', '<span class="bl">MF AUM Aug 2026</span>'),
    P('<span class="bn">₹85.8 L cr</span>', '<span class="bn">₹87.1 L cr</span>'),
    P('<span class="val" data-count="26.3">0<em>US$ bn</em></span>',
      '<span class="val" data-count="45.1">0<em>US$ bn</em></span>'),
    P('US$26.3 <span>bn</span></div><div class="l">Commitments raised by GIFT City (IFSC) funds — India\'s Singapore/Luxembourg play, with tax-neutral fund regimes.</div><div class="asof">IFSCA · Q4 2025</div>',
      'US$45.1 <span>bn</span></div><div class="l">Commitments raised by GIFT City (IFSC) funds — India\'s Singapore/Luxembourg play. FMEs at 235, live schemes 401, investor base +68% QoQ to 16,150.</div><div class="asof">IFSCA · Q1 FY27 (Jun 2026)</div>'),
    P('US$26.3 <span>bn</span></div><div class="l">Commitments raised by GIFT funds.</div><div class="asof">IFSCA · Q4 2025</div>',
      'US$45.1 <span>bn</span></div><div class="l">Commitments raised by GIFT funds — up from $39.1bn in Mar 2026; retail investor base +146% in the June quarter.</div><div class="asof">IFSCA · Q1 FY27 (Jun 2026)</div>'),
    P('industry AUM (₹85.76 lakh cr, Jul 2026', 'industry AUM (₹87.08 lakh cr, Aug 2026'),
],

'north-america-asset-servicing-kb.html': [
    P('$15.7T</div><div class="l">US ETF AUM as of May 2026, up from $10.3T at YE2024 <span class="tag fact">FACT</span></div><div class="s">ETFGI; ICI Fact Book 2025 Ch.4</div>',
      '$16.36T</div><div class="l">US ETF AUM at end-Aug 2026 — a record; +21.9% YTD from $13.43T at YE2025; 52nd consecutive month of net inflows <span class="tag fact">FACT</span></div><div class="s">ETFGI Aug 2026</div>'),
    P('$15.7T and compounding &mdash; the US hosts 71% of the global ETF market.',
      '$16.36T and compounding &mdash; the US hosts ~68% of the global ETF market.'),
    P('US ETF AUM grew from $10.3T (YE2024) to $15.7T (May 2026) on record inflows. Active ETFs are the fastest-growing segment ($313B inflows in 2024);',
      'US ETF AUM grew from $13.43T (YE2025) to a record $16.36T (Aug 2026) on record inflows — $1.41T YTD, 76.5% above the same period of 2025. Active ETFs are the fastest-growing segment ($529.96B inflows YTD);'),
    P('$15.7T</div><div class="l">US ETF AUM, May 2026 (up from $10.3T YE2024) <span class="tag fact">FACT</span></div><div class="s">ETFGI</div>',
      '$16.36T</div><div class="l">US ETF AUM, Aug 2026 (record; up from $13.43T YE2025) <span class="tag fact">FACT</span></div><div class="s">ETFGI</div>'),
    P('$1.12T</div><div class="l">Record US ETF net inflows in 2024; $837B YTD May 2026 <span class="tag fact">FACT</span></div><div class="s">ETFGI; ICI</div>',
      '$1.41T</div><div class="l">Record YTD US ETF net inflows through Aug 2026 (prior full-year record: $1.12T in 2024) <span class="tag fact">FACT</span></div><div class="s">ETFGI; ICI</div>'),
    P('US ETF AUM $10.3T&rarr;$15.7T.', 'US ETF AUM $13.4T&rarr;$16.4T YTD 2026.'),
    P('<b>Status as of Sep 2026: NOT YET FINALISED.</b> If adopted: &ge;$1B RAUM advisers get 12 months; others 18 months.',
      '<b>Status as of Sep 2026: NOT YET FINALISED.</b> A revised, crypto-specific custody rulemaking (&ldquo;Amendments to the Custody Rules&rdquo;) went to the White House OIRA for review on 25 Aug 2026, with a formal proposal targeted for Oct 2026 — narrower than the withdrawn Safeguarding Rule, recognising multi-sig/MPC custody, and turning on the &ldquo;qualified custodian&rdquo; definition (OCC-chartered trust banks stand to gain). If adopted: &ge;$1B RAUM advisers get 12 months; others 18 months.'),
],

'europe-asset-servicing-kb.html': [
    P('creating displaced-client pools.</p>',
      'creating displaced-client pools. <b>Update, Sep 2026:</b> the churn cuts both ways — HSBC won a £21bn RLAM Irish custody, depositary and fund-admin mandate off State Street (17 Sep), and Citi secured a US$380bn full middle-office mandate from Aegon Asset Management (13 Aug), scaling its Aladdin-provider model. <span class="tag fact">FACT</span></p>'),
],

'middle-east-asset-servicing-kb.html': [
    P('ADGM FSRA Consultation Paper No. 12 of 2025 proposes lighter regimes for Small Threshold Fund Managers (',
      'ADGM FSRA finalised these enhancements on 16 Sep 2026 — lighter regimes for Sub-Threshold Fund Managers ('),
    P(' committed) and Institutional Fund Managers. <span class="tag fact">FACT</span>',
      ' committed) and Institutional Fund Managers are now live rules, with a transition window to 31 Mar 2027 for VCFMs and foreign fund managers. <span class="tag fact">FACT</span>'),
    P('Together they redefine who can buy, who must be local, and where digital assets sit. <span class="tag fact">FACT</span></p>',
      'Together they redefine who can buy, who must be local, and where digital assets sit. <b>Sep 2026:</b> the CMA capped overseas investments by public money-market funds at 5% of NAV (two-year compliance; funds above 20% get six months) — $20.5B of public MMF assets re-shore into domestic servicing. <span class="tag fact">FACT</span></p>'),
    P('Consultation Paper No. 12 of 2025 (Small Threshold & Institutional Fund Managers).',
      'Consultation Paper No. 12 of 2025, finalised as the New Funds Rules (16 Sep 2026).'),
],

'new-rails-dlt-ai-apac.html': [
    P('tokenised US Treasuries ≈ $15.1B <span class="tag fact">FACT</span></div><div class="s">RWA market trackers, May 2026</div>',
      'tokenised US Treasuries ≈ $15.9B <span class="tag fact">FACT</span></div><div class="s">RWA market trackers, Sep 2026</div>'),
    P('RWA ex-stablecoins ~$39.2B, Treasuries ~$15.1B (Sep 2026)',
      'RWA ex-stablecoins ~$39.2B, Treasuries ~$15.9B (Sep 2026)'),
],

'executive-view.html': [
    P('US ETF $15.7T from $10.3T in 18 months', 'US ETF at a record $16.36T (Aug 2026), +21.9% YTD'),
    P('India ₹85.76 lakh cr MF + ₹16.94 lakh cr AIF', 'India ₹87.08 lakh cr MF + ₹16.94 lakh cr AIF'),
    P('$15.7T US ETF market, $1.12T record 2024 inflows, active ETFs the fastest-growing segment ($313B)',
      '$16.36T US ETF market (record), $1.41T YTD inflows through Aug 2026, active ETFs the fastest-growing segment ($529.96B YTD)'),
    P('₹85.76L cr MF · ₹16.94L cr AIF · SIF ₹31,175 cr', '₹87.08L cr MF · ₹16.94L cr AIF · SIF ₹31,175 cr'),
    P('$60T+ · ETF $15.7T · privates $7.7T', '$60T+ · ETF $16.4T · privates $7.7T'),
    P('US ETF AUM $15.7T (May 2026) from $10.3T at YE2024; record $1.12T net inflows in 2024; active ETFs $313B and accelerating.',
      'US ETF AUM at a record $16.36T (end-Aug 2026) — 52nd consecutive month of net inflows; record $1.41T YTD inflows, 76.5% above the same period of 2025; active ETFs $529.96B YTD.'),
    P('SEC safeguarding/custody rule still pending — when it lands, every qualified-custodian conversation reopens.',
      'Crypto-specific custody amendments at OIRA review since 25 Aug 2026; formal proposal targeted Oct 2026. When it lands, every qualified-custodian conversation reopens.'),
    P('HSBC exiting European custody field while Northern Trust wins mandates — active mandate churn window.',
      'HSBC retreated from segments of European custody while Northern Trust wins mandates — then HSBC took a £21bn RLAM Irish mandate off State Street (Sep 2026): churn cuts both ways, and every displaced client is a switch pitch.'),
],

'index.html': [
    P('<span>₹85.76L Cr MF AUM</span>', '<span>₹87.08L Cr MF AUM</span>'),
    P('US fund industry $39.2T, ETFs $15.7T, retirement $49.1T.', 'US fund industry $39.2T, ETFs $16.4T (record), retirement $49.1T.'),
    P('<span>$15.7T ETFs</span>', '<span>$16.4T ETFs</span>'),
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
