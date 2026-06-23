import { JSDOM } from 'jsdom'; import * as d3 from 'd3'; import fs from 'fs';

// --- assertions: any failure throws -> non-zero exit. No silent passes. ---
let PASS=0;
function assert(cond,msg){ if(!cond){ throw new Error('ASSERT FAILED: '+msg); } PASS++; }
function eq(a,b,msg){ assert(a===b, msg+` (got ${JSON.stringify(a)}, want ${JSON.stringify(b)})`); }

// jsdom lacks SVGSVGElement.viewBox.baseVal, so a deferred d3-zoom transition
// fires later via requestAnimationFrame and throws AFTER the synchronous test
// body has fully passed. Swallow ONLY that known teardown noise; rethrow
// anything else so real async bugs still red the run.
process.on('uncaughtException',e=>{
  const m=String(e&&e.message||e);
  if(/viewBox|baseVal|getScreenCTM|createSVGMatrix/i.test(m)) return; // known jsdom/d3 limitation
  console.error('UNCAUGHT (real):',e); process.exit(1);
});

// Test the artifact as it actually ships (D3 + fonts inlined; no CDN/link tags to strip).
const html=fs.readFileSync('index.html','utf8');
const dom=new JSDOM(html,{pretendToBeVisual:true,url:'https://example.org/app'});
const {window}=dom;
global.window=window; global.document=window.document;
global.SVGElement=window.SVGElement; global.Element=window.Element; global.HTMLElement=window.HTMLElement;
global.localStorage=window.localStorage; global.location=window.location; global.history=window.history;
window.d3=d3; window.matchMedia=()=>({matches:false,addEventListener(){}}); global.matchMedia=window.matchMedia;
window.requestAnimationFrame=cb=>setTimeout(()=>cb(Date.now()),0);
for(const id of ['m-questions','m-timeline','m-paths','m-constellation','m-lens']){const el=window.document.getElementById(id);
  Object.defineProperty(el,'clientWidth',{value:1180,configurable:true});Object.defineProperty(el,'clientHeight',{value:640,configurable:true});}
window.Element.prototype.scrollIntoView=function(){};

// The app script is the last <script> before </body>. (D3 is inlined in <head>
// as a separate <script>, so a leftmost regex would span both blocks and hit a
// literal </script>.) Slice the app block out by position instead.
const bodyEnd=html.lastIndexOf('</body>');
const appOpen=html.lastIndexOf('<script>',bodyEnd);
const appClose=html.lastIndexOf('</script>',bodyEnd);
const m=html.slice(appOpen+'<script>'.length,appClose);
try{ new window.Function('d3','window','document',m)(d3,window,window.document); }
catch(e){ console.error('SETUP ERR:',e.message,e.stack.split('\n')[1]); process.exit(1); }

const $=s=>window.document.querySelector(s),$$=s=>[...window.document.querySelectorAll(s)];
const click=el=>el&&el.dispatchEvent(new window.window.MouseEvent('click',{bubbles:true}));
const esc=()=>window.document.dispatchEvent(new window.window.KeyboardEvent('keydown',{key:'Escape'}));
const D=JSON.parse($('#ideas-data').textContent);
assert(D.concepts.length>=160,'ideas data present');

// PHILOSOPHY OF LANGUAGE: the linguistic turn gives `know` a language home (T2 #4).
const langIds=['Sense and Reference','On Denoting','Naming and Necessity','How to Do Things with Words','Speaker Meaning','Arbitrariness of the Sign'];
const langCs=D.concepts.filter(c=>langIds.includes(c.id));
eq(langCs.length,6,'all six philosophy-of-language ideas are present');
assert(langCs.every(c=>c.q==='know'),'philosophy of language lives under the know question');

