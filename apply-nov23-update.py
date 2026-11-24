#!/usr/bin/env python3
# GSCC weekly data update — 23 Nov 2026 (Edition No. 7, w/e 23 November 2026)
# 1. Replaces the "Weekly update" strip in the six modules (India included since Ed. 6).
# 2. India: SEBI 20 Nov FPI disclosure consultation, 5-day onboarding target, two settlement clocks, SIP attrition.
# 3. APAC: HSBC tokenised unit class + RedCoin, StanChart tokenised deposits, two-tier crypto-ETF custody, HKEX IFP.
# 4. Europe: Allianz GI UCITS depositary State Street -> BNY, MiKaDiv tax reporting, CACEIS rebrand.
# 5. North America: SEC 7 Dec clock, CIBC Mellon/BNY digital custody, awards datasets, proxy modernisation.
# 6. Middle East: State Street-Emirates NBD MOU, ADGM CP 8/2026 on virtual assets, the three dated clocks.
# 7. New Rails: BNY-SWIAT collateral pilot, Banca d'Italia paper, IOSCO monitoring report, BUIDL data-quality flag.
# 8. Rewrites weekly-brief.html as Edition No. 7 and re-dates the Executive View.
import re, sys

WEEK = 'week of 23 November 2026'
WEEKLY_START = '<div style="margin:0 0 20px;background:#FFFFFF;border:1px solid #D9DFE7;border-left:4px solid #C08A2D;border-radius:10px;padding:20px 24px">'
WEEKLY_END = re.compile(r'<div style="margin-top:12px;padding-top:10px;border-top:1px solid #EDF0F4;font-size:11\.5px;color:#5B6B7E">Sources:.*?</div>\s*</div>', re.S)

FACT = '<span style="font-family:\'IBM Plex Mono\',monospace;font-size:9px;background:#F3E9D4;color:#C08A2D;padding:2px 7px;border-radius:3px">ASSESSMENT</span>'


def block(items, sources):
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


def swap_strip(html, new):
    i = html.find(WEEKLY_START)
    if i < 0:
        return html, False
    m = WEEKLY_END.search(html, i)
    if not m:
        return html, False
    return html[:i] + new + html[m.end():], True


# ---------------------------------------------------------------- weekly strips
BLOCKS = {}

BLOCKS['india-asset-servicing-briefing.html'] = block([
 '<b style="color:#0E1B2C">SEBI moved to delete the FPI disclosure regime.</b> A consultation paper of <b>20 November</b> proposes removing the Additional Disclosure Framework outright &mdash; full look-through to every natural person, without threshold, for large or concentrated FPIs &mdash; and with it the same requirements for offshore-derivative subscribers and segregated portfolios. SEBI&rsquo;s own reasoning: the framework is unique to India and goes beyond AML beneficial-ownership rules, which it puts at 10&ndash;15% against roughly 25% in the US, UK, Singapore, Japan and Hong Kong. Comments close <b>11 December 2026</b>.',
 '<b style="color:#0E1B2C">The onboarding target is now a number.</b> On the same day SEBI chairman Tuhin Kanta Pandey said FPI onboarding could compress to <b>five days</b>. The binding constraint has been documentation and look-through, not registration &mdash; which is precisely what the consultation removes. Treat the two announcements as one package.',
 '<b style="color:#0E1B2C">Two settlement clocks, not one.</b> Net settlement of funds for FPI cash-market trades (securities stay gross) is due <b>31 December 2026</b> under SEBI&rsquo;s April circular; the mutual-fund <i>scheme-level</i> framework of 5 November applies from <b>1 April 2027</b> and explicitly forbids any cross-scheme or inter-scheme funding. Custodians have to run both regimes in parallel for a quarter.',
 '<b style="color:#0E1B2C">SIP attrition crossed 100%.</b> October&rsquo;s discontinuation ratio hit <b>116.7%</b> &mdash; 59.12 lakh SIPs stopped or matured against 50.68 lakh new registrations, up from 78.6% in September &mdash; and contributing accounts fell to <b>9.99 crore</b> from 10.06 crore. Flows held anyway: &#8377;32,160 crore, the third consecutive month above &#8377;32,000 crore. Gross flows are masking account churn; the TA book is working harder for the same money.',
 '<b style="color:#0E1B2C">Sell it as:</b> when the eligibility gate disappears, the differentiator moves to what you do after onboarding &mdash; beneficial-ownership monitoring, scheme-level cash forecasting and a single reconciliation spine across FPI, domestic MF and AIF books. Lead with the April 2027 netting benefit: it is the one item here with a bookable cash number. ' + FACT,
], 'SEBI consultation paper (20 Nov 2026); SEBI chairman, CII Financing Summit (20 Nov 2026); SEBI circulars (24 Apr &amp; 5 Nov 2026); AMFI monthly data (11 Nov 2026)')

