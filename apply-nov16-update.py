#!/usr/bin/env python3
# GSCC weekly data update — 16 Nov 2026 (Edition No. 6, w/e 16 November 2026)
# 1. Replaces the "Weekly update" strip in the five KB modules; adds one to India.
# 2. Refreshes India Oct-2026 AMFI data (MF AUM, SIP, folios, SIF) + SEBI net settlement.
# 3. Refreshes North America (BNY 400+ AI solutions, Citi Custody+ numbers, BNY digital-asset custody).
# 4. Refreshes Europe (AIFMD II transposition patchwork, ESMA stablecoin opinion, DORA steady state).
# 5. Refreshes Middle East (Saudi CMA consultation to 20 Dec, UAE CMA 9M data, ADGM fund regime).
# 6. Refreshes New Rails (BUIDL as collateral, Securitize/Ethena facility, GL1 Org, RWA board).
# 7. Rewrites weekly-brief.html as Edition No. 6.
import re, sys

WEEK = 'week of 16 November 2026'

def block(items, sources):
    """Build the weekly-update strip markup."""
    lis = '\n'.join(
        '    <li style="font-size:13.5px;color:#1B2735;padding:9px 0;border-top:1px solid #EDF0F4">' + i + '</li>'
        for i in items)
    return (
      '<div style="margin:0 0 20px;background:#FFFFFF;border:1px solid #D9DFE7;border-left:4px solid #C08A2D;border-radius:10px;padding:20px 24px">\n'
      '  <div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:#C08A2D;margin-bottom:6px">Weekly update &middot; ' + WEEK + '</div>\n'
      '  <div style="font-family:\'Fraunces\',serif;font-size:20px;color:#0E1B2C;margin-bottom:4px">What moved this week</div>\n'
      '  <div style="font-size:12.5px;color:#5B6B7E;margin-bottom:12px">Figures below supersede the Sep&ndash;Oct 2026 baselines in this module. Verify before client use.</div>\n'
      '  <ul style="list-style:none;padding:0;margin:0">\n' + lis + '\n  </ul>\n'
      '  <div style="margin-top:12px;padding-top:10px;border-top:1px solid #EDF0F4;font-size:11.5px;color:#5B6B7E">Sources: ' + sources +
      ' &nbsp;<span style="font-family:\'IBM Plex Mono\',monospace;font-size:9px;letter-spacing:.08em;background:#E2EFED;color:#2C7A74;padding:2px 7px;border-radius:3px">FACT</span></div>\n'
      '</div>')

FACT = '<span style="font-family:\'IBM Plex Mono\',monospace;font-size:9px;background:#F3E9D4;color:#C08A2D;padding:2px 7px;border-radius:3px">ASSESSMENT</span>'

# ---------------------------------------------------------------- weekly strips
BLOCKS = {}

BLOCKS['apac-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">Project Guardian&rsquo;s shared ledger became a bank-run standards body.</b> On 4 November HSBC, Kinexys by J.P. Morgan, MUFG, Societe Generale FORGE and Standard Chartered launched the Global Layer One Organisation, taking GL1 out of MAS and into industry hands. The common ledger was never built &mdash; the founders would not give up IP &mdash; so the output is standards, toolkits and a Programmable Compliance architecture. MAS now appears only as a listed policymaker.',
 '<b style="color:#0E1B2C">Northern Trust won an Australian scheme mandate.</b> Appointed asset servicing provider to LeavePlus, Victoria&rsquo;s portable long service leave scheme, covering global custody, fund administration, investment accounting, performance measurement and compliance monitoring (27 October).',
 '<b style="color:#0E1B2C">Singapore has moved past the pilot stage in fund tokenisation.</b> Live tokenised funds now trade on regulated platforms, and since November 2025 the market has carried a MAS-authorised, retail-eligible fund whose share register is maintained on-chain. The open questions are structural, not technical: where the register sits, what a valid transfer is, who controls the keys and what settles against what.',
 '<b style="color:#0E1B2C">Sell it as:</b> GL1 shifting from infrastructure to standards means interoperability &mdash; not a common ledger &mdash; is the near-term outcome. Open on register-and-collateral interoperability work, and on the digital transfer agent model where the investment book of record stays off-chain. ' + FACT,
], 'Global Layer One (4 Nov 2026); Global Custodian (27 Oct 2026); MAS Guide on Tokenisation of Capital Markets Products; Apex Group (3 Nov 2026)')