// init state
eq($('.switch button.active')?.dataset.mode,'questions','init mode is questions');
eq($('.switch button.active')?.getAttribute('aria-selected'),'true','active tab aria-selected');
// The empty-state overlay must be truly invisible on load, not merely carry the
// [hidden] attribute: an ID rule (#empty-state{display:flex}) outranks the UA
// [hidden]{display:none}, so the attribute alone does NOT hide it. Assert the
// CSS cascade actually collapses it (regression guard for the always-on overlay).
eq(window.getComputedStyle($('#empty-state')).display,'none','empty-state is display:none on load (not just [hidden])');

// build every mode without throwing
for(const mo of ['timeline','paths','constellation','lens','questions']) click($('.switch button[data-mode="'+mo+'"]'));
console.log('5 modes built ok');

// THRESHOLD / LANDING HERO: first-run welcome that names the feeling + honest scope.
const gate=$('#gate');
assert(gate && !gate.hidden, 'first-run threshold gate is shown on a fresh visit');
eq($('#gate .gate-line')?.dataset.i18n, "You're not the first to wonder", 'gate leads with the north-star feeling');
const gcount=$('#gate .gate-count')?.textContent||'';
assert(/11/.test(gcount)&&/425/.test(gcount)&&/4,?399/.test(gcount), 'gate shows the honest anchor count (11 questions / 425 thinkers / 4,399 years)');
assert(!/263/.test($('#gate .gate-inner')?.textContent||''), 'gate does NOT lead with the 263-ideas number');
assert(/2375|BCE/.test($('#gate .gate-span')?.dataset.i18n||''), 'gate states the honest span (2375 BCE → 2024)');
click($('#gate-enter')); // cross the threshold
eq(window.localStorage.getItem('aoi.entered'),'1','crossing the threshold records the first run so the gate stays dismissed');
assert(gate.classList.contains('closing')||gate.hidden, 'crossing the threshold dismisses the gate');

// EPISTEMIC STATUS (the 5-state spine): data integrity + Questions-tab surface
const STATE_IDS=['handed-off','hardened','live-rivals','open','dissolved'];
eq(D.questions.every(q=>STATE_IDS.includes(q.status)), true, 'every question carries a valid 5-state status');
eq(D.questions.every(q=>['clear','contested'].includes(q.statusConf)), true, 'every question has a clear/contested confidence flag');
eq(D.questions.every(q=>q.statusResidue===null||STATE_IDS.includes(q.statusResidue)), true, 'residue, when present, is a valid state');
eq(D.questions.every(q=>typeof q.statusWhy==='string'&&q.statusWhy.length>0), true, 'every question has a rationale');
eq(D.questions.every(q=>!/\(\w+ \d{3,4}\)/.test(q.statusWhy)), true, 'rationales name no single thinker+date as having settled it');
click($('.switch button[data-mode="questions"]'));
eq($$('#m-questions .band .q-status').length, 11, 'all eleven question bands show an epistemic-status badge');
eq($$('#m-questions .band .q-status').every(s=>STATE_IDS.includes(s.dataset.state)), true, 'each badge carries its state on data-state');
eq($$('.q-key-item').length, 5, 'the legend keys all five states');
assert(($('.q-key-note')?.textContent||'').includes('one vantage'), 'legend states the honesty caveat ("one map, from one vantage")');