BLOCKS['apac-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">HSBC put a tokenised fund unit class in a retail banking app.</b> From <b>19 November</b> eligible Hong Kong customers can open a RedCoin wallet in the HSBC HK app and buy a new tokenised unit class (Class SD) of HSBC Global Money Funds &ndash; Hong Kong Dollar from <b>HKD 100</b>, funded in RCHKD. HSBC Securities Services tokenises the class; HSBC Digital Assets Custody safekeeps both the units and the stablecoin. A G-SIB is now issuer, tokeniser, custodian and distributor on one instrument.',
 '<b style="color:#0E1B2C">Tokenised deposits went multi-currency and cross-border.</b> Standard Chartered launched tokenised deposits in Singapore on <b>19 November</b>, after Hong Kong on 2 November &mdash; near real-time flow between the two centres in SGD, HKD, USD, EUR, CNH and GBP, with China AMC, Finloop and PantherTrade among live users and Fireblocks and HashKey named as distribution partners. This is the settlement leg that tokenised funds have been missing.',
 '<b style="color:#0E1B2C">Hong Kong settled the crypto-ETF custody structure &mdash; two tiers.</b> HashKey Exchange, through HashKey Custody Services, was appointed sub-custodian for the GaoTeng Bitcoin ETF that listed on HKEX on <b>20 November</b>, with BOCI-Prudential Trustee as primary custodian holding overall responsibility. HashKey now sub-custodies seven virtual-asset ETFs across BTC, ETH and SOL. The bank trustee keeps the regulated wrapper; the licensed exchange keeps the keys.',
 '<b style="color:#0E1B2C">Fund distribution plumbing and prime brokerage both moved.</b> HKEX&rsquo;s Integrated Fund Platform launched Platform and Nominee Services on 28 October and executed its first trade on 2 November (Value Partners money market fund, CMB Wing Lung as transfer agent) &mdash; a direct challenge to paper-based order routing. Separately, Clear Street completed its acquisition of Boom Securities (HK) on <b>19 November</b> with SFC approval, taking a US prime broker into APAC custody and clearing.',
 '<b style="color:#0E1B2C">Sell it as:</b> the tokenised-fund value chain now has a visible division of labour &mdash; issuer/tokeniser, transfer agent of record, token custodian, cash-settlement rail. Pitch the seat you can actually hold, and ask clients which seat they think they are buying. ' + FACT,
], 'HSBC (19 Nov 2026); Standard Chartered (2 &amp; 19 Nov 2026); HashKey / GaoTeng (20 Nov 2026); HKEX IFP (28 Oct &amp; 2 Nov 2026); Clear Street (19 Nov 2026)')