BLOCKS['europe-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">AIFMD II transposition is a patchwork, not a date.</b> Seven months after the 16 April 2026 deadline a meaningful minority of member states still have not notified implementing measures: Portugal, Greece, Cyprus, Latvia and Estonia have notified nothing, and France&rsquo;s enabling ordinance has stalled with a National Assembly vote now targeted for late February 2027, leaving the AMF on a transitional regime. Germany has created a Special Purpose Lending Company concept; Croatia is the only state reported to have gold-plated.',
 '<b style="color:#0E1B2C">The real 2027 clock is reporting, not transposition.</b> ESMA&rsquo;s harmonised Annex IV technical standards are expected to apply from 16 April 2027, with new fields for delegation arrangements, staff resources, liquidity-management-tool use and loan origination &mdash; and AIFMD II brings UCITS management companies into formal supervisory reporting for the first time. Plan one programme, not two.',
 '<b style="color:#0E1B2C">ESMA told CASPs to withdraw non-compliant stablecoins.</b> The opinion of 8 October 2026 covers the full range of MiCA services and gives national regulators three months to require remediation of legacy exposures &mdash; so withdrawal bites around early January 2027. All transitional periods for existing CASPs expired on 1 July 2026.',
 '<b style="color:#0E1B2C">DORA is steady state, and that is the harder part.</b> The scramble to 17 January 2025 is over; the register of information on ICT third-party arrangements under Article 28 is where fund administrators and ManCos quietly fail. The ESAs&rsquo; 2027 work programme keeps CTPP oversight and feeds technical advice into the DORA review. ' + FACT,
], 'Legal 500 Q3 2026 EU funds update; ESMA opinion (8 Oct 2026); Sidley (11 Nov 2026); ESAs 2027 Work Programme (13 Oct 2026); DORA Reg. 2022/2554')

BLOCKS['north-america-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">The SEC custody rewrite enters its final comment weeks.</b> Comments on File S7-2026-35 close <b>7 December 2026</b>. The package keeps the Advisers Act rule&rsquo;s existing &ldquo;funds or securities&rdquo; coverage &mdash; it does not revive the 2023 Safeguarding Rule&rsquo;s asset-class expansion &mdash; while adding a state-trust-company crypto route, conditional adviser self-custody where no qualified custodian exists, a discretionary-trading exception and easier audit rules.',
 '<b style="color:#0E1B2C">BNY took a second digital-asset custody mandate.</b> The Invesco Galaxy Ethereum ETF signed a digital assets custody agreement with BNY Mellon on 6 November for an initial five-year term, auto-renewing annually, running alongside the trust&rsquo;s existing Coinbase arrangement. Two custodians, one asset &mdash; the diligence burden is the client&rsquo;s.',
 '<b style="color:#0E1B2C">The AI numbers are now auditable, not aspirational.</b> BNY&rsquo;s CEO put <b>more than 400 AI solutions in production</b> as of October (up from 300+), with about <b>150 digital employees</b>; AI addressed over 10% of custody settlement status inquiries in Q1 2026, investigated more than 80% faster than a year earlier. Citi published Custody+ metrics: Single Event Processing handles 80%+ of events once across the network, voluntary corporate actions up to <b>92% faster</b> in the US with <b>96% of events under two hours</b>, and AI tax-servicing automation cutting document processing by up to <b>70%</b> across 100,000+ withholding-tax reclaims a year.',
 '<b style="color:#0E1B2C">Sell it as:</b> permitted-custodian change is the one event that reopens the whole stack, and every US manager&rsquo;s custody committee will re-read its custodian list before 7 December. Pair it with the published AI metrics &mdash; cost curves beat demos in an RFP. ' + FACT,
], 'SEC File S7-2026-35; Sullivan &amp; Cromwell (22 Oct 2026); Invesco Galaxy Ethereum ETF Form 8-K (12 Nov 2026); BNY CEO remarks (Oct 2026); Citi Custody+ (5 Nov 2026)')

BLOCKS['middle-east-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">Riyadh is compounding the post-QFI opening.</b> The CMA opened a 30-day consultation on 20 November-close account procedures: a new category letting foreign individuals resident in GCC states invest directly in the Main Market, direct access for non-profit organisations and endowment funds, retained access for former Saudi and GCC residents, and simplified account opening across client types. A parallel consultation covers retail investment-fund rules and a governance overhaul giving 5%-voting holders more board leverage (out since 29 October).',
 '<b style="color:#0E1B2C">UAE CMA is licensing faster and the domestic fund pool is deepening.</b> 68 new companies licensed in 9M 2026 with 30+ applications under review; a target to decide complete licensing applications in <b>seven working days</b>; domestic investment funds up <b>94% year on year to 97</b> with AUM up <b>30% to AED 28.6bn</b>. An Investor Protection Fund, systemically-important-entity rules and PJSC demerger rules are targeted for end-2026.',
 '<b style="color:#0E1B2C">ADGM&rsquo;s graduated manager regime is now the structuring decision.</b> AUM grew <b>54% year on year in H1 2026</b>; fund and asset managers rose from 154 to <b>190</b> and funds from 209 to <b>276</b>, with managers established there overseeing more than <b>US$2.1trn</b> of global assets. The FSRA&rsquo;s Institutional Fund Manager and Sub-Threshold Fund Manager categories took effect 16 September 2026; existing VCFMs and foreign fund managers have until <b>31 March 2027</b> to comply &mdash; and foreign managers must now appoint an FSRA-licensed administrator and a UAE-resident director.',
 '<b style="color:#0E1B2C">Sell it as:</b> every relaxation adds an investor segment that needs account opening, custody, brokerage and reporting plumbing, and direct ownership replaces synthetic swap exposure &mdash; assets move onto the exchange register and into local custodian hands. Run the 31 March 2027 ADGM compliance date as a fund-admin and TA trigger. ' + FACT,
], 'Saudi CMA consultations (29 Oct &amp; Nov 2026); UAE CMA (3 &amp; 9 Nov 2026); ADGM / Abu Dhabi Media Office (29 Oct 2026); FSRA Fund Rulebook amendments (16 Sep 2026)')

