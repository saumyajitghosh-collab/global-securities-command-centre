#!/usr/bin/env python3
# GSCC data update — 24 Sep 2026: Abakkus/Fokkus SIF entry
# Thesis upgrade: SIF = new servicing segment between MF and alternatives.
import sys

def P(old, new):
    return (old, new)

PATCHES = {

'india-asset-servicing-briefing.html': [
    P('folios up from ~94,000 to 125,000+. Derivatives-enabled long-short and hybrid strategies create servicing requirements (collateral, margin, derivatives lifecycle, exposure monitoring) far beyond vanilla MF ops.</li>',
      'folios up from ~94,000 to 125,000+ (+35% MoM). Derivatives-enabled long-short and hybrid strategies create servicing requirements (collateral, margin, derivatives lifecycle, exposure monitoring) far beyond vanilla MF ops. Abakkus entered on 22 Sep 2026 with its Fokkus platform — the first manager committing to the full MF → SIF → PMS → AIF wrapper stack.</li>'),
    P('Target universe: AMCs launching SIF franchises, incumbent MF custodians, fund accountants, collateral/margin providers, RTAs and middle-office providers. <span class="tag">ASSESSMENT</span></div>',
      'Target universe: AMCs launching SIF franchises, incumbent MF custodians, fund accountants, collateral/margin providers, RTAs and middle-office providers. <b>Thesis upgraded: SIF is no longer an emerging product opportunity — it is a new servicing segment sitting between traditional mutual funds and alternatives, and it warrants a dedicated servicing proposition rather than being treated as another mutual-fund scheme.</b> First cross-wrapper proof point: Abakkus (22 Sep 2026) — SEBI approval (28 Aug) for its SIF platform <b>Fokkus</b> across equity, debt and hybrid strategies, announced the same day it filed its DRHP (group managed assets ₹40,000+ cr; mutual-fund book ₹10,000+ cr; KFin as registrar). Trigger: <b>NEW_SIF_MANAGER → cross-wrapper servicing opportunity</b> — one operating architecture across four regulatory wrappers (custody, NAV, derivatives servicing, collateral, IBOR, reconciliation, regulatory reporting, RTA integration) instead of four stacks. Flag Abakkus/Fokkus for account development. Strategy details are not yet disclosed — do not infer derivative intensity prematurely; the cross-wrapper operating-model conversation is sellable today. <span class="tag fact">FACT</span> <span class="tag assess">ASSESSMENT</span></div>'),
],

'executive-view.html': [
    P("d:'SIF net assets ₹31,175 cr in Aug 2026 — more than doubled from ₹13,814 cr in May. ₹7,699 cr net inflows in one month; folios 94k → 125k+.',",
      "d:'SIF net assets ₹31,175 cr in Aug 2026 (+35% MoM) — more than doubled from ₹13,814 cr in May. ₹7,699 cr net inflows in one month; folios 94k → 125k+.',"),
    P("m:'AMFI monthly SIF data · Aug 2026'},",
      "m:'AMFI monthly SIF data · Aug 2026'},\n {n:'NEW_SIF_MANAGER',s:'fired',reg:'India',\n  d:'Abakkus approved 28 Aug 2026 for its SIF platform Fokkus (equity, debt, hybrid) and announced it 22 Sep alongside its DRHP — group AUM ₹40,000+ cr, MF book ₹10,000+ cr. First manager committing to the full MF → SIF → PMS → AIF wrapper stack.',\n  p:'Cross-wrapper servicing opportunity: one architecture across four regulatory wrappers — flag Abakkus/Fokkus for account development.',\n  m:'Abakkus release · SEBI · Sep 2026'},"),
    P('A single AMC SIF mandate is a bankable reference for the entire derivatives-servicing stack.',
      'A single AMC SIF mandate is a bankable reference for the entire derivatives-servicing stack — and the archetype target is already visible: Abakkus/Fokkus, a listing-bound manager building the four-wrapper stack (MF → SIF → PMS → AIF) from scratch.'),
    P('AMC SIF franchises need collateral, margin, derivatives lifecycle and exposure monitoring from day one.</li>',
      'AMC SIF franchises need collateral, margin, derivatives lifecycle and exposure monitoring from day one. First named account-development target: Abakkus/Fokkus — the first full cross-wrapper SIF manager (Sep 2026).</li>'),
    P('Fourteen trigger conditions from across the modules, ranked by status.',
      'Fifteen trigger conditions from across the modules, ranked by status.'),
],

'index.html': [
    P('<div class="stat"><div class="v">14</div><div class="l">MANDATE TRIGGERS</div></div>',
      '<div class="stat"><div class="v">15</div><div class="l">MANDATE TRIGGERS</div></div>'),
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