// LENS (Map VI): "Eleven Doors In" board → focus+context ego-graph
click($('.switch button[data-mode="lens"]'));
eq($('.switch button.active')?.dataset.mode, 'lens', 'lens tab activates');
eq($('#lens-board').hidden, false, 'lens opens on the Eleven Doors board');
eq($$('.lb-cell').length, 11, 'board shows eleven question doors (one per question)');
// the board is one screen, one verb: graph-only chrome must be hidden on it
eq($('#lens-top').style.display, 'none', 'graph top chrome (control bar + trail) is hidden on the board');
eq($('#lens-hint').style.display, 'none', 'graph hint is hidden on the board');
click($$('.lb-cell')[0]); // enter through the first door
eq($('#lens-board').hidden, true, 'choosing a door dismisses the board');
assert($('#lens-top').style.display!=='none', 'top chrome returns inside the graph');
eq($('#lens-home').hidden, false, 'the "Doors" home button appears once inside the graph');
assert($$('#lens-svg g.lnode').length>1, 'lens renders a focus node plus neighbours');
eq($$('#lens-svg g.lnode.focus').length, 1, 'exactly one focus node at the centre');
// entering through a door starts a fresh path — a single step shows no rail yet
eq($('#lens-trail').hidden, true, 'breadcrumb rail is hidden at the path start (one concept)');
const lensName0=$('#lens-cap .lc-name')?.textContent||'';
assert(lensName0.length>0, 'lens caption names the focal idea');
const focusName0=$('#lens-svg g.lnode.focus text')?.textContent;
click($$('#lens-svg g.lnode')[1]); // travel to a neighbour
assert($('#lens-svg g.lnode.focus text')?.textContent!==focusName0, 'clicking a neighbour re-centres the lens');
// now the path has two concepts — the breadcrumb rail appears
eq($('#lens-trail').hidden, false, 'breadcrumb rail appears once you have walked a step');
eq($$('#lens-trail .lt-chip').length, 2, 'rail shows both concepts of the path');
assert($('#lens-trail .lt-chip.cur')?.textContent!==focusName0, 'current chip names where you are now, not where you started');
eq($$('#lens-trail .lt-chip.cur').length, 1, 'exactly one chip marked current');
click($('#lens-random')); // serendipity dice — must keep a valid focus
eq($$('#lens-svg g.lnode.focus').length, 1, 'random walk keeps a single focus');
assert($$('#lens-trail .lt-chip').length>=2, 'random walk extends the path');
// rewind by clicking the first breadcrumb chip → back to the start, rail collapses
click($$('#lens-trail .lt-chip')[0]);
eq($('#lens-trail').hidden, true, 'clicking the first chip rewinds the path to a single concept');
// guided tour (the rail is an Explore-mode notion; it hides in Tour)
click($('#lens-tour'));
eq($('#lens-trail').hidden, true, 'breadcrumb rail is hidden during the guided tour');
assert(!$('#lens-tour-nav').hasAttribute('hidden'), 'guided tour reveals the step controls');
assert(/^1\s*\/\s*\d+/.test($('#lens-count').textContent), 'tour starts at step 1 / N');
const tourBefore=$('#lens-count').textContent; click($('#lens-next'));
assert($('#lens-count').textContent!==tourBefore, 'Next advances the tour step');
// the "Doors" home button returns to the board
click($('#lens-home'));
eq($('#lens-board').hidden, false, 'home button returns to the Eleven Doors board');
// "open full entry" bridges to the shared dossier
click($('.switch button[data-mode="lens"]')); click($('#lens-explore'));
click($('#lens-cap .lc-open'));
assert($('#drawer').classList.contains('open'), 'lens "open full entry" opens the shared dossier');
// regression: with the dossier open, clicking a neighbour must keep the side panel
// in sync (it used to recentre the ring but leave the panel on the previous idea).
const lensDrBefore=$('#dr-name').textContent;
const lensNb=$$('#lens-svg g.lnode:not(.focus)')[0];
assert(!!lensNb, 'lens graph has a neighbour to navigate to');
click(lensNb);
eq($('#dr-name').textContent, $('#lens-svg g.lnode.focus text')?.textContent, 'open dossier follows the lens focus to the clicked neighbour');
assert($('#dr-name').textContent!==lensDrBefore, 'the synced dossier actually changed concepts');
esc(); click($('.switch button[data-mode="questions"]'));

// TIMELINE
click($('.switch button[data-mode="timeline"]'));
eq($$('#tl-svg .tl-node').length, D.concepts.length, 'timeline renders one node per concept');
eq($$('#tl-svg .tl-lane').length, D.questions.length, 'timeline has one lane per great question');
eq($$('#tl-svg .tl-lane-lab').length, D.questions.length, 'each question lane is labelled');
assert($$('#tl-svg .tl-tick').length>0, 'timeline has era ticks');
// re-encode: FIXED lane order (canonical, not recurrence) + status colour + density bands
eq($$('#tl-svg .tl-lane-lab').map(l=>l.dataset.q).join(' '), D.questions.map(q=>q.id).join(' '),
  'timeline lanes are in fixed canonical question order (not sorted by recurrence)');