BLOCKS['new-rails-dlt-ai-apac.html'] = block([
 '<b style="color:#0E1B2C">Tokenised collateral became an operating model.</b> Eligible OKX institutional clients can post BlackRock&rsquo;s BUIDL as collateral while they trade, under a framework Standard Chartered announced in April &mdash; the posted tokens stay in Standard Chartered custody and keep earning dollar yield. One instrument now has two custody layers: BNY Mellon for the fund&rsquo;s underlying assets, Standard Chartered for the posted tokens.',
 '<b style="color:#0E1B2C">A 24/7 liquidity facility went live behind it.</b> Securitize and Ethena activated a $100m facility on 12 November, launching with $50m ($25m USDC / $25m BUIDL) and able to add $50m within the hour, letting eligible investors move between BUIDL and stablecoins outside market hours. Haircuts and eligible chains were not disclosed.',
 '<b style="color:#0E1B2C">BUIDL&rsquo;s on-chain value fell faster than any product on the board.</b> Down <b>17.9% to $1.66bn</b> between 3 and 11 November ($360.9m lost), slipping from fourth to sixth, while Franklin Templeton&rsquo;s BENJI added $325m (+35.5%) and the 50-product board moved only &minus;0.6% organically. The distributed RWA board measured <b>$21.35bn</b> across 53 products, of which tokenised Treasuries and government securities are $10.40bn.',
 '<b style="color:#0E1B2C">Sell it as:</b> collateral-grade token diligence is a new sale. Ask every client posting tokenised fund units for margin four questions &mdash; which custodian holds the token, what the haircut policy is, how the two registers reconcile, and who can move the asset during a margin call. ' + FACT,
], 'Standard Chartered / OKX (28 Apr &amp; Nov 2026); Securitize&ndash;Ethena release (12 Nov 2026); RWAWeekly board (13 Nov 2026)')

INDIA_BLOCK = block([
 '<b style="color:#0E1B2C">October was stabilisation, not a rebound.</b> AMFI net AUM <b>&#8377;83.39 lakh crore</b> at 31 October, up 0.9% on September&rsquo;s &#8377;82.64 lakh crore; AAUM &#8377;85.18 lakh crore. Net industry inflows swung to <b>&#8377;1.74 lakh crore</b> from a &#8377;1.33 lakh crore outflow, carried by &#8377;1.13 lakh crore back into liquid and overnight debt funds. Equity inflows moderated 13.9% to <b>&#8377;32,994 crore</b> &mdash; still the 68th consecutive positive month &mdash; and equity AUM slipped to &#8377;37.15 lakh crore on mark-to-market.',
 '<b style="color:#0E1B2C">SIPs held above &#8377;32,000 crore for a third month.</b> SIP contribution <b>&#8377;32,160 crore</b> from <b>9.99 crore</b> contributing accounts; SIP assets <b>&#8377;17.68 lakh crore</b>, or 21.2% of industry AUM, up 8.8% year on year. Folios rose a net 15.80 lakh to <b>28.78 crore</b>.',
 '<b style="color:#0E1B2C">SIFs cleared &#8377;42,000 crore.</b> SIF assets reached <b>&#8377;42,669.52 crore</b> in October on <b>&#8377;5,150.41 crore</b> of positive inflows driven by hybrid and equity-oriented strategies, with three new strategies launched mobilising &#8377;679 crore. That is roughly 21 times the &#8377;2,010 crore of October 2025 in the category&rsquo;s first year.',
 '<b style="color:#0E1B2C">SEBI took settlement risk out of the MF cash leg.</b> A circular dated 5 November 2026 sets a framework for net settlement of funds for transactions undertaken by mutual fund schemes in the cash market &mdash; a funding and reconciliation change that lands on custodians and fund accountants, not just on members. ' + FACT,
], 'AMFI monthly data (11 Nov 2026); SEBI circular (5 Nov 2026)')

# ---------------------------------------------------------------- apply strips
WEEKLY_START = '<div style="margin:0 0 20px;background:#FFFFFF;border:1px solid #D9DFE7;border-left:4px solid #C08A2D;border-radius:10px;padding:20px 24px">'
WEEKLY_END = re.compile(r'<div style="margin-top:12px;padding-top:10px;border-top:1px solid #EDF0F4;font-size:11\.5px;color:#5B6B7E">Sources:.*?</div>\s*</div>', re.S)