BLOCKS['europe-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">A named depositary loss for State Street, effective 2 November.</b> Allianz Global Investors moved the custodian role for its German UCITS range from State Street Bank International (Munich) to <b>BNY Mellon SA/NV, Frankfurt branch</b>, with BaFin approval granted on 30 July 2026 and no cost to unitholders. The funds include Allianz Adiverba, Euro Rentenfonds, Thesaurus, Fondak and the Fondsvorsorge series &mdash; a large, long-standing, multi-fund mandate rather than a single vehicle.',
 '<b style="color:#0E1B2C">Withholding tax is turning into a custody product.</b> BNP Paribas extended its RAQUEST partnership on <b>10 November</b> to cover withholding-tax reporting under Germany&rsquo;s new <b>MiKaDiv</b> procedure, which starts in <b>January 2027</b>. Relief-at-source and reclaim analytics are now a scored line item in European depositary and custody RFPs, not a back-office courtesy.',
 '<b style="color:#0E1B2C">The asset-servicer brand map was redrawn.</b> CACEIS has traded under the Cr&eacute;dit Agricole name since <b>1 October</b>, part of the group&rsquo;s ACT 2028 plan &mdash; the first rebrand of a top-five European fund administrator since the BNP Paribas/BNY name changes. Mandate flow continued alongside it: Clearstream added post-trade services for FNZ Bank on top of Vestima (11 Nov) and Northern Trust was appointed administrator for Hargreaves Lansdown&rsquo;s money market fund (6 Nov).',
 '<b style="color:#0E1B2C">Sell it as:</b> a depositary change of this size re-papers every fund&rsquo;s custody chain at once &mdash; look-through, tax documentation, standing instructions, reporting formats. It is the cleanest live example to use in a German or Luxembourg RFP conversation. ' + FACT,
], 'Allianz Global Investors shareholder notice (custodian change, 2 Nov 2026); BaFin approval (30 Jul 2026); Global Custodian (6, 10 &amp; 11 Nov 2026)')

BLOCKS['north-america-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">Thirteen days left on the SEC custody file.</b> Comments on File <b>S7-2026-35</b> close <b>7 December 2026</b>. The open questions are the permitted-custodian definition for crypto, the conditions on conditional adviser self-custody (quarterly written determination that no qualified custodian is available) and the new Form ADV / Form N-CEN questions on tokenised private funds and tokenised fund shares. Every US manager&rsquo;s custody committee is re-reading its list before that date.',
 '<b style="color:#0E1B2C">Digital-asset custody reached Canada, via the JV route.</b> CIBC Mellon launched a digital asset custody service on <b>18 November</b> with <b>BNY as sub-custodian</b> &mdash; institutional safekeeping layered onto an existing domestic custody franchise rather than a new licence. This is the template for every mid-sized domestic custodian that cannot build digital custody alone.',
 '<b style="color:#0E1B2C">The award season is now a free competitive dataset.</b> Asset Servicing Times (12 Nov): <b>BNY</b> global custodian of the year, <b>Northern Trust</b> Americas and digital custodian, <b>HSBC</b> APAC and Middle East custodian, <b>BNP Paribas</b> European custodian and innovation in custody, <b>Apex</b> global fund administrator, <b>CACEIS</b> European, <b>HSBC</b> APAC and <b>CIBC Mellon</b> Americas fund administrator. Global Custodian (18 Nov): State Street, BNP Paribas, Citi and BNY Pershing took multiple honours; Citco overall hedge fund administrator, Ultimus LeverPoint overall private equity administrator.',
 '<b style="color:#0E1B2C">Proxy and asset-servicing rails are being rebuilt for digital holders.</b> Proxymity&rsquo;s Vote Connect Total went live in Canada with CIBC Mellon on 13 November, ahead of the 2027 AGM season, and Broadridge extended proxy voting to Dinari&rsquo;s tokenised US equities on 6 November &mdash; tokenised holders voting through conventional proxy infrastructure. Governance rights, not yield, are the harder tokenisation problem.',
 '<b style="color:#0E1B2C">Sell it as:</b> the awards tables are public evidence for a shortlist conversation, and the CIBC-Mellon/BNY structure is the answer to &ldquo;we can&rsquo;t build it ourselves&rdquo;. Pair both with the 7 December date. ' + FACT,
], 'SEC File S7-2026-35; Global Custodian (13, 18 Nov 2026); Asset Servicing Times Industry Excellence Awards (12 Nov 2026); CIBC Mellon (18 Nov 2026); Broadridge (6 Nov 2026)')