eq($$('#tl-svg .tl-band').length, D.questions.length, 'each lane has a temporal density band');
assert($$('#tl-svg .tl-band').every(b=>(b.getAttribute('d')||'').length>10), 'every density band has geometry');
const STINK={'handed-off':'#5fc7b8','hardened':'#86c08a','live-rivals':'#d9b65f','open':'#c3c7cf','dissolved':'#9aa3bd'};
assert($$('#tl-svg .tl-lane-lab').every(l=>l.style.fill===STINK[D.questions.find(q=>q.id===l.dataset.q).status]),
  'lane label colour encodes epistemic status (not region/hue)');
eq($$('#m-timeline .tl-stkey .row').length, 5, 'timeline legend keys all five status colours');

// ARGUMENTS tab (formerly "Paths") — the dialectic walk fills the whole tab now
// that the Reading-journeys view has been removed.
click($('.switch button[data-mode="paths"]'));
eq($('.switch button.active')?.dataset.mode, 'paths', 'Arguments tab activates');
eq($('#thr-wrap').hasAttribute('hidden'), false, 'the Arguments walk is visible');
assert(!$('#jrn-wrap'), 'the removed Reading-journeys pane is gone');
assert(!$('#paths-journeys')&&!$('#paths-threads'), 'the old Paths sub-toggle is gone');
eq($$('#thr-list .thr-item').length, D.arguments.length, 'one thread item per argument');
const before=$('#thr-count').textContent; click($('#thr-next'));
assert($('#thr-count').textContent!==before, 'Next advances the thread counter');
assert($$('#thr-rail .thr-dot').length>0, 'thread rail has step dots');
const stepName=$('#thr-open')||$('.thr-name');
assert(stepName && stepName.textContent.trim().length>0, 'thread step shows a non-empty name');
click($$('.thr-item')[3]);
assert(($('#thr-title')?.textContent||'').length>0, 'clicking a thread sets its title');
assert(!('journeys' in D), 'journeys data is no longer baked into the build');
esc();

// FILTERS
click($('#filt-btn'));
assert(!$('#filters').hasAttribute('hidden'), 'filter panel opens');
eq($$('#flt-q .flt-row').length, D.questions.length, 'one filter row per question');
assert($$('#flt-read .flt-pill').length===3, 'three reading-status pills');
assert($$('#flt-region .flt-pill').length>0, 'region pills present');
click($('.switch button[data-mode="questions"]'));
const totalCards=$$('#m-questions .card').length;
assert(totalCards>0,'questions view has cards');
const firstQRow=$('#flt-q .flt-row');
click(firstQRow); // hide one question
const visAfter=$$('#m-questions .card').filter(c=>c.style.display!=='none').length;
assert(visAfter<totalCards, 'hiding a question reduces visible cards');
assert($('#filt-btn').classList.contains('on'), 'filter button shows active state');
click(firstQRow); // restore
eq($$('#m-questions .card').filter(c=>c.style.display!=='none').length, totalCards, 'restoring shows all cards again');

// EMPTY STATE: turn every question off -> overlay shows
const qrows=$$('#flt-q .flt-row'); qrows.forEach(r=>{ if(!r.classList.contains('off')) click(r); });
assert(!$('#empty-state').hasAttribute('hidden'), 'empty-state appears when nothing matches');
click($('#empty-reset'));
assert($('#empty-state').hasAttribute('hidden'), 'reset clears the empty-state');