def swap_strip(html, new):
    i = html.find(WEEKLY_START)
    if i < 0:
        return html, False
    m = WEEKLY_END.search(html, i)
    if not m:
        return html, False
    return html[:i] + new + html[m.end():], True

# ---------------------------------------------------------------- India data
INDIA = [
 # ledger row values
 ('data-count="82.64">0<em>\u20b9 lakh cr</em>', 'data-count="83.39">0<em>\u20b9 lakh cr</em>'),
 ('data-count="32490" data-int="1"', 'data-count="32160" data-int="1"'),
 ('data-count="27.39">0<em>crore</em>', 'data-count="28.78">0<em>crore</em>'),
 # glance metric
 ('<div class="n">\u20b982.64 <span>lakh cr</span></div><div class="l">Mutual fund AUM (~US$1 trillion). &minus;\u20b94.4 lakh cr in September on a \u20b91.83 lakh cr debt outflow and mark-to-market losses; record SIP \u20b932,490 cr.</div><div class="asof">AMFI \u00b7 Sep 30, 2026</div>',
  '<div class="n">\u20b983.39 <span>lakh cr</span></div><div class="l">Mutual fund AUM (~US$1 trillion). Up 0.9% in October on a \u20b91.74 lakh cr net inflow swing, carried by \u20b91.13 lakh cr back into liquid and overnight funds; equity inflows \u20b932,994 cr; SIP \u20b932,160 cr.</div><div class="asof">AMFI \u00b7 Oct 31, 2026</div>'),
 # fund-admin card
 ('<li>~59 AMCs; AUM \u20b982.64 lakh cr (Sep 2026, &minus;5.1% MoM on a \u20b91.83 lakh cr debt outflow and mark-to-market losses, against record SIP flows of \u20b932,490 cr; AAUM \u20b987.09 lakh cr; 28.62 crore folios), on course for \u20b9100 lakh cr within a couple of years.</li>',
  '<li>~59 AMCs; AUM <b>\u20b983.39 lakh cr</b> (Oct 2026, +0.9% MoM as \u20b91.74 lakh cr of net inflows partly offset mark-to-market drag; AAUM \u20b985.18 lakh cr; SIP flows \u20b932,160 cr; SIP assets \u20b917.68 lakh cr, 21.2% of AUM; 28.78 crore folios), on course for \u20b9100 lakh cr within a couple of years.</li>'),
 # SIF narrative
 ('<b>SIFs (Specialized Investment Funds) hit \u20b938,287 cr net assets in Sep 2026</b> \u2014 up 22.8% on August&rsquo;s \u20b931,175 cr',
  '<b>SIFs (Specialized Investment Funds) hit \u20b942,669.52 cr net assets in Oct 2026</b> on \u20b95,150.41 cr of net inflows and three new strategies raising \u20b9679 cr \u2014 up from \u20b938,287 cr in Sep 2026, itself up 22.8% on August&rsquo;s \u20b931,175 cr'),
 # hunt card
 ('plus SIFs at \u20b938,287 cr after a 22.8% September, more than nineteen times the October 2025 base.',
  'plus SIFs at \u20b942,670 cr after a \u20b95,150 cr October inflow, roughly 21 times the October 2025 base.'),
 # bars
 ('<span class="bl">SIF net assets Sep 2026</span><div class="track"><div class="fill" data-w="25"></div></div><span class="bn">\u20b938,287 cr</span>',
  '<span class="bl">SIF net assets Oct 2026</span><div class="track"><div class="fill" data-w="28"></div></div><span class="bn">\u20b942,670 cr</span>'),
 ('<span class="bl">MF AUM Sep 2026</span><div class="track"><div class="fill" data-w="91"></div></div><span class="bn">\u20b982.64 L cr</span>',
  '<span class="bl">MF AUM Oct 2026</span><div class="track"><div class="fill" data-w="92"></div></div><span class="bn">\u20b983.39 L cr</span>'),
 # sources list
 ('<li><b>AMFI</b> \u2014 industry AUM (\u20b982.64 lakh cr, Sep 2026; \u20b987.08 lakh cr Aug 2026; \u20b973.73 lakh cr FY26 close), SIP flows (\u20b932,490 cr, Sep 2026), folios (28.62 cr), AMFI SIF monthly report (\u20b938,286.94 cr net assets, 34 schemes, 1,56,483 folios at 30 Sep 2026), AMFI\u2013CRISIL Factbook 2026 (21.3% AUM/GDP).</li>',
  '<li><b>AMFI</b> \u2014 industry AUM (<b>\u20b983.39 lakh cr</b>, Oct 2026; AAUM \u20b985.18 lakh cr; \u20b982.64 lakh cr Sep 2026; \u20b973.73 lakh cr FY26 close), SIP flows (\u20b932,160 cr, Oct 2026), SIP assets (\u20b917.68 lakh cr), folios (<b>28.78 cr</b>), AMFI SIF monthly report (\u20b942,669.52 cr net assets, \u20b95,150.41 cr Oct inflows, 3 new strategies; 34 schemes, 1,56,483 folios at 30 Sep 2026), AMFI\u2013CRISIL Factbook 2026 (21.3% AUM/GDP).</li>'),
 # stamp
 ('<span class="stamp">Data as of Mar\u2013Sep 2026 \u00b7 Verify before client use</span>',
  '<span class="stamp">Data as of Mar\u2013Oct 2026 \u00b7 Verify before client use</span>'),
]