BLOCKS['middle-east-asset-servicing-kb.html'] = block([
 '<b style="color:#0E1B2C">State Street and Emirates NBD formalised an expansion.</b> A memorandum of understanding signed in Dubai on <b>17 November</b> covers the evolution of Emirates NBD Asset Management&rsquo;s operating model, investment solutions and market products, digital innovation and support for the group&rsquo;s wealth business &mdash; building on more than a decade of State Street fund administration and custody for the manager. Read it as an incumbent deepening before the post-QFI and UAE-CMA pipeline converts.',
 '<b style="color:#0E1B2C">ADGM opened its virtual-asset integration consultation.</b> Consultation Paper No. <b>8 of 2026</b>, published <b>13 November</b>, proposes folding virtual assets into the FSMR framework and the FSRA rulebooks, with differentiation retained only where the asset class warrants it. For custodians this is the licensing question behind every digital-asset mandate in Abu Dhabi.',
 '<b style="color:#0E1B2C">Three dated clocks now govern the region.</b> Saudi CMA&rsquo;s account-procedure consultation closes <b>20 December 2026</b> (26 days); UAE onshore firms have until <b>31 December 2026</b> to regularise under the new Capital Market Authority, a date the regulator may extend; ADGM foreign fund managers and VCFMs must comply with the new fund rules by <b>31 March 2027</b>, including an ADGM-licensed administrator and a UAE-resident director.',
 '<b style="color:#0E1B2C">Sell it as:</b> the region is no longer a relationship market &mdash; it is a calendar. Build a single compliance-and-onboarding timeline across Riyadh, Abu Dhabi and onshore UAE and take it to the client as a planning artefact. Whoever brings the calendar controls the conversation. ' + FACT,
], 'Emirates NBD / State Street (17 Nov 2026); ADGM FSRA Consultation Paper No. 8 of 2026 (13 Nov 2026); Saudi CMA; UAE Federal Decree-Law 32/2025; FSRA fund rules (16 Sep 2026)')

BLOCKS['new-rails-dlt-ai-apac.html'] = block([
 '<b style="color:#0E1B2C">BNY proved you can move collateral on-chain without tokenising the asset.</b> On <b>18 November</b> it completed a bilateral collateral pilot with SWIAT, alongside Standard Chartered, DekaBank and LBBW, testing how traditionally custodied securities can be used in blockchain-based collateral transactions. No wrapper, no new instrument &mdash; just the movement and the record. That is the commercially realistic version of tokenised collateral, and it sits beside the BUIDL structure rather than competing with it.',
 '<b style="color:#0E1B2C">A central bank called the custody gap out loud.</b> Banca d&rsquo;Italia&rsquo;s <i>From vaults to validations</i> (17 November) finds tokenisation has not produced custody solutions beyond key custody and account management, and names four obstacles: no unified ecosystem, thin liquidity in tokenised assets, risk-manager caution and no clear legal framework. Individual on-chain segregation is offered by very few operators; account-based segregation still does the work. Custody&rsquo;s future is described as trust, interoperability and operational integrity across networks &mdash; orchestration, not safekeeping.',
 '<b style="color:#0E1B2C">IOSCO put a number on the market: $37bn, and still transitional.</b> The 2026 monitoring report measures tokenised real-world assets at <b>$37bn on 30 June 2026</b>, up from $16bn on 1 July 2025, and finds the market fragmented, with primary issuance ahead of secondary trading and traction concentrated in fixed income and money market funds. It also records SIX folding its SDX DLT CSD into the traditional securities services division &mdash; tokenised infrastructure absorbed by incumbents, not spun out of them.',
 '<b style="color:#0E1B2C">Two more entrants, one new rail.</b> Deutsche Bank launched institutional digital asset custody after BaFin approval, starting with bitcoin and ether. Ant International launched its WhaleRTP protocol on <b>19 November</b> for real-time settlement between tokenised deposits and tokenised money market funds &mdash; the same gap Standard Chartered is closing from the bank side.',
 '<b style="color:#0E1B2C">Data-quality flag &mdash; do not splice BUIDL series.</b> RWA.xyz shows BUIDL at <b>$2.08&ndash;2.16bn</b> (15 Oct &ndash; 2 Nov 2026) while the RWAWeekly board carried <b>$1.66bn</b> on 11 November after a &minus;17.9% move. Different universes and inclusion rules; quote one series, name it, and never carry a delta across the two. ' + FACT,
], 'BNY (18 Nov 2026); Banca d&rsquo;Italia, Markets, infrastructures, payment systems (17 Nov 2026); IOSCO FR/06/2026 (2026 monitoring report); Deutsche Bank (Nov 2026); Ant International (19 Nov 2026); RWA.xyz; RWAWeekly (13 Nov 2026)')