// READING STATUS + progress + persistence
click($$('#m-questions .card')[0]);
assert(($('#dr-name').textContent||'').length>0, 'drawer shows a concept name');
click($$('#dr-status button').find(b=>b.dataset.s==='read'));
assert(/\d+\s*\/\s*\d+/.test($('#progress').textContent), 'progress chip shows N / M');
assert(!!window.localStorage.getItem('aoi.reading.v1'), 'reading status persisted to localStorage');
// renderStatus re-renders the buttons, so re-query for the now-active one.
assert($$('#dr-status button').find(b=>b.dataset.s==='read')?.classList.contains('on'), 'read button shows active state after selection');
// the card itself reflects status via data-rs (drives the dim+check / gold-dot CSS).
eq($$('#m-questions .card')[0].dataset.rs, 'read', 'card carries data-rs="read" after marking read');
click($$('#dr-status button').find(b=>b.dataset.s==='unread'));
eq($$('#m-questions .card')[0].dataset.rs, 'unread', 'card data-rs returns to "unread"');

// SEARCH "locate in all tabs": clicking an idea result locates it in the active tab (no forced switch)
click($('.switch button[data-mode="questions"]'));
const sIdea=D.concepts[0].id;
const s2=$('#search2'); s2.value=sIdea; s2.dispatchEvent(new window.window.Event('input',{bubbles:true}));
const ideaRes=$$('#res2 .r2').find(e=>/idea/.test(e.querySelector('.q')?.textContent||''));
assert(!!ideaRes, 'search shows an idea result');
click(ideaRes);
assert($('#m-questions').classList.contains('active'), 'search result stays on the current tab (no forced switch)');
const locCard=$$('#m-questions .card .c-id').find(e=>e.textContent===sIdea)?.closest('.card');
assert(locCard?.classList.contains('sel'), 'clicking an idea search result locates (sel) its card in the current tab');

// CONTESTED badge: opening a contested concept reveals the tag, a normal one hides it
const contestedId=D.concepts.find(c=>c.contested)?.id;
const plainId=D.concepts.find(c=>!c.contested)?.id;
function openByName(n){ const card=$$('#m-questions .card .c-id').find(e=>e.textContent===n); click(card?.closest('.card')); }
// Assert computed display, not just the attribute: #dr-contested{display:flex}
// outranks UA [hidden]{display:none} by specificity, so the attribute alone
// would leave the badge on for every concept (regression guard).
if(contestedId){ openByName(contestedId); assert(!$('#dr-contested').hasAttribute('hidden'), 'contested concept shows the Contested badge');
  eq(window.getComputedStyle($('#dr-contested')).display,'flex','contested badge is display:flex (visible)'); }
if(plainId){ openByName(plainId); assert($('#dr-contested').hasAttribute('hidden'), 'non-contested concept hides the badge');
  eq(window.getComputedStyle($('#dr-contested')).display,'none','non-contested badge is display:none (truly hidden)'); }

// READINGS: honest Primary-led order (merge.py bakes KIND_ORDER). No Primary
// may trail a companion text in any concept's list; the drawer leads each list
// with "primary sources first" and only companion texts carry a quiet badge —
// the retired "ranked by influence" claim must be gone from the whole artifact.
const allPrimaryLed=D.concepts.every(c=>{ let sawNon=false;
  return (c.readings||[]).every(r=>{ if(r.kind!=='Primary'){sawNon=true; return true;} return !sawNon; }); });
assert(allPrimaryLed, 'every concept lists its Primary readings first (baked Primary-led order)');
assert(!/ranked by influence/i.test(html), 'retired the false "ranked by influence" label everywhere');
const mixed=D.concepts.find(c=>(c.readings||[]).some(r=>r.kind==='Primary')&&(c.readings||[]).some(r=>r.kind!=='Primary'));
if(mixed){ openByName(mixed.id);
  eq($$('#dr-readings .reading .badge').length, (mixed.readings||[]).filter(r=>r.kind!=='Primary').length, 'only companion (non-Primary) readings carry a badge');
  assert(!$$('#dr-readings .reading')[0].querySelector('.badge'), 'the leading (Primary) reading is unmarked'); }