# ---------------------------------------------------------------- other modules
NORTHAM = [
 ('BNY Eliza (300+ AI solutions), Citi Custody+ (real-time SEP)',
  'BNY Eliza (400+ AI solutions in production, ~150 digital employees), Citi Custody+ (real-time Single Event Processing: voluntary corporate actions up to 92% faster in the US, 96% of events under two hours)'),
 ('<b>300+ AI solutions in production</b> (125+ at Sep 2025); 100% of staff trained; digital employees handle ~10% of payment validations; client inquiries resolved 80% faster and onboarding 20% faster.',
  '<b>400+ AI solutions in production</b> (300+ in 2025; 125+ at Sep 2025); ~150 digital employees; 100% of staff trained; AI addressed 10%+ of custody settlement status inquiries in Q1 2026, investigated 80%+ faster; client inquiries resolved 80% faster and onboarding 20% faster.'),
 ('<div class="row"><b>Proof points</b><div>300+ AI solutions in production (40+ in Asset Servicing); 99% employee adoption;',
  '<div class="row"><b>Proof points</b><div>400+ AI solutions in production (40+ in Asset Servicing); ~150 digital employees; 99% employee adoption;'),
]

EUROPE = [
 ('BNY\u2019s <b>Eliza</b> platform has <b>300+ AI solutions in production</b> (40+ in Asset Servicing)',
  'BNY\u2019s <b>Eliza</b> platform has <b>400+ AI solutions in production</b> and ~150 digital employees (40+ solutions in Asset Servicing)'),
 ('<b>300+ AI solutions in production</b> (40+ in Asset Servicing; ~150 digital employees; 40% of code AI-authored in Q2 2026)',
  '<b>400+ AI solutions in production</b> (40+ in Asset Servicing; ~150 digital employees; 40% of code AI-authored in Q2 2026)'),
]

RAILS = [
 ('<b style="color:#0E1B2C">BUIDL is no longer the largest tokenised Treasury fund.</b> Tokenised Treasuries sit at about $14.5bn, up 3.6x since the start of 2025 but essentially flat since May. BUIDL is $2.0&ndash;2.2bn; Ondo has moved ahead at roughly $3bn.',
  '<b style="color:#0E1B2C">BUIDL is no longer the largest tokenised Treasury fund &mdash; and it is shrinking.</b> Tokenised Treasuries sit at about $14.5bn, up 3.6x since the start of 2025 but essentially flat since May. BUIDL fell <b>17.9% to $1.66bn</b> between 3 and 11 November, the largest move on the RWAWeekly board; Ondo has moved ahead at roughly $3bn and Franklin Templeton&rsquo;s BENJI added $325m (+35.5%) over the same window. The distributed RWA board measured $21.35bn across 53 products.'),
 ('BNY\'s Eliza platform reports <b>300+ AI solutions in production</b> (40+ in Asset Servicing)',
  'BNY\'s Eliza platform reports <b>400+ AI solutions in production</b> with ~150 digital employees (40+ in Asset Servicing)'),
]

EXEC = [
 ('India \u20b982.64 lakh cr MF + \u20b916.94 lakh cr AIF', 'India \u20b983.39 lakh cr MF + \u20b916.94 lakh cr AIF'),
 ('the \u20b938,287 cr pool grew 22.8% in September alone',
  'the pool reached \u20b942,669.52 cr in October, +&#8377;5,150.41 cr in a single month'),
 ('BNY Eliza: 300+ AI solutions in production (40+ in Asset Servicing), adoption +175% in 2025;',
  'BNY Eliza: 400+ AI solutions in production with ~150 digital employees (40+ in Asset Servicing), adoption +175% in 2025;'),
]

