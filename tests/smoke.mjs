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
for(const id of ['m-questions','m-timeline','m-web','m-threads','m-constellation','m-lens']){const el=window.document.getElementById(id);
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

// init state
eq($('.switch button.active')?.dataset.mode,'questions','init mode is questions');
eq($('.switch button.active')?.getAttribute('aria-selected'),'true','active tab aria-selected');
// The empty-state overlay must be truly invisible on load, not merely carry the
// [hidden] attribute: an ID rule (#empty-state{display:flex}) outranks the UA
// [hidden]{display:none}, so the attribute alone does NOT hide it. Assert the
// CSS cascade actually collapses it (regression guard for the always-on overlay).
eq(window.getComputedStyle($('#empty-state')).display,'none','empty-state is display:none on load (not just [hidden])');

// build every mode without throwing
for(const mo of ['timeline','web','threads','constellation','lens','questions']) click($('.switch button[data-mode="'+mo+'"]'));
console.log('6 modes built ok');

// LENS (Map VI): "Eleven Doors In" board → focus+context ego-graph
click($('.switch button[data-mode="lens"]'));
eq($('.switch button.active')?.dataset.mode, 'lens', 'lens tab activates');
eq($('#lens-board').hidden, false, 'lens opens on the Eleven Doors board');
eq($$('.lb-cell').length, 11, 'board shows eleven question doors (one per question)');
// the board is one screen, one verb: graph-only chrome must be hidden on it
eq($('#lens-ctrl').style.display, 'none', 'graph control bar is hidden on the board');
eq($('#lens-hint').style.display, 'none', 'graph hint is hidden on the board');
click($$('.lb-cell')[0]); // enter through the first door
eq($('#lens-board').hidden, true, 'choosing a door dismisses the board');
assert($('#lens-ctrl').style.display!=='none', 'control bar returns inside the graph');
eq($('#lens-home').hidden, false, 'the "Doors" home button appears once inside the graph');
assert($$('#lens-svg g.lnode').length>1, 'lens renders a focus node plus neighbours');
eq($$('#lens-svg g.lnode.focus').length, 1, 'exactly one focus node at the centre');
const lensName0=$('#lens-cap .lc-name')?.textContent||'';
assert(lensName0.length>0, 'lens caption names the focal idea');
const focusName0=$('#lens-svg g.lnode.focus text')?.textContent;
click($$('#lens-svg g.lnode')[1]); // travel to a neighbour
assert($('#lens-svg g.lnode.focus text')?.textContent!==focusName0, 'clicking a neighbour re-centres the lens');
click($('#lens-random')); // serendipity dice — must keep a valid focus
eq($$('#lens-svg g.lnode.focus').length, 1, 'random walk keeps a single focus');
// guided tour
click($('#lens-tour'));
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
esc(); click($('.switch button[data-mode="questions"]'));

// TIMELINE
click($('.switch button[data-mode="timeline"]'));
eq($$('#tl-svg .tl-node').length, D.concepts.length, 'timeline renders one node per concept');
eq($$('#tl-svg .tl-lane').length, 3, 'timeline has 3 lanes');
assert($$('#tl-svg .tl-tick').length>0, 'timeline has era ticks');

// THREADS
click($('.switch button[data-mode="threads"]'));
eq($$('#thr-list .thr-item').length, D.arguments.length, 'one thread item per argument');
const before=$('#thr-count').textContent; click($('#thr-next'));
assert($('#thr-count').textContent!==before, 'Next advances the thread counter');
assert($$('#thr-rail .thr-dot').length>0, 'thread rail has step dots');
const stepName=$('#thr-open')||$('.thr-name');
assert(stepName && stepName.textContent.trim().length>0, 'thread step shows a non-empty name');
click($$('.thr-item')[3]);
assert(($('#thr-title')?.textContent||'').length>0, 'clicking a thread sets its title');

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

// FOIL (argues against)
openByName('Modern Virtue Ethics');
assert(($('#dr-foil')?.textContent||'').length>0, 'foil shown for a concept that rejects others');

// DEEP LINK
openByName('Capitalist Realism');
assert(/#\/questions\/idea\//.test(window.location.hash), 'opening a concept writes a deep-link hash');
window.location.hash='#/threads/2.1';
window.dispatchEvent(new window.window.HashChangeEvent('hashchange'));
eq($('.switch button.active')?.dataset.mode, 'threads', 'hashchange routes to threads mode');

// ABOUT modal: opens, Esc closes, focus restored to the trigger
click($('.switch button[data-mode="questions"]'));
const aboutBtn=$('#about-btn'); aboutBtn.focus(); click(aboutBtn);
assert($('#about-overlay').classList.contains('open'), 'About panel opens');
assert($('#about-overlay').getAttribute('aria-modal')==='true', 'About panel is aria-modal');
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

console.log(`SMOKE OK — ${PASS} assertions passed.`);
// Do NOT force exit. The known async d3-zoom error is swallowed by the
// uncaughtException handler above; the process then exits 0 on its own. Any
// real failure has already thrown synchronously and exited non-zero.
