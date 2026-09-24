#!/usr/bin/env python3
# GSCC data update — 24 Sep 2026 (evening edition)
# Motilal custodian entry, SIF Intelligence detail, SEBI board watch, Qatar-Apex hub,
# HSBC Al Rajhi ETF custody, NT Singapore unit trusts, Warwickshire, SocGen-Ultumus, SC-LMAX.
import sys

def P(old, new):
    return (old, new)

PATCHES = {

'india-asset-servicing-briefing.html': [
    P('''<div class="metric"><div class="n">17</div><div class="l">SEBI-registered custodians competing for FPI, MF, AIF and insurance custody — foreign banks and domestic banks alike.</div><div class="asof">SEBI registry</div></div>''',
      '''<div class="metric"><div class="n">18</div><div class="l">SEBI-registered custodians competing for FPI, MF, AIF and insurance custody — foreign banks, domestic banks and broker-led entrants alike; Motilal Oswal is the newest (approved 23 Sep 2026).</div><div class="asof">SEBI registry</div></div>'''),
    P('''Stock Holding Corporation and Orbis compete hard on price); and <b>clearing/settlement services</b>''',
      '''Stock Holding Corporation and Orbis compete hard on price — joined by Motilal Oswal's new custodian subsidiary, approved 23 Sep 2026 with operations from Q4 2026); and <b>clearing/settlement services</b>'''),
    P('''Winning the DDP relationship at fund inception locks in custody — which makes FPI custody a land-grab at the point of India market entry.</p>''',
      '''Winning the DDP relationship at fund inception locks in custody — which makes FPI custody a land-grab at the point of India market entry.</p>
    <div class="note" style="margin:18px 0"><b>New custodian entrant → greenfield platform buyer.</b> Motilal Oswal Custodial Services (a wholly owned subsidiary of MOFSL) received SEBI approval on 23 Sep 2026 to act as custodian of securities — safekeeping, trade settlement, corporate-action processing and regulatory reporting for AIFs, PMS, mutual funds, insurers and pension funds, with operations commencing in Q4 2026. A new licensed custodian is a greenfield infrastructure buyer: the core custody platform, fund-accounting stack, depository connectivity and compliance tooling are all bought before the first client lands. Trigger: <b>NEW_CUSTODIAN_ENTRANT → platform & infrastructure build-out</b> — the build-out window is now, and it precedes any market-share shift. <span class="tag fact">FACT</span> <span class="tag assess">ASSESSMENT</span></div>'''),
    P('''₹7,699 cr net inflows in a single month; folios up from ~94,000 to 125,000+ (+35% MoM).''',
      '''₹7,699 cr net inflows in a single month; folios up from ~94,000 to 125,000+ (+35% MoM); 33 schemes across 17 AMCs; AUM up 528% from ₹4,928 cr in January, with hybrid strategies driving 60% of net inflows and the category completing its first year on 17 Sep (SIF Intelligence Report, Sep 2026).'''),
    P('''the first manager committing to the full MF → SIF → PMS → AIF wrapper stack.</li>''',
      '''the first manager committing to the full MF → SIF → PMS → AIF wrapper stack. The SEBI board meeting of 24 Sep was set to consider a PMS overhaul — including an MF-PMS category investing in direct MF plans, ETFs and SIFs with the minimum ticket halved to ₹25 lakh — which would widen the cross-wrapper universe further.</li>'''),
],

'middle-east-asset-servicing-kb.html': [
    P('''<h4>HSBC</h4><p>Saudi AUC $86B &rarr; $224B in 2025 (~35% share); 7 of 10 largest Saudi AMs on the network.</p>''',
      '''<h4>HSBC</h4><p>Saudi AUC $86B &rarr; $224B in 2025 (~35% share) &rarr; $235B by Mar 2026; custodian to the Al Rajhi MSCI Saudi Arabia ETF (Sep 2026); 7 of 10 largest Saudi AMs on the network.</p>'''),
    P('''named "Middle East's best for securities services 2026" (Euromoney)</td>''',
      '''named "Middle East's best for securities services 2026" (Euromoney); $235B AUC in KSA by Mar 2026 and custodian to the Al Rajhi MSCI Saudi Arabia ETF (14 Sep 2026)</td>'''),
    P('''<tr><td><b>BNY</b></td><td>Digital-asset custody in Abu Dhabi via Finstreet partnership (May 2026)</td><td class="mono">First-mover in regulated digital custody, ME</td></tr>''',
      '''<tr><td><b>BNY</b></td><td>Digital-asset custody in Abu Dhabi via Finstreet partnership (May 2026)</td><td class="mono">First-mover in regulated digital custody, ME</td></tr>
      <tr><td><b>Apex Group</b></td><td>Strategic partnership with Invest Qatar (23 Sep 2026) for a regional asset-servicing hub in Lusail — first privately licensed financial firm in Lusail Boulevard; fund administration, digital-asset operations and tokenised structures on Apex Digital 3.0</td><td class="mono">Qatar buys a servicing hub · $3.5T AUA platform localises</td></tr>'''),
],

'apac-asset-servicing-kb.html': [
    P('''Even BlackRock has been recruiting a Transfer Agency Services Director APAC in Singapore — a demand signal from the very top of the market.</div>''',
      '''Even BlackRock has been recruiting a Transfer Agency Services Director APAC in Singapore — a demand signal from the very top of the market. September 2026: Northern Trust partnered with Perpetual (Asia) for full-cycle retail unit-trust servicing — custody, fund administration, middle office and TA, with independent trustee oversight — a month after expanding First Sentier's Singapore unit-trust administration. Integrated fund-servicing demand is broadening from alternatives into the retail fund base.</div>'''),
],

'europe-asset-servicing-kb.html': [
    P('''and Citi secured a US$380bn full middle-office mandate from Aegon Asset Management (13 Aug), scaling its Aladdin-provider model.''',
      '''and Citi secured a US$380bn full middle-office mandate from Aegon Asset Management (13 Aug), scaling its Aladdin-provider model. Northern Trust added a £3.6bn Warwickshire Pension Fund mandate (7 Sep) — global custody, valuation reporting, capital-call execution and performance measurement, a reference win into the 18-fund Border to Coast network; and Soci&eacute;t&eacute; G&eacute;n&eacute;rale SS appointed Ultumus (23 Sep) to streamline its ETF operations.'''),
],

'new-rails-dlt-ai-apac.html': [
    P('''Deutsche Bank debuts digital-asset custody in 2026. When the reference books move''',
      '''Deutsche Bank debuts digital-asset custody in 2026. Standard Chartered onboarded LMAX Group as the first client of its Luxembourg digital-asset custody platform (16 Sep 2026, after its MiCA authorisation in June), with a parallel DIFC appointment — extending bank-grade digital custody from the Gulf into the EU. When the reference books move'''),
],

'executive-view.html': [
    P('''p:'Cross-wrapper servicing opportunity: one architecture across four regulatory wrappers — flag Abakkus/Fokkus for account development.',
  m:'Abakkus release · SEBI · Sep 2026'},''',
      '''p:'Cross-wrapper servicing opportunity: one architecture across four regulatory wrappers — flag Abakkus/Fokkus for account development.',
  m:'Abakkus release · SEBI · Sep 2026'},
 {n:'NEW_CUSTODIAN_ENTRANT',s:'fired',reg:'India',
  d:'Motilal Oswal Custodial Services received SEBI approval (23 Sep 2026) — safekeeping, settlement, corporate actions and regulatory reporting for AIFs, PMS, MFs, insurers and pension funds; operations from Q4 2026.',
  p:'Greenfield platform buyer: core custody platform, fund accounting, connectivity and compliance tooling are all bought before the first client lands.',
  m:'Motilal Oswal release · SEBI · Sep 2026'},'''),
    P('Fifteen trigger conditions from across the modules',
      'Sixteen trigger conditions from across the modules'),
],

'index.html': [
    P('''<div class="stat"><div class="v">15</div><div class="l">MANDATE TRIGGERS</div></div>''',
      '''<div class="stat"><div class="v">16</div><div class="l">MANDATE TRIGGERS</div></div>'''),
],

'weekly-brief.html': [
    P('''the IFSC investor base grew 68% in the June quarter. <span class="tag fact">FACT</span>''',
      '''the IFSC investor base grew 68% in the June quarter. And Motilal Oswal received SEBI's nod to launch custodian services (23 Sep) — the first broker-led domestic entrant in years, and a greenfield platform buyer. <span class="tag fact">FACT</span>'''),
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