# ---------------------------------------------------------------- weekly brief
BRIEF = '''<div class="kicker">Premium Edition &middot; Published Thursdays</div>
<h1>The Weekly Brief</h1>
<div class="edition">Edition <b>&#8470; 6 &middot; w/e 16 November 2026</b> &middot; Compiled from 7 modules, 4 regions &middot; <b>Professional tier</b></div>
<p class="lede">What actually moved in global securities services this week &mdash; and the one conversation each move should trigger. <b>Every data point carries its label.</b></p>

<article>
<h2><span class="no">01</span>Tokenised collateral stopped being a pilot</h2>
<p>Three threads closed in the same fortnight. Eligible OKX institutional clients can now post BlackRock&rsquo;s BUIDL as collateral while they trade, under a framework Standard Chartered announced in April &mdash; the posted tokens stay in Standard Chartered custody and keep earning dollar yield, while BNY Mellon continues to custody the fund&rsquo;s underlying assets. On 12 November Securitize and Ethena activated a <b>$100m, 24/7 liquidity facility</b> for BUIDL, launching with $50m ($25m USDC / $25m BUIDL) and able to top up $50m within the hour, so eligible investors can move between the fund and stablecoins outside market hours. On 4 November HSBC, Kinexys by J.P. Morgan, MUFG, Societe Generale FORGE and Standard Chartered launched the Global Layer One Organisation, taking MAS&rsquo;s shared-ledger project industry-side &mdash; as a standards body, because the common ledger was never built. <span class="tag fact">FACT</span></p>
<p><b>Why it matters:</b> one instrument now has two custody layers, two reconciliation breaks and no publicly disclosed haircut policy. That is a new diligence, segregation and margin-mobility requirement that most institutional mandates do not yet document &mdash; and it arrives precisely as the SEC proposes to make tokenised-share custody a public disclosure item.</p>
<div class="read"><b>The servicing read:</b> four questions to put in front of any client posting tokenised fund units for margin &mdash; which custodian holds the token, what the haircut policy is, how the two registers reconcile, and who can move the asset during a margin call. Lead with the BUIDL/Standard Chartered structure as the reference case. <span class="tag fact">FACT</span> <span class="tag assess">ASSESSMENT</span></div>
</article>

<article>
<h2><span class="no">02</span>The week&rsquo;s other movers</h2>
<div class="movers">
<div class="mover"><div class="mv-where">India</div><div><b>October was stabilisation, not a rebound &mdash; and SIFs cleared &#8377;42,000 crore.</b> AMFI net AUM <b>&#8377;83.39 lakh crore</b> at 31 October (+0.9% MoM), AAUM &#8377;85.18 lakh crore, as net inflows swung to <b>&#8377;1.74 lakh crore</b> from a &#8377;1.33 lakh crore outflow &mdash; &#8377;1.13 lakh crore of it back into liquid and overnight funds. Equity inflows moderated 13.9% to &#8377;32,994 crore, still the 68th positive month; SIP contribution &#8377;32,160 crore, SIP assets &#8377;17.68 lakh crore (21.2% of AUM), folios 28.78 crore. SIF assets reached <b>&#8377;42,669.52 crore</b> on &#8377;5,150.41 crore of inflows and three new strategies raising &#8377;679 crore &mdash; roughly 21 times October 2025. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">India &middot; Reg</div><div><b>SEBI took settlement risk out of the MF cash leg.</b> A circular of 5 November sets a framework for net settlement of funds for transactions undertaken by mutual fund schemes in the cash market &mdash; a funding, reconciliation and intraday-liquidity change that lands on custodians and fund accountants, not only on members. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Middle East</div><div><b>Riyadh is compounding the post-QFI opening.</b> The CMA is consulting until <b>20 December</b> on account procedures: a new category for foreign individuals resident in GCC states to buy Main Market shares directly, direct access for endowments and non-profits, retained access for former Saudi and GCC residents, and simplified account opening. A parallel consultation covers retail fund rules, and a governance overhaul giving 5%-voting holders more board leverage has been out since 29 October. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Middle East &middot; UAE</div><div><b>The UAE is licensing faster and the fund pool is deepening.</b> 68 new companies licensed in 9M 2026 with 30+ under review and a seven-working-day decision target; domestic funds up <b>94% YoY to 97</b> with AUM up <b>30% to AED 28.6bn</b>. ADGM grew AUM <b>54% YoY in H1 2026</b>, managers from 154 to <b>190</b> and funds from 209 to <b>276</b>; its new Institutional and Sub-Threshold Fund Manager categories bite on 31 March 2027. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">North America</div><div><b>The AI claims became auditable numbers.</b> BNY put <b>more than 400 AI solutions in production</b> in October (up from 300+) with ~150 digital employees; AI handled 10%+ of custody settlement status inquiries in Q1 2026, investigated 80%+ faster. Citi published Custody+ metrics: Single Event Processing touches 80%+ of events once, voluntary corporate actions up to <b>92% faster</b> in the US with <b>96% of events under two hours</b>, and AI tax servicing cutting document processing up to <b>70%</b> across 100,000+ withholding-tax reclaims a year. BNY also took a second digital-asset custody mandate &mdash; the Invesco Galaxy Ethereum ETF, five-year term from 6 November, alongside Coinbase. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Europe</div><div><b>AIFMD II transposition is a patchwork, not a date.</b> Portugal, Greece, Cyprus, Latvia and Estonia have notified nothing; France&rsquo;s ordinance has stalled to a late-February 2027 Assembly vote with the AMF on a transitional regime; Croatia is the only state reported to have gold-plated. The real clock is ESMA&rsquo;s harmonised Annex IV standards from <b>16 April 2027</b> &mdash; new fields for delegation, staff resources, LMT use and loan origination, with UCITS ManCos in scope for the first time. Separately, ESMA&rsquo;s 8 October opinion gives regulators three months to force remediation of non-MiCA-compliant stablecoin exposures, biting around early January 2027. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">APAC &middot; Digital</div><div><b>Project Guardian&rsquo;s ledger became a rulebook.</b> The Global Layer One Organisation launched 4 November under HSBC, Kinexys, MUFG, Societe Generale FORGE and Standard Chartered; MAS now appears only as a listed policymaker. The output is standards, toolkits and programmable-compliance architecture &mdash; not shared infrastructure. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Mandates</div><div><b>Clearstream</b> won further post-trade services from FNZ Bank on top of Vestima (11 Nov); <b>Northern Trust</b> was appointed administrator for Hargreaves Lansdown&rsquo;s money market fund (6 Nov) and asset servicing provider to Australia&rsquo;s LeavePlus scheme (27 Oct); <b>QNB Group</b> used The Network Forum Middle East to press its State Street custody servicing model for Qatar (4 Nov). <span class="tag fact">FACT</span></div></div>
</div>
</article>

<article>
<h2><span class="no">03</span>Data points to refresh in the modules</h2>
<p>Old value &rarr; new value, with the source and label. These are the entries the module pages now carry.</p>
<div class="movers">
<div class="mover"><div class="mv-where">India &middot; MF</div><div>Industry net AUM <b>&#8377;82.64 &rarr; &#8377;83.39 lakh crore</b>; AAUM &#8377;87.09 &rarr; <b>&#8377;85.18 lakh crore</b>; SIP flow &#8377;32,490 &rarr; <b>&#8377;32,160 crore</b>; SIP assets &rarr; <b>&#8377;17.68 lakh crore</b> (21.2% of AUM); folios 28.62 &rarr; <b>28.78 crore</b>; equity inflows &#8377;38,307 &rarr; <b>&#8377;32,994 crore</b>. AMFI, 11 Nov 2026. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">India &middot; SIF</div><div>Net assets <b>&#8377;38,287 &rarr; &#8377;42,669.52 crore</b>; monthly inflow &#8377;7,578 (Sep) &rarr; <b>&#8377;5,150.41 crore</b>; three new strategies raising <b>&#8377;679 crore</b>; schemes and folios held at 34 and 1,56,483 (30 Sep). AMFI SIF monthly report. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">New Rails</div><div>BUIDL <b>$2.0&ndash;2.2bn &rarr; $1.66bn</b> (&minus;17.9% in eight days, &minus;$360.9m, 4th &rarr; 6th on the board); tokenised RWA <b>$39.0bn &rarr; $21.35bn</b> on the RWAWeekly board &mdash; different methodology, so do not splice the two series; BENJI +$325m (+35.5%). RWA.xyz; RWAWeekly, 13 Nov 2026. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">North America</div><div>BNY AI in production <b>300+ &rarr; 400+ solutions</b>, digital employees ~150; Citi Custody+ newly quantified &mdash; <b>92% faster</b> voluntary corporate actions, <b>96% of events &lt;2 hours</b>, tax documents <b>&minus;70%</b>. BNY CEO remarks (Oct 2026); Citi (5 Nov 2026). <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Middle East</div><div>ADGM managers <b>154 &rarr; 190</b>, funds <b>209 &rarr; 276</b>, AUM <b>+54% YoY</b>, US$2.1trn overseen; UAE CMA domestic funds <b>97 (+94%)</b> and AUM <b>AED 28.6bn (+30%)</b>; Saudi QFI removal now <b>1 Feb 2026 in force</b>, next consultation closes <b>20 Dec 2026</b>. ADGM; UAE CMA; Saudi CMA. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Europe</div><div>SEC-equivalent watch item: AIFMD II transposition <b>&ldquo;complete by 16 Apr 2026&rdquo; &rarr; patchwork, France to Feb 2027</b>; Annex IV template live <b>16 Apr 2027</b>; MiCA CASP transitional ended <b>1 Jul 2026</b>, ESMA stablecoin remediation bites <b>early Jan 2027</b>. Legal 500; ESMA. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Assessment</div><div>BUIDL&rsquo;s eight-day drawdown is rotation, not a sentiment break: BENJI added $325m over the same window and the 50-product board moved only <b>&minus;0.6%</b> organically. <span class="tag assess">ASSESSMENT</span></div></div>
</div>
</article>

<article>
<h2><span class="no">04</span>What we&rsquo;re watching next</h2>
<ul class="watch">
<li><b>SEC custody comments &mdash; 7 December.</b> File S7-2026-35. Watch the final permitted-custodian definition and the transition clocks that start on adoption; every US manager&rsquo;s custody committee re-reads its list before this date.</li>
<li><b>Saudi CMA &mdash; 20 December.</b> Whether the GCC-resident individual category survives consultation intact, and whether the retail fund rules and the 5%-holder governance overhaul land together.</li>
<li><b>AMFI November data &mdash; early December.</b> Does SIF hold above &#8377;42,670 crore through a second month, and does the first debt-oriented strategy file?</li>
<li><b>ADGM&rsquo;s 31 March 2027 deadline.</b> Foreign fund managers must appoint an FSRA-licensed administrator and a UAE-resident director and unwind delegation arrangements &mdash; a dated fund-admin and TA trigger.</li>
<li><b>ESMA Annex IV consultation.</b> The technical standards are still unpublished but the reporting regime is expected to apply from 16 April 2027; delegation and staff-resource fields are the data-model problem.</li>
<li><b>DTCC tokenisation go-live.</b> 25 securities, 24/7 wallet-to-wallet transfers &mdash; the volume test for tokenised collateral, and the natural comparator to the BUIDL structure.</li>
</ul>
</article>

'''