# ---------------------------------------------------------------- brief
BRIEF = '''<div class="kicker">Premium Edition &middot; Published Thursdays</div>
<h1>The Weekly Brief</h1>
<div class="edition">Edition <b>&#8470; 7 &middot; w/e 23 November 2026</b> &middot; Compiled from 7 modules, 4 regions &middot; <b>Professional tier</b></div>
<p class="lede">What actually moved in global securities services this week &mdash; and the one conversation each move should trigger. <b>Every data point carries its label.</b></p>

<article>
<h2><span class="no">01</span>India decided to stop asking foreigners to prove who they are</h2>
<p>On <b>20 November</b> SEBI published a consultation proposing to remove the Additional Disclosure Framework for foreign portfolio investors outright &mdash; the full look-through to every natural person, with no ownership threshold, that applied to FPIs breaching concentration or size tests, and which extended to offshore-derivative subscribers and segregated portfolios. SEBI&rsquo;s own case is that the framework is unique to India and goes beyond anti-money-laundering beneficial-ownership rules, which it puts at 10&ndash;15% against roughly 25% in the US, UK, Singapore, Japan and Hong Kong. Comments close <b>11 December 2026</b>. The same day, chairman Tuhin Kanta Pandey said FPI onboarding could come down to <b>five days</b>. <span class="tag fact">FACT</span></p>
<p><b>Why it matters:</b> India has spent a decade as the market where a global manager&rsquo;s onboarding file went to die. Remove the disclosure gate and the queue moves &mdash; but so does the reason a client tolerated a slow, bespoke operating model. The competitive question stops being &ldquo;can you get me in&rdquo; and becomes &ldquo;what do you do once I&rsquo;m in&rdquo;: beneficial-ownership monitoring, scheme-level cash forecasting, and one reconciliation spine across FPI, domestic mutual fund and AIF books.</p>
<div class="read"><b>The servicing read:</b> pair it with the settlement clocks, because they are the only part of this with a bookable number. FPI cash-market net settlement of funds is due <b>31 December 2026</b>; mutual-fund scheme-level netting starts <b>1 April 2027</b> and forbids any cross-scheme funding. Custodians run both in parallel for a quarter, and the funding benefit is a hard rupee figure in a business case. <span class="tag fact">FACT</span> <span class="tag assess">ASSESSMENT</span></div>
</article>

<article>
<h2><span class="no">02</span>The week&rsquo;s other movers</h2>
<div class="movers">
<div class="mover"><div class="mv-where">APAC &middot; Digital</div><div><b>A G-SIB became issuer, tokeniser, custodian and distributor on one fund.</b> From <b>19 November</b> Hong Kong customers can open a RedCoin wallet in the HSBC HK app and buy a tokenised unit class (Class SD) of HSBC Global Money Funds &ndash; HKD from <b>HKD 100</b>. HSBC Securities Services tokenises the class; HSBC Digital Assets Custody safekeeps the units and the stablecoin. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">APAC &middot; Rails</div><div><b>Tokenised deposits went multi-currency and cross-border.</b> Standard Chartered launched them in Singapore on 19 November, after Hong Kong on 2 November &mdash; near real-time flow in SGD, HKD, USD, EUR, CNH and GBP, with China AMC, Finloop and PantherTrade live. This is the cash leg tokenised funds have been missing. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">APAC &middot; Custody</div><div><b>Hong Kong settled the crypto-ETF structure: two tiers.</b> HashKey, through HashKey Custody Services, became sub-custodian for the GaoTeng Bitcoin ETF listing on 20 November, with <b>BOCI-Prudential Trustee</b> as primary custodian holding overall responsibility. HashKey now sub-custodies seven virtual-asset ETFs. The bank trustee keeps the wrapper; the licensed exchange keeps the keys. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Europe &middot; Mandate</div><div><b>A named depositary loss for State Street.</b> From 2 November Allianz Global Investors&rsquo; German UCITS range &mdash; Adiverba, Euro Rentenfonds, Thesaurus, Fondak, the Fondsvorsorge series &mdash; moved from State Street Bank International to <b>BNY Mellon SA/NV, Frankfurt</b>, BaFin-approved on 30 July, at no cost to unitholders. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Europe &middot; Product</div><div><b>Withholding tax became a custody product.</b> BNP Paribas extended RAQUEST on 10 November to cover reporting under Germany&rsquo;s new <b>MiKaDiv</b> procedure from <b>January 2027</b>. Separately CACEIS has traded under the Cr&eacute;dit Agricole name since 1 October. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">North America</div><div><b>Thirteen days left on the SEC custody file.</b> Comments on S7-2026-35 close <b>7 December</b>: the crypto permitted-custodian definition, conditional self-custody conditions and the new Form ADV / N-CEN tokenised-fund questions are all still open. Meanwhile CIBC Mellon launched Canadian digital asset custody on 18 November with <b>BNY as sub-custodian</b> &mdash; the JV template for domestic custodians that cannot build it alone. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Middle East</div><div><b>State Street formalised an expansion with Emirates NBD.</b> An MOU signed in Dubai on <b>17 November</b> covers Emirates NBD Asset Management&rsquo;s operating-model evolution, investment solutions, digital innovation and wealth, on top of a decade of fund administration and custody. ADGM separately opened Consultation Paper No. 8 of 2026 on 13 November to fold virtual assets into the FSMR framework. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Mandates</div><div><b>Clearstream</b> added post-trade services for FNZ Bank on top of Vestima (11 Nov); <b>Northern Trust</b> took Hargreaves Lansdown&rsquo;s money market fund administration (6 Nov); <b>Clear Street</b> closed its Boom Securities (HK) acquisition on 19 November with SFC approval, taking a US prime broker into APAC custody. <span class="tag fact">FACT</span></div></div>
</div>
</article>

<article>
<h2><span class="no">03</span>Data points to refresh in the modules</h2>
<p>Old value &rarr; new value, with the source and label. These are the entries the module pages now carry.</p>
<div class="movers">
<div class="mover"><div class="mv-where">India &middot; Reg</div><div>FPI additional disclosure framework <b>&ldquo;in force&rdquo; &rarr; proposed for removal</b>, comments to <b>11 Dec 2026</b>; FPI onboarding <b>&ldquo;weeks&rdquo; &rarr; 5-day target</b>; FPI net settlement <b>&ldquo;pending&rdquo; &rarr; 31 Dec 2026</b>; MF scheme-level netting <b>new &rarr; 1 Apr 2027</b>. SEBI, 20 Nov &amp; 5 Nov 2026. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">India &middot; Flows</div><div>SIP discontinuation ratio <b>78.6% &rarr; 116.7%</b>; SIPs stopped/matured <b>49.68 &rarr; 59.12 lakh</b>; new registrations <b>63.26 &rarr; 50.68 lakh</b>; contributing accounts <b>10.06 &rarr; 9.99 crore</b>. Contribution held at &#8377;32,160 crore. AMFI, 11 Nov 2026. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Europe</div><div>Allianz GI UCITS depositary <b>State Street Bank International &rarr; BNY Mellon SA/NV</b>, effective 2 Nov 2026 (BaFin, 30 Jul 2026); German withholding-tax reporting <b>&ldquo;BAFin/legacy&rdquo; &rarr; MiKaDiv from Jan 2027</b>; CACEIS <b>&rarr; Cr&eacute;dit Agricole brand</b> from 1 Oct 2026. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">New Rails</div><div>Tokenised RWA <b>$16bn (1 Jul 2025) &rarr; $37bn (30 Jun 2026)</b> on the IOSCO measure &mdash; a different universe from the $21.35bn RWAWeekly board already in the module, so label the series. BUIDL <b>$2.08&ndash;2.16bn</b> (RWA.xyz) vs <b>$1.66bn</b> (RWAWeekly, 11 Nov): do not splice. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Middle East</div><div>New dated entries: State Street&ndash;Emirates NBD <b>MOU 17 Nov 2026</b>; ADGM <b>CP No. 8 of 2026, 13 Nov 2026</b>; Saudi account consultation <b>26 days to 20 Dec</b>; UAE onshore regularisation <b>31 Dec 2026</b>; ADGM foreign manager rules <b>31 Mar 2027</b>. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">APAC</div><div>HSBC tokenised unit class <b>new &rarr; HKD 100 minimum, 19 Nov 2026</b>; Standard Chartered tokenised deposits <b>HK only &rarr; HK + SG, six currencies</b>; crypto-ETF custody <b>single-tier &rarr; two-tier (trustee + exchange sub-custodian)</b>; Clear Street <b>announced &rarr; closed 19 Nov 2026</b>. <span class="tag fact">FACT</span></div></div>
<div class="mover"><div class="mv-where">Assessment</div><div>The week&rsquo;s real signal is structural, not numerical: banks are choosing to orchestrate tokenised rails (BNY&ndash;SWIAT, CIBC Mellon&ndash;BNY, HSBC in-app) rather than tokenise the asset. Expect 2027 RFP language to ask for orchestration evidence, not token issuance. <span class="tag assess">ASSESSMENT</span></div></div>
</div>
</article>

<article>
<h2><span class="no">04</span>What we&rsquo;re watching next</h2>
<ul class="watch">
<li><b>SEBI comments &mdash; 11 December.</b> Whether the ADF is deleted or merely softened for ODI subscribers, and whether the five-day onboarding target arrives with a named service standard attached to intermediaries.</li>
<li><b>SEC custody comments &mdash; 7 December.</b> The permitted-custodian definition for crypto and the transition clocks that start on adoption. Thirteen days; custody committees are re-reading lists now.</li>
<li><b>Saudi CMA &mdash; 20 December.</b> Whether the GCC-resident individual category survives consultation, and whether the retail fund rules and the 5%-holder governance overhaul land together.</li>
<li><b>AMFI November data &mdash; early December.</b> Does SIF hold above &#8377;42,670 crore for a second month, and does the discontinuation ratio stay above 100%? That second number matters more for TA revenue than the AUM headline.</li>
<li><b>UAE onshore regularisation &mdash; 31 December 2026.</b> Firms that have not re-papered under the new Capital Market Authority face fines up to AED 200m or a multiple of profit; the extension question is unresolved.</li>
<li><b>Two settlement go-lives &mdash; 31 December 2026 and 1 April 2027.</b> FPI net funding first, then MF scheme-level netting. Watch which custodians publish a funding-benefit number and which stay silent.</li>
</ul>
</article>

'''

