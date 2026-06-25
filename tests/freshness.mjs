// Freshness checks — guard against the website drifting out of date.
// Run after the smoke test (which already proves atlas.html behaves). These
// three are static/consistency checks; the build-in-sync guard lives in
// `python3 build.py --check` and is run separately from `npm test`.
//
//   2. i18n coverage   — every UI string used (data-i18n + T('…')) has zh + ru
//   3. routes resolve  — every tab slug and deep-link lands on the right view
//   4. counts in sync  — the hard-coded copy numbers match the actual dataset
//   5. doc counts      — README + MISSION cite the current idea count, not a stale one
//
import { JSDOM } from 'jsdom'; import * as d3 from 'd3'; import fs from 'fs';

let PASS=0;
const fail=[];
function assert(cond,msg){ if(cond){PASS++; return;} fail.push(msg); }
function eq(a,b,msg){ assert(a===b, msg+` (got ${JSON.stringify(a)}, want ${JSON.stringify(b)})`); }

const html=fs.readFileSync('atlas.html','utf8');
const tpl =fs.readFileSync('src/template.html','utf8');
const i18n=JSON.parse(fs.readFileSync('src/i18n.json','utf8'));
const ideas=JSON.parse(fs.readFileSync('src/ideas.json','utf8'));
const atlas=JSON.parse(fs.readFileSync('src/atlas_graph.json','utf8'));

// ───────────────────────── 2. i18n coverage ─────────────────────────
// Collect every UI string the app will ask T() to translate: the static
// data-i18n="…" attributes plus the string-literal T('…') calls in the script.
// T() resolves against I18N.ui, so each key must carry both zh and ru there or
// it silently falls back to English.
const htmlUnescape=s=>s.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>')
  .replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&#(\d+);/g,(_,n)=>String.fromCharCode(+n));