ARCHIVE = ('<div class="archive"><b>Archive:</b> Edition &#8470; 5 &middot; 26 October 2026 &mdash; the SEC&rsquo;s custody rewrite and crypto framework, Q3 servicing results (BNY $63.4trn, State Street $59.2trn and a $332m installation backlog), SIF crossing &#8377;38,287 crore, HKEX T+1 for H2 2028 and Standard Chartered&rsquo;s Zodia acquisition. '
           'Edition &#8470; 4 &middot; 12 October 2026 &mdash; fund-admin consolidation (UBS &rarr; Northern Trust, CACEIS &rarr; Edmond de Rothschild, KKR &rarr; Gen II), BNY&rsquo;s EU MiCA custody launch and ESMA&rsquo;s stablecoin warning to CASPs. '
           'Edition &#8470; 3 &middot; 5 October 2026 &mdash; the SEC custody-rule proposal, State Street&rsquo;s US RIA re-entry, HKEX IFP and SIF concentration. '
           'Edition &#8470; 2 &middot; 24 September 2026 &mdash; the Abakkus/Fokkus SIF entry reframed as a servicing segment, plus the September data refresh. '
           'Edition &#8470; 1 &middot; 21 September 2026 &mdash; the launch-week brief (India MF AUM record, ETF records, HSBC-RLAM, Citi-Aegon, ADGM rules, Saudi MMF cap).</div>')