ARCHIVE = ('<div class="archive"><b>Archive:</b> Edition &#8470; 6 &middot; 16 November 2026 &mdash; AMFI October data (AUM &#8377;83.39 lakh crore, SIF &#8377;42,669.52 crore), BUIDL as collateral at Standard Chartered, Securitize&ndash;Ethena&rsquo;s $100m 24/7 facility, the Global Layer One Organisation, AIFMD II&rsquo;s transposition patchwork and Saudi CMA&rsquo;s 20 December consultation. '
           'Edition &#8470; 5 &middot; 26 October 2026 &mdash; the SEC&rsquo;s custody rewrite and crypto framework, Q3 servicing results (BNY $63.4trn, State Street $59.2trn and a $332m installation backlog), SIF crossing &#8377;38,287 crore, HKEX T+1 for H2 2028 and Standard Chartered&rsquo;s Zodia acquisition. '
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

for f, new in BLOCKS.items():
    c = load(f)
    c2, done = swap_strip(c, new)
    if not done:
        print('FAIL strip:', f); ok = False; continue
    save(f, c2); print('strip replaced:', f)

# Executive view: re-date the data vintage
c = load('executive-view.html')
n = c.count('Data as of Sep 2026')
c = c.replace('Data as of Sep 2026', 'Data as of Oct 2026')
c = c.replace('Data as of September 2026.', 'Data as of October 2026.')
save('executive-view.html', c)
print(f'executive-view.html: re-dated ({n} eyebrow/footer occurrences)')

# Weekly brief rewrite
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
print('weekly-brief.html rewritten: Edition 7')

sys.exit(0 if ok else 1)