const jsUnescape=s=>s.replace(/\\(['"\\])/g,'$1');

const keys=new Set();
for(const m of tpl.matchAll(/data-i18n="([^"]*)"/g)) keys.add(htmlUnescape(m[1]));
for(const m of tpl.matchAll(/\bT\(\s*(['"])((?:\\.|(?!\1).)*)\1/g)) keys.add(jsUnescape(m[2]));

const ui=i18n.ui||{};
const missing=[];
for(const k of keys){
  if(!k) continue;
  const e=ui[k];
  if(!e) { missing.push(`${JSON.stringify(k).slice(0,60)} — absent from i18n.ui`); continue; }
  if(!e.zh) missing.push(`${JSON.stringify(k).slice(0,60)} — missing zh`);
  if(!e.ru) missing.push(`${JSON.stringify(k).slice(0,60)} — missing ru`);
}
assert(keys.size>50, `collected a sane number of UI strings (${keys.size})`);
assert(missing.length===0, `every UI string has zh + ru — ${missing.length} gap(s):\n   `+missing.slice(0,25).join('\n   '));

// ───────────────────────── 4. counts in sync ─────────────────────────
// The landing front door + the atlas <meta> tags hard-code anchor numbers. They
// must equal the dataset, or the first thing a visitor reads is a lie. The
// "Begin Wondering" gate is gone; the counts now live in index.html's hero.
const landing=fs.readFileSync('index.html','utf8');
const conceptCount=ideas.concepts.length;
const qCount=ideas.questions.length;
const atlasCount=(atlas.nodes||[]).length;
const eras=ideas.concepts.map(c=>c.era).filter(e=>typeof e==='number');
const minEra=Math.min(...eras), maxEra=Math.max(...eras);
const years=maxEra-minEra;

const between=(s,a,b)=>{ const i=s.indexOf(a); if(i<0) return ''; const j=s.indexOf(b,i+a.length); return j<0?'':s.slice(i,j); };
const metaDesc=(html.match(/name="description"\s+content="([^"]*)"/)||[])[1]||'';
const counts=between(landing,'class="counts"','</div>');

assert(new RegExp(`\\b${conceptCount}\\s+ideas\\b`).test(metaDesc), `atlas meta description says "${conceptCount} ideas" (dataset count)`);
assert(counts.includes(`>${qCount}</b>`), `landing shows ${qCount} questions (dataset count)`);
assert(counts.includes(`>${conceptCount}</b>`), `landing shows ${conceptCount} ideas (dataset count)`);
assert(counts.includes(`>${atlasCount}</b>`), `landing shows ${atlasCount} thinkers (atlas node count)`);
assert(counts.includes(`>${years}</b>`), `landing shows ${years} years (maxEra−minEra)`);

// ───────────────────────── 5. doc counts in sync ─────────────────────────
// The living docs cite the idea count in prose, and no build step regenerates
// them — so they silently drift (README read "269", MISSION "263" while the
// dataset had already moved to ${conceptCount}). Guard the headline number so a
// round bump can't ship a doc that contradicts the app. Dated audit records
// (docs/CONCEPT-GAPS.md, the *-CRITIQUE.md panels) are point-in-time snapshots
// and are intentionally NOT checked.
const ideasRe=new RegExp(`\\b${conceptCount}\\s+ideas\\b`);
for(const f of ['README.md','docs/MISSION.md']){
  const txt=fs.readFileSync(f,'utf8');
  assert(ideasRe.test(txt), `${f} cites the current idea count ("${conceptCount} ideas")`);
}

// ───────────────────────── 3. routes resolve ─────────────────────────
// Boot the real app in jsdom and drive the hash router: every tab slug and the
// canonical deep-links must land on the right view without throwing.
function boot(){
  const dom=new JSDOM(html,{pretendToBeVisual:true,url:'https://example.org/app'});
  const w=dom.window;
  global.window=w; global.document=w.document;
  global.SVGElement=w.SVGElement; global.Element=w.Element; global.HTMLElement=w.HTMLElement;
  global.localStorage=w.localStorage; global.location=w.location; global.history=w.history;
  w.d3=d3; w.matchMedia=()=>({matches:false,addEventListener(){}}); global.matchMedia=w.matchMedia;
  w.requestAnimationFrame=cb=>setTimeout(()=>cb(Date.now()),0);
  for(const id of ['m-questions','m-timeline','m-constellation','m-lens']){const el=w.document.getElementById(id);
    Object.defineProperty(el,'clientWidth',{value:1180,configurable:true});Object.defineProperty(el,'clientHeight',{value:640,configurable:true});}
  w.Element.prototype.scrollIntoView=function(){};
  const bodyEnd=html.lastIndexOf('</body>');
  const appOpen=html.lastIndexOf('<script>',bodyEnd);
  const appClose=html.lastIndexOf('</script>',bodyEnd);
  const code=html.slice(appOpen+'<script>'.length,appClose);
  new w.Function('d3','window','document',code)(d3,w,w.document);
  return w;
}
process.on('uncaughtException',e=>{ const m=String(e&&e.message||e);
  if(/viewBox|baseVal|getScreenCTM|createSVGMatrix/i.test(m)) return; // known jsdom/d3 noise
  console.error('UNCAUGHT (real):',e); process.exit(1); });

const w=boot();
const go=h=>{ w.location.hash=h; w.dispatchEvent(new w.HashChangeEvent('hashchange')); };
const mode=()=>w.document.querySelector('.switch button.active')?.dataset.mode;
const someConcept=ideas.concepts[0].id;
const somePerson=(atlas.nodes||[])[0]?.id;

// tab slugs → internal modes
for(const [slug,want] of [['questions','questions'],['timeline','timeline'],['concepts','lens'],['thinkers','constellation']])
  { go('#/'+slug); eq(mode(),want,`#/${slug} activates the ${want} view`); }
// legacy ids still resolve (old shared links must not break)
go('#/lens'); eq(mode(),'lens','legacy #/lens still resolves to the Concepts view');
go('#/constellation'); eq(mode(),'constellation','legacy #/constellation still resolves to the Thinkers view');
// deep links
go('#/concepts/'+encodeURIComponent(someConcept));
eq(mode(),'lens','#/concepts/<id> opens the Concepts view');
eq(w.document.getElementById('lens-board').hidden,true,'#/concepts/<id> drops past the board to a focused graph');
go('#/questions/idea/'+encodeURIComponent(someConcept));
assert(w.document.getElementById('drawer').classList.contains('open'),'#/questions/idea/<id> opens the concept dossier');
if(somePerson){ go('#/thinkers/person/'+encodeURIComponent(somePerson));
  eq(mode(),'constellation','#/thinkers/person/<id> opens the Thinkers view');
  assert(w.document.getElementById('drawer').classList.contains('open'),'#/thinkers/person/<id> opens the thinker dossier'); }

// ───────────────────────── report ─────────────────────────
if(fail.length){ console.error(`FRESHNESS FAILED — ${fail.length} check(s):`);
  for(const f of fail) console.error('  ✗ '+f); process.exit(1); }
console.log(`FRESHNESS OK — ${PASS} checks passed.`);