# ---------------------------------------------------------------- run
ok = True
def load(f):
    return open(f, encoding='utf-8').read()

def save(f, c):
    open(f, 'w', encoding='utf-8').write(c)

# 1. weekly strips (replace existing, or insert after cover for India)
for f, new in BLOCKS.items():
    c = load(f)
    c2, done = swap_strip(c, new)
    if not done:
        print('FAIL strip:', f); ok = False; continue
    save(f, c2); print('strip replaced:', f)

# India: insert strip after the cover ledger section
c = load('india-asset-servicing-briefing.html')
anchor = '<span class="stamp">Data as of Mar\u2013Sep 2026 \u00b7 Verify before client use</span>'
idx = c.find(anchor)
if idx < 0:
    print('FAIL: India stamp anchor'); ok = False
else:
    # find end of the ledger block that follows the stamp (first </section>)
    end = c.find('</section>', idx)
    ins = end + len('</section>')
    c = c[:ins] + '\n\n' + INDIA_BLOCK + c[ins:]
    save('india-asset-servicing-briefing.html', c)
    print('strip inserted: india')

# 2. data patches
for f, patches in (('india-asset-servicing-briefing.html', INDIA),
                   ('north-america-asset-servicing-kb.html', NORTHAM),
                   ('europe-asset-servicing-kb.html', EUROPE),
                   ('new-rails-dlt-ai-apac.html', RAILS),
                   ('executive-view.html', EXEC)):
    c = load(f); n = 0
    for old, new in patches:
        if old in c:
            c = c.replace(old, new, 1); n += 1
        else:
            print('FAIL patch in', f, ':', old[:80]); ok = False
    save(f, c); print(f'{f}: {n}/{len(patches)} patches')

# 3. weekly brief rewrite
c = load('weekly-brief.html')
c2, k = re.subn(r'<div class="kicker">Premium Edition.*?(?=<article>\s*<h2><span class="no">05</span>)',
                BRIEF, c, flags=re.S)
if k != 1:
    print('FAIL: brief body', k); ok = False
c = c2
c2, k = re.subn(r'<div class="archive">.*?</div>', ARCHIVE, c, flags=re.S)
if k != 1:
    print('FAIL: archive', k); ok = False
save('weekly-brief.html', c2)
print('weekly-brief.html rewritten: Edition 6')

sys.exit(0 if ok else 1)