// FOIL (argues against)
openByName('Modern Virtue Ethics');
assert(($('#dr-foil')?.textContent||'').length>0, 'foil shown for a concept that rejects others');

// DEEP LINK
openByName('Capitalist Realism');
assert(/#\/questions\/idea\//.test(window.location.hash), 'opening a concept writes a deep-link hash');
window.location.hash='#/paths/2.1';
window.dispatchEvent(new window.window.HashChangeEvent('hashchange'));
eq($('.switch button.active')?.dataset.mode, 'paths', 'hashchange routes to the Arguments view');
eq($('#thr-wrap').hasAttribute('hidden'), false, 'a /paths hash lands on the Arguments walk');
// legacy deep links (/paths/threads/i.s, /threads/i.s, /journeys/i) still route to Arguments
window.location.hash='#/paths/threads/2.1';
window.dispatchEvent(new window.window.HashChangeEvent('hashchange'));
eq($('.switch button.active')?.dataset.mode, 'paths', 'legacy /paths/threads hash still routes to Arguments');
window.location.hash='#/journeys/1';
window.dispatchEvent(new window.window.HashChangeEvent('hashchange'));
eq($('.switch button.active')?.dataset.mode, 'paths', 'legacy /journeys hash still routes to Arguments');

// ABOUT modal: opens, Esc closes, focus restored to the trigger
click($('.switch button[data-mode="questions"]'));
const aboutBtn=$('#about-btn'); aboutBtn.focus(); click(aboutBtn);
assert($('#about-overlay').classList.contains('open'), 'About panel opens');
assert($('#about-overlay').getAttribute('aria-modal')==='true', 'About panel is aria-modal');
// PR2: "Where to begin" gateways + derived "recurring works" live in the About
// panel. The derived list is baked by merge.py (count>=2, reach-sorted); the
// curated gateways must all resolve to real concepts and open the drawer.
assert(Array.isArray(D.recurring)&&D.recurring.length>=10, 'derived recurring-works list is baked into the data');
assert(D.recurring.every(r=>r.count>=2), 'every recurring work spans at least two concepts');
assert(D.recurring.every((r,i,a)=>i===0||a[i-1].count>=r.count), 'recurring works are sorted by reach (count, descending)');
const beginBtns=$$('#about-begin .begin-i');
assert(beginBtns.length===10, 'ten curated "where to begin" gateways render');
eq($$('#about-recurring .recur-i').length, D.recurring.length, 'recurring list renders one row per derived work');
click(beginBtns[0]); // closes About, opens the gateway concept's drawer
assert(!$('#about-overlay').classList.contains('open'), 'clicking a gateway closes the About panel');
assert($('#drawer').classList.contains('open'), 'clicking a gateway opens its concept drawer');
esc(); // shut the drawer before re-testing About Esc below
aboutBtn.focus(); click(aboutBtn);
esc();
assert(!$('#about-overlay').classList.contains('open'), 'Esc closes the About panel');
eq(window.document.activeElement, aboutBtn, 'focus returns to the About trigger on close');

// ESC closes the drawer (ensure filters/about are shut first so the drawer is top-most)
if(!$('#filters').hasAttribute('hidden')) click($('#filt-btn'));
click($$('#m-questions .card')[0]);
assert($('#drawer').classList.contains('open'), 'drawer opens on card click');
esc();
assert(!$('#drawer').classList.contains('open'), 'Esc closes the drawer when it is top-most');

// LANGUAGE TOGGLE: switching language flips the active button + <html lang>,
// and with an empty/partial overlay every string safely falls back to English.
click($('.switch button[data-mode="questions"]'));
assert($$('#lang-switch button').length===3, 'three language buttons present');
eq($('#lang-switch button.active')?.dataset.lang, 'en', 'English is the active language on load');
const firstCardName=$('#m-questions .card .c-id')?.textContent;
click($('#lang-switch button[data-lang="zh"]'));
eq($('#lang-switch button.active')?.dataset.lang, 'zh', 'clicking 繁 makes Traditional Chinese active');
eq(window.document.documentElement.lang, 'zh-Hant', 'html lang switches to zh-Hant');
assert(!$('#about-mt-note').hasAttribute('hidden'), 'machine-assisted note shows for a non-English language');
click($('#lang-switch button[data-lang="ru"]'));
eq($('#lang-switch button.active')?.dataset.lang, 'ru', 'clicking RU makes Russian active');
click($('#lang-switch button[data-lang="en"]'));
eq(window.document.documentElement.lang, 'en', 'html lang returns to en');
assert($('#about-mt-note').hasAttribute('hidden'), 'machine-assisted note hidden again in English');
eq($('#m-questions .card .c-id')?.textContent, firstCardName, 'concept names restore on English (fallback round-trips)');

// --- REGRESSION: lazy-built graph modes localise (timeline / lens / constellation) ---
// The bug: a graph mode built for the FIRST time while the language was ALREADY
// non-English shipped English node text. The build wrote raw ids and relied on a
// later applyLang relabel that never re-fires for an already-active language.
// Boot a fresh app straight into 繁中, build each graph cold, and assert the
// rendered SVG text is localized (concept nodes carry zh names; the constellation
// localises its region headings + legend — thinker names stay as proper nouns).
{
  const dom2=new JSDOM(html,{pretendToBeVisual:true,url:'https://example.org/app'});
  const w=dom2.window;
  w.localStorage.setItem('aoi.lang','zh'); // app reads this at init -> boots in zh
  global.window=w; global.document=w.document;
  global.SVGElement=w.SVGElement; global.Element=w.Element; global.HTMLElement=w.HTMLElement;
  global.localStorage=w.localStorage; global.location=w.location; global.history=w.history;
  w.d3=d3; w.matchMedia=()=>({matches:false,addEventListener(){}}); global.matchMedia=w.matchMedia;
  w.requestAnimationFrame=cb=>setTimeout(()=>cb(Date.now()),0);
  for(const id of ['m-timeline','m-lens','m-constellation']){const el=w.document.getElementById(id);
    Object.defineProperty(el,'clientWidth',{value:1180,configurable:true});Object.defineProperty(el,'clientHeight',{value:640,configurable:true});}
  w.Element.prototype.scrollIntoView=function(){};
  try{ new w.Function('d3','window','document',m)(d3,w,w.document); }
  catch(e){ console.error('SETUP2 ERR:',e.message,e.stack.split('\n')[1]); process.exit(1); }
  const q2=s=>[...w.document.querySelectorAll(s)];
  const click2=el=>el&&el.dispatchEvent(new w.MouseEvent('click',{bubbles:true}));
  const hasCJK=s=>/[\u4e00-\u9fff]/.test(s||'');
  eq(w.document.documentElement.lang,'zh-Hant','fresh boot starts in zh when localStorage says so');
  click2(w.document.querySelector('.switch button[data-mode="timeline"]'));
  assert(q2('.tl-node text').some(t=>hasCJK(t.textContent)),'timeline built cold under zh shows localized concept names');
  click2(w.document.querySelector('.switch button[data-mode="lens"]'));
  click2(q2('.lb-cell')[0]); // enter a door so the ego-graph builds cold under zh
  assert(q2('#lens-svg g.lnode text').some(t=>hasCJK(t.textContent)),'idea lens built cold under zh shows localized concept names');
  click2(w.document.querySelector('.switch button[data-mode="constellation"]'));
  assert(q2('.cregion').some(t=>hasCJK(t.textContent)),'constellation built cold under zh shows localized region headings');
  assert(q2('.clegend .rg').some(t=>hasCJK(t.textContent)),'constellation legend headings localise under zh');
}

console.log(`SMOKE OK — ${PASS} assertions passed.`);
// Do NOT force exit. The known async d3-zoom error is swallowed by the
// uncaughtException handler above; the process then exits 0 on its own. Any
// real failure has already thrown synchronously and exited non-zero.
