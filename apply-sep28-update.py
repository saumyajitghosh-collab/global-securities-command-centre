#!/usr/bin/env python3
# GSCC weekly data update — 28 Sep 2026
# India: SIF pipeline (AlphaGrep 14 Oct, Axis + HDFC preparing, Tata AAA NFO).
# Executive View: NEW_SIF_MANAGER trigger desc/proposition updated.
# New Rails: Sep 2026 timeline event (ChinaAMC tokenised-deposit MMF,
#   Wellington/Midas mWIN, ARK-Securitize, Malaysia UMYR).
# Europe: Standish acquires NCM Fund Services.
import sys

def P(old, new):
    return (old, new)

# ---------------- India module ----------------
INDIA = [
P('wrapper stack. The SEBI board meeting of 24 Sep',
  'wrapper stack. The queue is lengthening: AlphaGrep Mutual Fund launches its Eminence Hybrid Long-Short Fund on 14 Oct 2026, and Axis MF and HDFC MF are both preparing SIF entries — while Tata\u2019s Titanium Active Asset Allocator Long-Short NFO (opened 23 Sep, closes 7 Oct) adds a multi-asset strategy able to run equity 35\u2013100%, debt up to 65%, commodity derivatives up to 30% and unhedged shorts up to 25% — servicing-heavy by design. The SEBI board meeting of 24 Sep'),
]

# ---------------- Executive View ----------------
EXEC = [
P("wrapper stack.',\n  p:'Cross-wrapper servicing opportunity: one architecture across four regulatory wrappers \u2014 flag Abakkus/Fokkus for account development.',\n  m:'Abakkus release \u00b7 SEBI \u00b7 Sep 2026'",
  "wrapper stack. The queue is lengthening: AlphaGrep launches its Eminence Hybrid Long-Short Fund on 14 Oct 2026, and Axis MF and HDFC MF are preparing entries (28 Sep reports).',\n  p:'Cross-wrapper servicing opportunity: one architecture across four regulatory wrappers \u2014 flag Abakkus/Fokkus for account development, and pre-position with AlphaGrep, Axis and HDFC before their SIF stacks are bought.',\n  m:'Abakkus release \u00b7 SEBI \u00b7 Cafemutual \u00b7 Sep 2026'"),
]

# ---------------- New Rails module ----------------
RAILS = [
P('<div class="ev t"><div class="d">NOV 2026</div><h5>KRX Novel Securities Market opens (16 Nov)</h5>',
  '<div class="ev t"><div class="d">SEP 2026</div><h5>Tokenised funds go institutional: ChinaAMC deposit-tokenised MMF \u00b7 Wellington/Midas mWIN \u00b7 ARK onchain</h5><p>ChinaAMC (HK)\u2019s digital money-market fund now runs on tokenised deposits \u2014 HSBC rails, Standard Chartered custody, an Asia-Pacific first that extends Ensemble into a live retail fund. Midas + Wellington ($1.3T AUM) launched mWIN, an actively managed tokenised credit strategy via a Luxembourg securitisation vehicle on Ethereum, with Northern Trust as custodian and independent NAV pricer. ARK tokenised its Venture Fund with Securitize. Malaysia\u2019s Luno\u2013Halogen\u2013Kenanga trio is exploring a ringgit stablecoin for tokenised-MMF DvP settlement. <span class="tag fact">FACT</span></p><div class="so"><b>Sell:</b> the tokenised-fund servicing stack (custody + NAV + register + collateral) now has lighthouse buy-side names attached \u2014 lead with them in every DLT-curious account.</div></div>\n    <div class="ev t"><div class="d">NOV 2026</div><h5>KRX Novel Securities Market opens (16 Nov)</h5>'),
]

# ---------------- Europe module ----------------
EUROPE = [
P('emerging as infrastructure partners, not direct competitors. <span class="tag fact">FACT</span></p></div>',
  'emerging as infrastructure partners, not direct competitors. <b>Standish</b> agreed on 24 Sep 2026 to acquire NCM Fund Services (Edinburgh, London, Jersey, Guernsey), adding AIFM, depositary and operator services; post-close Standish runs 1,300+ staff and ~$900bn AUA &mdash; private-capital fund-admin consolidation rolls on. <span class="tag fact">FACT</span></p></div>'),
]

# ---- apply ----
ok = True
for fname, patches in (('india-asset-servicing-briefing.html', INDIA),
                       ('executive-view.html', EXEC),
                       ('new-rails-dlt-ai-apac.html', RAILS),
                       ('europe-asset-servicing-kb.html', EUROPE)):
    try:
        with open(fname, encoding='utf-8') as f:
            c = f.read()
    except FileNotFoundError:
        print(f'FAIL: {fname} not found'); ok = False; continue
    applied = 0
    for old, new in patches:
        if old in c:
            c = c.replace(old, new, 1); applied += 1
        else:
            print(f'FAIL: {fname}: anchor not found: {old[:70]!r}...'); ok = False
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{fname}: {applied}/{len(patches)} patches applied')

sys.exit(0 if ok else 1)
