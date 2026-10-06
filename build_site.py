"""Build the MGMT 405 practice site.

Reads src/practice_questions.py + src/practice_mcqs.py, validates every
question, and writes one page per module to docs/ plus a docs/index.html
overview. GitHub Pages serves the docs/ folder, so each module gets a stable
URL the course calendar can link to directly, e.g. .../module-4-part-1.html

It also reads src/mock_midterm.py and writes docs/mock-midterm.html, a timed,
submit-once quiz in the format of the real midterm (Modules 1-3).

Do not edit docs/*.html by hand -- edit the sources and rerun this script.
"""
import json, sys, pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from practice_questions import QUESTIONS, MODULES
from practice_mcqs import ADDITIONAL_MCQS
from mock_midterm import MOCK

QUESTIONS = QUESTIONS + ADDITIONAL_MCQS
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

# ---------------- validation (whole bank) ----------------
ID_PREFIX = {m[0]: m[0].lower().replace("-", "") + "-" for m in MODULES}  # M4-I -> m4i-
seen_ids = set()
for q in QUESTIONS:
    assert "id" in q and "module" in q and "format" in q, f"missing core fields: {q}"
    assert q["id"] not in seen_ids, f"duplicate id {q['id']}"
    seen_ids.add(q["id"])
    assert q["module"] in ID_PREFIX, f"{q['id']} has unknown module {q['module']!r}"
    assert q["id"].startswith(ID_PREFIX[q["module"]]), f"{q['id']} does not match module {q['module']}"
    assert len(q["hints"]) == 3, f"{q['id']} needs 3 hints"
    assert q.get("solution"), f"{q['id']} needs a solution"
    if q["format"] == "mcq":
        assert len(q["choices"]) == 5, f"{q['id']} needs 5 choices"
        assert 0 <= q["correct_index"] < 5, f"{q['id']} bad correct_index"
    else:
        assert q["format"] == "open", f"{q['id']} unknown format {q['format']!r}"
        assert isinstance(q["answer"], (int, float)), f"{q['id']} needs a numeric answer"
        assert q["tolerance_abs"] >= 0, f"{q['id']} needs a non-negative tolerance"
    assert isinstance(q.get("order", 0), int), f"{q['id']} order must be an integer"
    # Each page carries the rounding and sign instructions at the top, so no question
    # repeats them (a per-question "enter a negative number" tells students the sign)
    for field in ("stem", "ask"):
        low = q[field].lower()
        assert "decimal place" not in low and "round to" not in low, \
            f"{q['id']} repeats the rounding instruction in {field}"
        assert "negative number" not in low and "negative for loss" not in low, \
            f"{q['id']} repeats the sign instruction in {field}"
    if q["format"] == "mcq":
        # "None/All of the above" only makes sense as the last option
        for i, c in enumerate(q["choices"][:-1]):
            assert "of the above" not in c.lower(), \
                f"{q['id']} option {chr(65 + i)} says '{c}' but is not the last option"

# ---------------- validation (mock midterm) ----------------
def _numeric_choice(c):
    t = c.replace(",", "").replace("$", "").replace("%", "").replace("+", "").replace("−", "-").strip()
    try:
        return float(t)
    except ValueError:
        return None

_mock_ids = set()
def _mock_id(i):
    assert i not in _mock_ids and i not in seen_ids, f"mock: duplicate id {i}"
    _mock_ids.add(i)

assert len(MOCK["mcqs"]) == 10, "mock: Part 1 needs exactly 10 multiple-choice questions"
for q in MOCK["mcqs"]:
    _mock_id(q["id"])
    assert len(q["choices"]) == 5 and 0 <= q["correct_index"] < 5, f"{q['id']}: needs 5 choices and a valid correct_index"
    assert q.get("solution") and q.get("module") and q.get("topic"), f"{q['id']}: needs module, topic and solution"
    for field in ("stem", "ask"):
        low = q[field].lower()
        assert "decimal place" not in low and "round to" not in low and "negative number" not in low, \
            f"{q['id']}: repeats the rounding or sign instruction in {field}"
    for i, c in enumerate(q["choices"][:-1]):
        assert "of the above" not in c.lower(), f"{q['id']}: option {chr(65 + i)} says 'of the above' but is not last"
    for c in q["choices"]:
        assert "approximately" not in c.lower() and "[" not in c, f"{q['id']}: option '{c}' singles itself out"
    nums = [_numeric_choice(c) for c in q["choices"]]
    if all(n is not None for n in nums):
        assert nums == sorted(nums), f"{q['id']}: numeric options must be in ascending order"
_pos = Counter(q["correct_index"] for q in MOCK["mcqs"])
assert max(_pos.values()) <= 3, f"mock: correct answers cluster on one letter: {dict(_pos)}"

_total = len(MOCK["mcqs"]) * MOCK["mcq_points"]
for p in MOCK["problems"]:
    _mock_id(p["id"])
    assert abs(sum(part["points"] for part in p["parts"]) - p["points"]) < 1e-9, \
        f"{p['id']}: part points do not add up to {p['points']}"
    _total += p["points"]
    for part in p["parts"]:
        _mock_id(part["id"])
        assert part.get("solution"), f"{part['id']}: needs a solution"
        low = part["text"].lower()
        assert "decimal place" not in low and "round to" not in low, f"{part['id']}: repeats the rounding instruction"
        pts = 0
        for it in part["items"]:
            _mock_id(it["id"])
            if it["kind"] == "select":
                assert 0 <= it["correct"] < len(it["options"]), f"{it['id']}: bad correct index"
                pts += it["points"]
            elif it["kind"] == "number":
                assert isinstance(it["answer"], (int, float)) and it["tolerance"] >= 0, \
                    f"{it['id']}: needs a numeric answer and a non-negative tolerance"
                pts += it["points"]
            elif it["kind"] == "formula":
                fpts = 0
                for f in it["fields"]:
                    _mock_id(f["id"])
                    assert "{" + f["key"] + "}" in it["template"], f"{it['id']}: template has no slot for {f['key']}"
                    assert isinstance(f["answer"], (int, float)) and f["tolerance"] >= 0, \
                        f"{f['id']}: needs a numeric answer and a non-negative tolerance"
                    fpts += f["points"]
                assert abs(fpts - it["points"]) < 1e-9, f"{it['id']}: field points do not add up to {it['points']}"
                pts += it["points"]
            else:
                assert it["kind"] == "text", f"{it['id']}: unknown item kind {it['kind']!r}"
        for r in part.get("self_rubric", []):
            _mock_id(r["id"])
            pts += r["points"]
        assert abs(pts - part["points"]) < 1e-9, f"{part['id']}: items + self rubric = {pts} points, expected {part['points']}"
assert _total == 100, f"mock: total points = {_total}, expected 100"
for _txt in [q["stem"] + " " + q["ask"] for q in MOCK["mcqs"]] + \
            [p["intro"] + " " + " ".join(part["text"] for part in p["parts"]) for p in MOCK["problems"]]:
    assert " PC " not in _txt and "mon comp" not in _txt.lower(), "mock: spell out terms in student text"

# ---------------- shared CSS ----------------
CSS = """
:root {
  --bg:#fafaf7; --fg:#1a1a1a; --muted:#666; --line:#dcd9d2; --card:#fff;
  --accent:#0066cc; --accent-soft:#e6f0fa; --good:#2a8a3e; --good-soft:#e7f5ea;
  --warn:#b85c00; --warn-soft:#fff7ea; --bad:#b03030; --bad-soft:#fdecec;
}
* { box-sizing:border-box; }
body { margin:0; font-family:-apple-system,Segoe UI,sans-serif; background:var(--bg); color:var(--fg); line-height:1.5; }
header { background:#1f3a5f; color:#fff; padding:14px 22px; }
header h1 { margin:0; font-size:18px; font-weight:600; }
header .sub { color:#cfdbe8; font-size:13px; margin-top:2px; }
.modnav { background:#fff; border-bottom:1px solid var(--line); padding:0 10px; display:flex; overflow-x:auto; }
.modnav a { padding:11px 14px; font-size:13px; font-weight:600; color:var(--muted); text-decoration:none; border-bottom:3px solid transparent; white-space:nowrap; }
.modnav a:hover { color:var(--fg); background:#f5f3ec; }
.modnav a.active { color:var(--accent); border-bottom-color:var(--accent); }
.controls { background:#f0ede5; padding:8px 22px; display:flex; align-items:center; gap:14px; font-size:13px; border-bottom:1px solid var(--line); flex-wrap:wrap; }
.controls label { font-weight:600; }
.controls select { padding:4px 8px; font-size:13px; border:1px solid var(--line); border-radius:3px; background:#fff; }
.controls .stats { margin-left:auto; color:var(--muted); }
.controls .stats strong { color:var(--good); }
main { max-width:880px; margin:0 auto; padding:18px 22px 100px; }
.note { background:var(--accent-soft); color:var(--accent); border-left:3px solid var(--accent); padding:8px 12px; margin:0 0 14px; border-radius:0 4px 4px 0; font-size:13.5px; font-weight:600; }
.intro { color:var(--muted); font-size:14px; margin:4px 0 0; }
.cards { display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:14px; margin-top:18px; }
.card { display:block; background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px 18px; text-decoration:none; color:var(--fg); box-shadow:0 1px 2px rgba(0,0,0,0.03); }
.card:hover { border-color:var(--accent); box-shadow:0 2px 6px rgba(0,0,0,0.08); }
.card .mlabel { color:var(--accent); font-weight:700; font-size:13px; }
.card .mtitle { font-weight:600; margin:4px 0 8px; font-size:15px; line-height:1.35; }
.card .mmeta { color:var(--muted); font-size:12.5px; }
.card .mprog { margin-top:8px; font-size:12.5px; color:var(--muted); }
.card .mprog.some { color:var(--good); font-weight:600; }
.q { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:18px 22px; margin-bottom:14px; box-shadow:0 1px 2px rgba(0,0,0,0.03); }
.q.done.correct { border-left:4px solid var(--good); }
.q.done.failed  { border-left:4px solid var(--bad); }
.qhead { display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:8px; }
.qid { font-family:ui-monospace,Menlo,Consolas,monospace; color:var(--muted); font-size:12px; }
.qtag { display:inline-block; background:var(--accent-soft); color:var(--accent); border-radius:10px; padding:1px 8px; font-size:11px; font-weight:600; }
.qtag.mcq { background:#f5e9ff; color:#6a2cb0; }
.qtag.open { background:#e6f0fa; color:#0066cc; }
.qtheme { color:var(--muted); font-size:13px; font-weight:600; }
.qstatus { margin-left:auto; font-size:12px; font-weight:600; }
.qstatus.correct { color:var(--good); }
.qstatus.failed  { color:var(--bad); }
.qstem { font-size:14.5px; margin:10px 0; white-space:pre-wrap; }
.qask  { font-size:14.5px; font-weight:600; margin:10px 0; }
.input-row { display:flex; gap:8px; align-items:center; margin:14px 0; flex-wrap:wrap; }
.input-row input[type=number] { padding:6px 10px; font-size:15px; border:1px solid var(--line); border-radius:4px; width:160px; }
.input-row input[type=number]:disabled { background:#f4f4f4; color:#999; }
.unit { color:var(--muted); font-size:14px; }
.choices label { display:block; padding:7px 10px; margin:3px 0; cursor:pointer; border:1px solid var(--line); border-radius:4px; background:#fff; font-size:14px; }
.choices label:hover { background:#f5f3ec; }
.choices label.selected { background:var(--accent-soft); border-color:var(--accent); }
.choices input { margin-right:8px; }
button.action { padding:6px 14px; font-size:14px; font-weight:600; border:1px solid var(--accent); background:var(--accent); color:#fff; border-radius:4px; cursor:pointer; }
button.action:hover { background:#0055aa; }
button.action.secondary { background:#fff; color:var(--accent); }
button.action.secondary:hover { background:var(--accent-soft); }
button.action:disabled { background:#aaa; border-color:#aaa; cursor:not-allowed; }
.feedback { margin:8px 0; padding:8px 12px; border-radius:4px; font-size:13.5px; font-weight:600; }
.feedback.correct { background:var(--good-soft); color:var(--good); border-left:3px solid var(--good); }
.feedback.wrong   { background:var(--bad-soft); color:var(--bad); border-left:3px solid var(--bad); }
.feedback.info    { background:var(--accent-soft); color:var(--accent); border-left:3px solid var(--accent); }
.feedback.result  { padding:14px 18px; font-size:15.5px; border-left-width:5px; display:flex; align-items:center; gap:12px; }
.feedback.result .icon { font-size:28px; line-height:1; font-weight:700; }
.feedback.result .sub  { font-weight:500; opacity:0.85; font-size:13.5px; margin-left:4px; }
.hint { background:var(--warn-soft); border-left:3px solid var(--warn); padding:8px 12px; margin:6px 0; border-radius:0 4px 4px 0; font-size:13.5px; }
.hint b { color:var(--warn); }
.solution { background:#f5f3ec; border-left:3px solid #888; padding:10px 14px; margin:8px 0; border-radius:0 4px 4px 0; }
.solution h4 { margin:0 0 6px; font-size:13px; color:#444; text-transform:uppercase; letter-spacing:0.04em; }
.solution pre { margin:0; white-space:pre-wrap; font-family:ui-monospace,Menlo,Consolas,monospace; font-size:13px; line-height:1.5; }
.attempts { color:var(--muted); font-size:12px; margin-left:8px; }
.calc-toggle { position:fixed; bottom:18px; right:18px; padding:10px 14px; background:var(--accent); color:#fff; border:none; border-radius:50px; font-size:14px; font-weight:600; cursor:pointer; box-shadow:0 2px 8px rgba(0,0,0,0.15); z-index:90; }
.calc-toggle:hover { background:#0055aa; }
.calc { position:fixed; bottom:64px; right:18px; width:260px; background:#fff; border:1px solid var(--line); border-radius:8px; box-shadow:0 4px 16px rgba(0,0,0,0.18); padding:8px; display:none; z-index:90; }
.calc.show { display:block; }
.calc .display { background:#f5f3ec; border:1px solid var(--line); border-radius:4px; padding:10px 12px; font-family:ui-monospace,Menlo,Consolas,monospace; font-size:18px; text-align:right; min-height:44px; word-break:break-all; overflow-wrap:anywhere; }
.calc .keys { display:grid; grid-template-columns:repeat(5, 1fr); gap:4px; margin-top:6px; }
.calc .keys button { padding:9px 0; font-size:14px; font-weight:600; border:1px solid var(--line); background:#fff; cursor:pointer; border-radius:4px; }
.calc .keys button:hover { background:#f0ede5; }
.calc .keys button.op { background:var(--accent-soft); color:var(--accent); }
.calc .keys button.eq { background:var(--accent); color:#fff; grid-column:span 2; }
.calc .keys button.fn { background:#e9e6dd; color:#555; }
.calc .err { color:var(--bad); }
@media (max-width:640px) {
  main { padding:14px 14px 100px; }
  .calc { right:8px; left:8px; bottom:60px; width:auto; }
}
"""

# ---------------- calculator widget (shared by the module pages and the mock midterm) ----------------
CALC_HTML = """<button class="calc-toggle" id="calctoggle">🖩 Calculator</button>
<div class="calc" id="calc">
  <div class="display" id="calcdisp">0</div>
  <div class="keys">
    <button class="fn" data-act="clear">C</button>
    <button class="fn" data-act="back">⌫</button>
    <button class="fn" data-key="(">(</button>
    <button class="fn" data-key=")">)</button>
    <button class="op" data-key="/">÷</button>
    <button data-key="7">7</button>
    <button data-key="8">8</button>
    <button data-key="9">9</button>
    <button class="op" data-key="*">×</button>
    <button class="fn" data-act="sqrt">√</button>
    <button data-key="4">4</button>
    <button data-key="5">5</button>
    <button data-key="6">6</button>
    <button class="op" data-key="-">−</button>
    <button class="fn" data-key="**">x^y</button>
    <button data-key="1">1</button>
    <button data-key="2">2</button>
    <button data-key="3">3</button>
    <button class="op" data-key="+">+</button>
    <button class="fn" data-key=".">.</button>
    <button data-key="0">0</button>
    <button data-key="00">00</button>
    <button class="eq" data-act="eq">=</button>
  </div>
</div>"""

CALC_JS = """// ---- Calculator ----
const calc = document.getElementById('calc');
const calcDisp = document.getElementById('calcdisp');
let calcExpr = '';
function calcUpdate() { calcDisp.textContent = calcExpr || '0'; calcDisp.classList.remove('err'); }
function calcEval() {
  if (!calcExpr) return;
  try {
    if (!/^[\\d+\\-*/().\\s*]+$/.test(calcExpr.replace(/\\*\\*/g, ''))) throw 'bad';
    const v = Function('return (' + calcExpr + ')')();
    if (!isFinite(v)) throw 'overflow';
    calcExpr = String(+v.toFixed(10).replace(/\\.?0+$/, ''));
    calcUpdate();
  } catch (e) { calcDisp.textContent = 'Error'; calcDisp.classList.add('err'); calcExpr = ''; }
}
document.getElementById('calctoggle').addEventListener('click', () => calc.classList.toggle('show'));
document.querySelectorAll('.calc .keys button').forEach(b => {
  b.addEventListener('click', () => {
    const k = b.dataset.key, a = b.dataset.act;
    if (a === 'clear') { calcExpr = ''; calcUpdate(); }
    else if (a === 'back') { calcExpr = calcExpr.slice(0, -1); calcUpdate(); }
    else if (a === 'eq') { calcEval(); }
    else if (a === 'sqrt') {
      try {
        const v = calcExpr ? Function('return (' + calcExpr + ')')() : 0;
        if (v < 0) throw 'neg';
        calcExpr = String(+Math.sqrt(v).toFixed(10).replace(/\\.?0+$/, ''));
        calcUpdate();
      } catch (e) { calcDisp.textContent = 'Error'; calcDisp.classList.add('err'); calcExpr = ''; }
    }
    else if (k) { calcExpr += k; calcUpdate(); }
  });
});"""

# ---------------- module page template ----------------
PAGE_TMPL = """<!doctype html>
<html lang=en>
<meta charset=utf-8>
<meta name=viewport content="width=device-width, initial-scale=1">
<title>__PAGETITLE__</title>
<style>__CSS__</style>

<header>
  <h1>MGMT 405 — Practice Problems</h1>
  <div class="sub">__SUB__</div>
</header>

<nav class="modnav">__NAV__</nav>

<div class="controls">
  <label>Question type:</label>
  <select id="typefilter">
    <option value="all">All</option>
    <option value="open">Open (numeric answer)</option>
    <option value="mcq">Multiple choice</option>
  </select>
  <span class="stats">
    <span id="progress">0 / 0 attempted</span> · <strong id="correct">0 correct</strong>
    <button id="reset" style="margin-left:8px; font-size:11px; padding:2px 8px; background:#fff; border:1px solid var(--line); border-radius:3px; cursor:pointer;">Reset this module</button>
  </span>
</div>

<main>
  <div class="note">Please round all numbers to one decimal place (e.g., 43.6791 &rarr; 43.7). Enter a loss as a negative number.</div>
  <div id="main"></div>
</main>

__CALC_HTML__

<script id="QDATA" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('QDATA').textContent);
const QS = D.questions;

// ---- Per-question state, persisted in localStorage (shared across module pages) ----
const STATE_KEY = 'mgmt405_practice_v1';
let STATE = {};
try { STATE = JSON.parse(localStorage.getItem(STATE_KEY)) || {}; } catch (_) { STATE = {}; }
function saveState() { try { localStorage.setItem(STATE_KEY, JSON.stringify(STATE)); } catch (_) {} }
function getQState(qid) {
  if (!STATE[qid]) STATE[qid] = {attempts:0, hints_shown:0, completed:false, last_answer_correct:false, mcq_choice:null, last_input:'', show_solution:false};
  if (STATE[qid].show_solution === undefined) STATE[qid].show_solution = false;
  return STATE[qid];
}

let typeFilter = 'all';

function escapeHTML(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// Stems and asks are plain text except that **text** renders bold (the only markup allowed).
function fmt(s) {
  return escapeHTML(s).replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>');
}

// ---- Stats ----
function updateStats() {
  let attempted = 0, correct = 0, total = 0;
  for (const q of QS) {
    if (typeFilter !== 'all' && q.format !== typeFilter) continue;
    total++;
    const s = STATE[q.id];
    if (s && (s.completed || s.attempts > 0)) attempted++;
    if (s && s.last_answer_correct) correct++;
  }
  document.getElementById('progress').textContent = attempted + ' / ' + total + ' attempted';
  document.getElementById('correct').textContent = correct + ' correct';
}

// ---- Render questions ----
function renderQuestions() {
  const main = document.getElementById('main');
  main.innerHTML = '';
  const filtered = QS.filter(q => typeFilter === 'all' || q.format === typeFilter);
  if (filtered.length === 0) {
    main.innerHTML = '<p style="color:var(--muted)">No questions match the current filter.</p>';
    updateStats(); return;
  }
  for (const q of filtered) {
    main.appendChild(renderQuestion(q));
  }
  updateStats();
}

function renderQuestion(q) {
  const s = getQState(q.id);
  const card = document.createElement('div');
  card.className = 'q';
  if (s.completed) card.classList.add('done', s.last_answer_correct ? 'correct' : 'failed');

  const head = document.createElement('div');
  head.className = 'qhead';
  head.innerHTML =
    '<span class="qtag ' + q.format + '">' + (q.format === 'open' ? 'OPEN' : 'MCQ') + '</span>' +
    '<span class="qtheme">' + escapeHTML(q.theme) + '</span>' +
    '<span class="qid">' + q.id + '</span>' +
    '<span class="qstatus ' + (s.completed ? (s.last_answer_correct ? 'correct' : 'failed') : '') + '">' +
      (s.completed ? (s.last_answer_correct ? '✓ Solved' : '✗ See solution') : '') +
    '</span>';
  card.appendChild(head);

  const stem = document.createElement('div');
  stem.className = 'qstem';
  stem.innerHTML = fmt(q.stem);
  card.appendChild(stem);

  const ask = document.createElement('div');
  ask.className = 'qask';
  ask.innerHTML = fmt(q.ask);
  card.appendChild(ask);

  // Input area
  const inputArea = document.createElement('div');
  if (q.format === 'open') {
    inputArea.className = 'input-row';
    const inp = document.createElement('input');
    inp.type = 'number';
    inp.step = 'any';
    inp.placeholder = 'Numeric answer';
    inp.value = s.last_input || '';
    if (s.completed) inp.disabled = true;
    inp.dataset.qid = q.id;
    inputArea.appendChild(inp);
    if (q.unit) {
      const u = document.createElement('span');
      u.className = 'unit';
      u.textContent = q.unit;
      inputArea.appendChild(u);
    }
    if (!s.completed) {
      const btn = document.createElement('button');
      btn.className = 'action';
      btn.textContent = 'Check answer';
      btn.dataset.qid = q.id;
      btn.dataset.action = 'submit-open';
      inputArea.appendChild(btn);
    } else if (s.last_answer_correct) {
      const btn = document.createElement('button');
      btn.className = 'action secondary';
      btn.textContent = s.show_solution ? 'Hide solution' : 'Show solution';
      btn.dataset.qid = q.id;
      btn.dataset.action = 'toggle-solution';
      inputArea.appendChild(btn);
    }
    if (!s.completed && s.attempts > 0) {
      const att = document.createElement('span');
      att.className = 'attempts';
      att.textContent = 'Attempts: ' + s.attempts + ' / 3';
      inputArea.appendChild(att);
    }
  } else {
    inputArea.className = 'choices';
    inputArea.dataset.qid = q.id;
    for (let i = 0; i < q.choices.length; i++) {
      const lbl = document.createElement('label');
      const selected = s.mcq_choice === i;
      if (selected) lbl.classList.add('selected');
      lbl.innerHTML = '<input type="radio" name="' + q.id + '" value="' + i + '"' + (selected ? ' checked' : '') + (s.completed ? ' disabled' : '') + '> ' +
                     '<strong>' + String.fromCharCode(65 + i) + ')</strong> ' + escapeHTML(q.choices[i]);
      inputArea.appendChild(lbl);
    }
    const row = document.createElement('div');
    row.style.marginTop = '8px';
    if (!s.completed) {
      const btn = document.createElement('button');
      btn.className = 'action';
      btn.textContent = 'Check answer';
      btn.dataset.qid = q.id;
      btn.dataset.action = 'submit-mcq';
      row.appendChild(btn);
    } else if (s.last_answer_correct) {
      const btn = document.createElement('button');
      btn.className = 'action secondary';
      btn.textContent = s.show_solution ? 'Hide solution' : 'Show solution';
      btn.dataset.qid = q.id;
      btn.dataset.action = 'toggle-solution';
      row.appendChild(btn);
    }
    if (!s.completed && s.attempts > 0) {
      const att = document.createElement('span');
      att.className = 'attempts';
      att.textContent = 'Attempts: ' + s.attempts + ' / 3';
      row.appendChild(att);
    }
    inputArea.appendChild(row);
  }
  card.appendChild(inputArea);

  // Feedback and hints
  const fb = document.createElement('div');
  fb.className = 'feedback-area';
  fb.dataset.qid = q.id;
  card.appendChild(fb);

  if (s.completed) {
    const resDiv = document.createElement('div');
    resDiv.className = 'feedback result ' + (s.last_answer_correct ? 'correct' : 'wrong');
    if (s.last_answer_correct) {
      const tag = s.hints_shown > 0 ? '(after ' + s.hints_shown + ' hint' + (s.hints_shown > 1 ? 's' : '') + ')' : '(first try)';
      resDiv.innerHTML = '<span class="icon">✓</span><span><strong>Correct!</strong> <span class="sub">' + tag + '</span></span>';
    } else {
      resDiv.innerHTML = '<span class="icon">✗</span><span><strong>Incorrect.</strong> <span class="sub">No attempts remaining — full solution shown below.</span></span>';
    }
    fb.appendChild(resDiv);
  } else if (s.attempts > 0) {
    const left = 3 - s.attempts;
    const tail = left >= 0 ? ' (' + Math.max(left, 0) + ' attempt' + (left === 1 ? '' : 's') + ' left)' : '';
    const wrongDiv = document.createElement('div');
    wrongDiv.className = 'feedback wrong';
    wrongDiv.innerHTML = '<strong>✗ Not quite — try again.</strong> Hint ' + s.hints_shown + ' revealed below.' + tail;
    fb.appendChild(wrongDiv);
  }
  if (s.hints_shown > 0) renderHints(fb, q, s.hints_shown);
  if (s.completed && (!s.last_answer_correct || s.show_solution)) renderSolution(fb, q);

  return card;
}

function renderHints(container, q, n_shown) {
  container.querySelectorAll('.hint').forEach(el => el.remove());
  for (let i = 0; i < n_shown && i < q.hints.length; i++) {
    const h = document.createElement('div');
    h.className = 'hint';
    h.innerHTML = '<b>Hint ' + (i+1) + ':</b> ' + escapeHTML(q.hints[i]);
    container.appendChild(h);
  }
}

function renderSolution(container, q) {
  if (container.querySelector('.solution')) return;
  const sol = document.createElement('div');
  sol.className = 'solution';
  sol.innerHTML = '<h4>Full solution</h4><pre>' + escapeHTML(q.solution) + '</pre>';
  container.appendChild(sol);
}

// ---- Answer checking ----
function checkOpen(q, value) {
  const userVal = parseFloat(value);
  if (isNaN(userVal)) return {ok:false, msg:'Please enter a numeric answer.'};
  const tol = q.tolerance_abs || 0;
  const correct = Math.abs(userVal - q.answer) <= tol;
  return {ok:correct, msg: correct ? 'Correct!' : 'Not quite — try again.'};
}

function checkMCQ(q, choiceIndex) {
  if (choiceIndex === null || choiceIndex === undefined) return {ok:false, msg:'Pick an option first.'};
  const correct = choiceIndex === q.correct_index;
  return {ok:correct, msg: correct ? 'Correct!' : 'Not quite — try again.'};
}

// ---- Submit handler ----
document.addEventListener('click', e => {
  if (e.target.dataset.action === 'submit-open' || e.target.dataset.action === 'submit-mcq') {
    handleSubmit(e.target);
  } else if (e.target.dataset.action === 'toggle-solution') {
    const qid = e.target.dataset.qid;
    const s = getQState(qid);
    s.show_solution = !s.show_solution;
    saveState();
    renderQuestions();
  }
});

function handleSubmit(btn) {
  const qid = btn.dataset.qid;
  const q = QS.find(x => x.id === qid);
  const s = getQState(qid);

  if (s.completed) return;

  let result;
  if (q.format === 'open') {
    const inp = btn.parentElement.querySelector('input[type=number]');
    s.last_input = inp.value;
    result = checkOpen(q, inp.value);
  } else {
    const sel = document.querySelector('.choices[data-qid="' + qid + '"] input[type=radio]:checked');
    const choiceIndex = sel ? parseInt(sel.value) : null;
    s.mcq_choice = choiceIndex;
    result = checkMCQ(q, choiceIndex);
  }

  if (result.ok) {
    s.attempts += 1;
    s.completed = true;
    s.last_answer_correct = true;
    s.show_solution = false;
    saveState();
    renderQuestions();
    return;
  }

  s.attempts += 1;
  if (s.attempts <= 3) {
    if (s.hints_shown < s.attempts) s.hints_shown = s.attempts;
  } else {
    s.completed = true;
    s.last_answer_correct = false;
    s.show_solution = true;
    s.hints_shown = q.hints.length;
  }
  saveState();
  renderQuestions();
}

// MCQ choice highlighting
document.addEventListener('change', e => {
  if (e.target.matches('.choices input[type=radio]')) {
    const parent = e.target.closest('.choices');
    parent.querySelectorAll('label').forEach(l => l.classList.remove('selected'));
    e.target.closest('label').classList.add('selected');
  }
});

// ---- Filters ----
document.getElementById('typefilter').addEventListener('change', e => {
  typeFilter = e.target.value;
  renderQuestions();
});
document.getElementById('reset').addEventListener('click', () => {
  if (!confirm('Reset your progress on this module? This cannot be undone.')) return;
  for (const q of QS) delete STATE[q.id];
  saveState();
  renderQuestions();
});

__CALC_JS__

// ---- Init ----
renderQuestions();
</script>
"""

# ---------------- index (overview) template ----------------
INDEX_TMPL = """<!doctype html>
<html lang=en>
<meta charset=utf-8>
<meta name=viewport content="width=device-width, initial-scale=1">
<title>MGMT 405 — Practice Problems</title>
<style>__CSS__</style>

<header>
  <h1>MGMT 405 — Practice Problems</h1>
  <div class="sub">Managerial Economics · Interactive practice with hints and step-by-step solutions</div>
</header>

<nav class="modnav">__NAV__</nav>

<main>
  <p class="intro">Pick a module below. Each question gives you three attempts, revealing one more hint after each miss; the full step-by-step solution appears once you solve it (or run out of attempts). Your progress is saved in this browser.</p>
  <div class="cards">__CARDS__</div>
</main>

<script id="QDATA" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('QDATA').textContent);
let STATE = {};
try { STATE = JSON.parse(localStorage.getItem('mgmt405_practice_v1')) || {}; } catch (_) { STATE = {}; }
for (const m of D.modules) {
  const el = document.querySelector('.mprog[data-slug="' + m.slug + '"]');
  if (!el) continue;
  let attempted = 0, correct = 0;
  for (const qid of m.ids) {
    const s = STATE[qid];
    if (s && (s.completed || s.attempts > 0)) attempted++;
    if (s && s.last_answer_correct) correct++;
  }
  if (attempted === 0) { el.textContent = 'Not started'; }
  else { el.textContent = attempted + ' / ' + m.ids.length + ' attempted · ' + correct + ' correct'; el.classList.add('some'); }
}
</script>
"""

# ---------------- mock midterm template ----------------
# A timed, submit-once quiz that imitates a Canvas (BruinLearn) quiz: start screen,
# countdown, question list, autosave in localStorage, confirmation on submit, then
# the auto-graded score, correct answers, step-by-step solutions and the rubric.
# Written as a raw string, so the JavaScript below uses single backslashes.
MOCK_CSS = """
.quiz-wrap { display:flex; gap:20px; max-width:1140px; margin:0 auto; padding:18px 22px 110px; align-items:flex-start; }
.quiz-main { flex:1 1 auto; min-width:0; }
.quiz-side { width:250px; flex:0 0 250px; position:sticky; top:12px; }
.side-box { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:12px 14px; margin-bottom:12px; }
.side-title { font-weight:700; font-size:12px; text-transform:uppercase; letter-spacing:0.05em; color:var(--muted); margin-bottom:6px; }
.timer { font-family:ui-monospace,Menlo,Consolas,monospace; font-size:28px; font-weight:700; line-height:1.1; }
.timer.urgent { color:var(--bad); }
.side-note { font-size:12px; color:var(--muted); margin-top:4px; }
.qlist { display:flex; flex-direction:column; }
.qlist a { font-size:13px; padding:2px 0; color:var(--fg); text-decoration:none; white-space:nowrap; }
.qlist a:hover { color:var(--accent); }
.qlist a .dot { display:inline-block; width:18px; color:var(--muted); }
.qlist a.answered .dot { color:var(--good); }
.qlist a.partial .dot { color:var(--warn); }
.quiz-side button.action { width:100%; padding:10px 14px; font-size:15px; }
.parth { font-size:17px; margin:22px 0 10px; }
.pintro { background:#eef3f8; border:1px solid #cfdbe8; border-radius:8px; padding:12px 18px; margin:0 0 14px; }
.pintro .ptitle { font-weight:700; font-size:15px; }
.qbox { background:var(--card); border:1px solid var(--line); border-radius:8px; margin-bottom:16px; box-shadow:0 1px 2px rgba(0,0,0,0.03); }
.qbox-head { display:flex; justify-content:space-between; align-items:center; background:#f0ede5; border-bottom:1px solid var(--line); padding:8px 16px; font-weight:700; font-size:14px; border-radius:8px 8px 0 0; }
.qbox-body { padding:12px 18px 16px; }
.qbox-body .qtag { margin-bottom:4px; }
.item-row { display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin:10px 0; font-size:14px; }
.item-row > label { flex:0 0 270px; font-weight:600; }
.item-row.col { flex-direction:column; align-items:stretch; gap:4px; }
.item-row.col > label { flex:none; }
input.num { padding:6px 10px; font-size:15px; border:1px solid var(--line); border-radius:4px; width:160px; font-family:inherit; }
input.num.short { width:92px; padding:4px 8px; }
.item-row select { padding:6px 10px; font-size:14px; border:1px solid var(--line); border-radius:4px; background:#fff; max-width:100%; }
.formula { font-family:ui-monospace,Menlo,Consolas,monospace; font-size:15px; display:inline-flex; align-items:center; gap:6px; flex-wrap:wrap; }
textarea.expl { width:100%; font:inherit; font-size:14px; padding:8px 10px; border:1px solid var(--line); border-radius:4px; resize:vertical; }
.submit-row { display:flex; align-items:center; gap:14px; margin:18px 0; flex-wrap:wrap; }
button.action.big { padding:10px 22px; font-size:16px; }
.choices-r .choice-r { padding:7px 10px; margin:3px 0; border:1px solid var(--line); border-radius:4px; font-size:14px; background:#fff; }
.choice-r.right { background:var(--good-soft); border-color:var(--good); }
.choice-r.wrong { background:var(--bad-soft); border-color:var(--bad); }
.tag { display:inline-block; font-size:11px; font-weight:700; border-radius:10px; padding:1px 8px; margin-left:6px; color:#fff; vertical-align:middle; }
.tag-ok { background:var(--good); }
.tag-you { background:#555; }
.res-row { display:grid; grid-template-columns:minmax(180px,1.4fr) minmax(120px,1fr) minmax(120px,1fr) 84px; gap:10px; align-items:center; font-size:13.5px; padding:7px 0; border-bottom:1px dashed var(--line); }
.res-row .res-label { font-weight:600; }
.res-row .res-rubric { font-weight:400; color:var(--muted); font-size:12.5px; }
.res-k { display:block; font-size:10.5px; text-transform:uppercase; letter-spacing:0.04em; color:var(--muted); }
.res-pts { text-align:right; font-weight:600; white-space:nowrap; }
.mark.ok { color:var(--good); font-weight:700; }
.mark.bad { color:var(--bad); font-weight:700; }
.res-text { margin:8px 0; font-size:13.5px; }
.res-text .res-label { font-weight:600; }
.res-quote { background:#f7f6f2; border-left:3px solid #bbb; padding:6px 10px; white-space:pre-wrap; margin-top:2px; }
.rubric { margin:12px 0 6px; font-size:13.5px; background:var(--warn-soft); border-left:3px solid var(--warn); padding:8px 12px; border-radius:0 4px 4px 0; }
.rubric-title { font-weight:700; color:var(--warn); margin-bottom:4px; }
.rubric label { display:block; padding:3px 0; cursor:pointer; }
.rubric .rpts { color:var(--muted); }
.sec-score { font-weight:700; margin:8px 0; }
.score-card { background:var(--card); border:1px solid var(--line); border-left:5px solid var(--accent); border-radius:8px; padding:16px 20px; margin:0 0 14px; }
.score-card .big { font-size:28px; font-weight:700; }
.score-sub { font-size:14px; margin-top:2px; }
.score-sub.muted { color:var(--muted); font-size:13px; }
main.start { max-width:780px; }
.start h2 { margin:0 0 10px; font-size:22px; }
.start h3 { margin:16px 0 6px; font-size:16px; }
.start table.meta td { padding:3px 16px 3px 0; font-size:14px; vertical-align:top; }
.start ul.instr { padding-left:20px; font-size:14px; }
.start ul.instr li { margin:4px 0; }
.figs { display:flex; flex-wrap:wrap; gap:8px; margin-top:8px; }
.sdfig { width:100%; max-width:330px; height:auto; background:#fff; border:1px solid var(--line); border-radius:6px; }
.sdfig.wide { max-width:400px; }
.sdfig .ax { stroke:#333; stroke-width:1.3; }
.sdfig .dem { stroke:#0066cc; stroke-width:2; fill:none; }
.sdfig .sup { stroke:#b85c00; stroke-width:2; fill:none; }
.sdfig .mr { stroke:#2a8a3e; stroke-width:2; fill:none; }
.sdfig .mc { stroke:#b03030; stroke-width:1.5; fill:none; }
.sdfig .dashed { stroke-dasharray:6 4; }
.sdfig .guide { stroke:#888; stroke-width:1; stroke-dasharray:2 3; }
.sdfig .shift { stroke:#444; stroke-width:1.5; }
.sdfig text { font-size:11px; font-family:-apple-system,Segoe UI,sans-serif; fill:#1a1a1a; }
.sdfig .ft { font-weight:700; font-size:12px; }
.sdfig .fl { fill:#555; }
.sdfig .cl { font-weight:700; }
.sdfig .pt { fill:#1a1a1a; }
.sdfig .pt.p1 { fill:#b03030; }
@media (max-width:860px) {
  .quiz-wrap { flex-direction:column; padding:14px 14px 110px; }
  .quiz-side { width:auto; flex:none; position:static; }
  .qlist { flex-direction:row; flex-wrap:wrap; gap:2px 12px; }
  .item-row > label { flex:1 1 100%; }
  .res-row { grid-template-columns:1fr 1fr; }
  .res-row .res-label { grid-column:1 / -1; }
  .res-pts { text-align:left; }
}
"""

MOCK_TMPL = r"""<!doctype html>
<html lang=en>
<meta charset=utf-8>
<meta name=viewport content="width=device-width, initial-scale=1">
<title>Mock Midterm · MGMT 405 Practice</title>
<style>__CSS__
__MOCKCSS__</style>

<header>
  <h1>MGMT 405 — Practice Problems</h1>
  <div class="sub">Mock Midterm: Modules 1–3 · 100 points · 2-hour time limit · same format as the real midterm</div>
</header>

<nav class="modnav">__NAV__</nav>

<div id="app"></div>

__CALC_HTML__

<script id="QDATA" type="application/json">__DATA__</script>
<script>
'use strict';
const D = JSON.parse(document.getElementById('QDATA').textContent);
const KEY = D.state_key;
const LIMIT_MS = D.time_limit_minutes * 60 * 1000;
const P1_PTS = D.mcqs.length * D.mcq_points;
const P2_PTS = D.problems.reduce((a, p) => a + p.points, 0);
const app = document.getElementById('app');
let S = loadState();
let timerHandle = null;
let figCounter = 0;

// ---- State: one attempt, saved in localStorage under its own key ----
function loadState() {
  try {
    const s = JSON.parse(localStorage.getItem(KEY));
    if (s && s.status) { s.answers = s.answers || {}; s.self = s.self || {}; return s; }
  } catch (_) {}
  return {status: 'not_started', answers: {}, self: {}};
}
function saveState() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (_) {} }

// ---- Helpers ----
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
function fmt(s) { return esc(s).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>'); }
function fmtNum(v) {
  if (typeof v !== 'number') return esc(v);
  if (Number.isInteger(v)) return v.toLocaleString('en-US');
  return (+v.toFixed(4)).toLocaleString('en-US', {maximumFractionDigits: 4});
}
function fmtPts(v) { return Number.isInteger(v) ? String(v) : String(+v.toFixed(2)); }
function parseNum(s) {
  if (s === null || s === undefined) return NaN;
  const t = String(s).replace(/−/g, '-').replace(/[\s,$%]/g, '');
  if (t === '' || t === '-' || t === '.' || t === '-.') return NaN;
  return Number(t);
}
function hms(ms) {
  const s = Math.max(0, Math.floor(ms / 1000));
  return Math.floor(s / 3600) + ':' + String(Math.floor((s % 3600) / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
}
function isSet(v) { return v !== undefined && v !== null && v !== ''; }

// ---- Structure: one section per multiple-choice question and per problem part ----
const SECTIONS = [];
D.mcqs.forEach((q, i) => SECTIONS.push({id: q.id, kind: 'mcq', label: 'Question ' + (i + 1), points: D.mcq_points, q: q}));
D.problems.forEach((p, pi) => p.parts.forEach(part => SECTIONS.push({id: part.id, kind: 'part', label: 'Problem ' + (pi + 1) + ' ' + part.label, points: part.points, part: part, problem: p})));

// ---- Gradable items, flattened ----
const ITEMS = [];
D.mcqs.forEach(q => ITEMS.push({id: q.id, sec: q.id, kind: 'choice', points: D.mcq_points, correct: q.correct_index}));
D.problems.forEach(p => p.parts.forEach(part => part.items.forEach(it => {
  if (it.kind === 'number') ITEMS.push({id: it.id, sec: part.id, kind: 'number', points: it.points, answer: it.answer, tolerance: it.tolerance});
  else if (it.kind === 'select') ITEMS.push({id: it.id, sec: part.id, kind: 'choice', points: it.points, correct: it.correct});
  else if (it.kind === 'formula') it.fields.forEach(f => ITEMS.push({id: f.id, sec: part.id, kind: 'number', points: f.points, answer: f.answer, tolerance: f.tolerance}));
})));
const ITEM_BY_ID = {};
ITEMS.forEach(it => { ITEM_BY_ID[it.id] = it; });

function checkItem(it) {
  const a = S.answers[it.id];
  if (it.kind === 'choice') return {answered: isSet(a), ok: isSet(a) && Number(a) === it.correct};
  const v = parseNum(a);
  const answered = !isNaN(v);
  const answers = Array.isArray(it.answer) ? it.answer : [it.answer];
  return {answered: answered, ok: answered && answers.some(x => Math.abs(v - x) <= it.tolerance + 1e-9)};
}
function sectionState(sec) {
  // every gradable field, plus every free-text box, counts as something to answer
  const answered = [];
  if (sec.kind === 'mcq') answered.push(checkItem(ITEM_BY_ID[sec.id]).answered);
  else sec.part.items.forEach(it => {
    if (it.kind === 'text') answered.push(!!(S.answers[it.id] && String(S.answers[it.id]).trim()));
    else if (it.kind === 'formula') it.fields.forEach(f => answered.push(checkItem(ITEM_BY_ID[f.id]).answered));
    else answered.push(checkItem(ITEM_BY_ID[it.id]).answered);
  });
  const n = answered.filter(a => a).length;
  return n === 0 ? 'none' : (n === answered.length ? 'all' : 'partial');
}
function computeScore() {
  let auto = 0, autoMax = 0, selfPts = 0, selfMax = 0;
  const per = {};
  for (const it of ITEMS) { autoMax += it.points; const r = checkItem(it); per[it.id] = r; if (r.ok) auto += it.points; }
  for (const p of D.problems) for (const part of p.parts) for (const r of (part.self_rubric || [])) { selfMax += r.points; if (S.self[r.id]) selfPts += r.points; }
  return {auto: auto, autoMax: autoMax, selfPts: selfPts, selfMax: selfMax, per: per, total: auto + selfPts, max: autoMax + selfMax};
}
function sectionScore(sec, sc) {
  let earned = 0;
  for (const it of ITEMS) if (it.sec === sec.id && sc.per[it.id].ok) earned += it.points;
  if (sec.kind === 'part') for (const r of (sec.part.self_rubric || [])) if (S.self[r.id]) earned += r.points;
  return earned;
}
function storeScore(sc) { S.score_auto = sc.auto; S.score_total = sc.total; saveState(); }

// ---- Timer ----
function startTimer() { stopTimer(); tick(); timerHandle = setInterval(tick, 500); }
function stopTimer() { if (timerHandle) { clearInterval(timerHandle); timerHandle = null; } }
function tick() {
  if (S.status !== 'in_progress') { stopTimer(); return; }
  const left = S.started_at + LIMIT_MS - Date.now();
  const el = document.getElementById('timer');
  if (left <= 0) { if (el) el.textContent = '0:00:00'; submitQuiz(true); return; }
  if (el) { el.textContent = hms(left); el.classList.toggle('urgent', left < 5 * 60 * 1000); }
}

// ---- Attempt lifecycle ----
function start() {
  S = {status: 'in_progress', started_at: Date.now(), answers: {}, self: {}};
  saveState(); renderQuiz(); window.scrollTo(0, 0);
}
function confirmSubmit() {
  const n = SECTIONS.filter(sec => sectionState(sec) !== 'all').length;
  const msg = (n ? 'You have ' + n + ' question' + (n > 1 ? 's' : '') + ' without a complete answer. ' : '') +
              'Submit the quiz now? You cannot change your answers afterwards.';
  if (confirm(msg)) submitQuiz(false);
}
function submitQuiz(auto) {
  if (S.status !== 'in_progress') return;
  stopTimer();
  S.status = 'submitted';
  S.submitted_at = auto ? Math.min(Date.now(), S.started_at + LIMIT_MS) : Date.now();
  S.auto_submitted = !!auto;
  saveState();
  renderResults();
  window.scrollTo(0, 0);
  if (auto) setTimeout(() => alert('Time is up. Your quiz was submitted automatically.'), 100);
}
function retake() {
  if (!confirm('Start a new attempt? Your answers and results from this attempt will be erased.')) return;
  S = {status: 'not_started', answers: {}, self: {}};
  saveState(); renderStart(); window.scrollTo(0, 0);
}

// ---- Start screen ----
function renderStart() {
  stopTimer();
  let h = '<main class="start"><h2>' + esc(D.title) + ' — ' + esc(D.subtitle) + '</h2>';
  h += '<table class="meta">' +
    '<tr><td>Time limit</td><td><strong>' + (D.time_limit_minutes / 60) + ' hours</strong></td></tr>' +
    '<tr><td>Points</td><td><strong>' + (P1_PTS + P2_PTS) + '</strong> · Part 1: ' + D.mcqs.length + ' multiple-choice questions × ' + D.mcq_points + ' points (' + P1_PTS + ' points) · Part 2: ' + D.problems.length + ' problems (' + P2_PTS + ' points)</td></tr>' +
    '<tr><td>Covers</td><td>Modules 1, 2 and 3</td></tr>' +
    '<tr><td>Attempts</td><td>One; you can retake the quiz after seeing your results</td></tr></table>';
  h += '<div class="note">' + esc(D.rounding_note) + '</div>';
  h += '<h3>Instructions</h3><ul class="instr">' + D.start_notes.map(n => '<li>' + fmt(n) + '</li>').join('') + '</ul>';
  h += '<p style="margin-top:18px"><button class="action big" id="startbtn">Take the Quiz</button></p></main>';
  app.innerHTML = h;
}

// ---- Shared pieces ----
function boxHead(label, pts) {
  return '<div class="qbox-head"><span>' + esc(label) + '</span><span>' + fmtPts(pts) + ' pts</span></div>';
}
function problemIntro(p, pnum) {
  return '<div class="pintro" id="prob-' + p.id + '"><div class="ptitle">Problem ' + pnum + ' — ' + esc(p.title) + ' (' + fmtPts(p.points) + ' points)</div><div class="qstem">' + fmt(p.intro) + '</div></div>';
}
function inputHTML(id, cls) {
  const v = S.answers[id];
  return '<input type="text" inputmode="decimal" autocomplete="off" class="num' + (cls ? ' ' + cls : '') + '" data-item="' + id + '" value="' + esc(isSet(v) ? v : '') + '">';
}
function selectHTML(it) {
  const v = S.answers[it.id];
  let h = '<select data-item="' + it.id + '"><option value=""' + (isSet(v) ? '' : ' selected') + '>— choose —</option>';
  it.options.forEach((o, k) => { h += '<option value="' + k + '"' + (isSet(v) && Number(v) === k ? ' selected' : '') + '>' + esc(o) + '</option>'; });
  return h + '</select>';
}
function formulaHTML(it) {
  let t = esc(it.template);
  it.fields.forEach(f => { t = t.replace('{' + f.key + '}', inputHTML(f.id, 'short')); });
  return '<span class="formula">' + t + '</span>';
}
function itemQuizHTML(it) {
  if (it.kind === 'text') {
    const v = S.answers[it.id] || '';
    return '<div class="item-row col"><label>' + esc(it.label) + '</label><textarea class="expl" rows="' + (it.rows || 3) + '" data-item="' + it.id + '">' + esc(v) + '</textarea></div>';
  }
  let h = '<div class="item-row"><label>' + esc(it.label) + '</label>';
  if (it.kind === 'number') h += inputHTML(it.id) + (it.unit ? '<span class="unit">' + esc(it.unit) + '</span>' : '');
  else if (it.kind === 'select') h += selectHTML(it);
  else if (it.kind === 'formula') h += formulaHTML(it);
  return h + '</div>';
}

function mcqBox(sec, i, mode) {
  const q = sec.q;
  let h = '<div class="qbox" id="sec-' + q.id + '">' + boxHead(sec.label, sec.points) + '<div class="qbox-body">';
  if (mode === 'results') h += '<div class="qtag">' + esc(q.module) + ' · ' + esc(q.topic) + '</div>';
  h += '<div class="qstem">' + fmt(q.stem) + '</div><div class="qask">' + fmt(q.ask) + '</div>';
  const chosen = S.answers[q.id];
  if (mode === 'quiz') {
    h += '<div class="choices">';
    q.choices.forEach((c, k) => {
      const sel = isSet(chosen) && Number(chosen) === k;
      h += '<label' + (sel ? ' class="selected"' : '') + '><input type="radio" name="' + q.id + '" value="' + k + '" data-item="' + q.id + '"' + (sel ? ' checked' : '') + '> <strong>' + String.fromCharCode(65 + k) + ')</strong> ' + esc(c) + '</label>';
    });
    h += '</div>';
  } else {
    const r = checkItem(ITEM_BY_ID[q.id]);
    h += '<div class="choices-r">';
    q.choices.forEach((c, k) => {
      const sel = r.answered && Number(chosen) === k;
      const cls = k === q.correct_index ? ' right' : (sel ? ' wrong' : '');
      h += '<div class="choice-r' + cls + '"><strong>' + String.fromCharCode(65 + k) + ')</strong> ' + esc(c) +
           (k === q.correct_index ? '<span class="tag tag-ok">Correct answer</span>' : '') + (sel ? '<span class="tag tag-you">Your answer</span>' : '') + '</div>';
    });
    h += '</div>' + resultLine(r, sec.points) + '<div class="solution"><h4>Solution</h4><pre>' + esc(q.solution) + '</pre></div>';
  }
  return h + '</div></div>';
}
function resultLine(r, pts) {
  if (!r.answered) return '<div class="feedback wrong">Not answered · 0 / ' + fmtPts(pts) + ' pts</div>';
  return r.ok ? '<div class="feedback correct">Correct · ' + fmtPts(pts) + ' / ' + fmtPts(pts) + ' pts</div>'
              : '<div class="feedback wrong">Incorrect · 0 / ' + fmtPts(pts) + ' pts</div>';
}

function resRow(label, yours, right, earned, pts, ok, rubric) {
  return '<div class="res-row' + (ok ? ' ok' : ' bad') + '">' +
    '<div class="res-label">' + esc(label) + (rubric ? '<div class="res-rubric">' + esc(rubric) + '</div>' : '') + '</div>' +
    '<div class="res-cell"><span class="res-k">Your answer</span>' + yours + '</div>' +
    '<div class="res-cell"><span class="res-k">Correct</span>' + right + '</div>' +
    '<div class="res-pts"><span class="mark ' + (ok ? 'ok' : 'bad') + '">' + (ok ? '✓' : '✗') + '</span> ' + fmtPts(earned) + ' / ' + fmtPts(pts) + '</div></div>';
}
function withUnit(v, unit) {
  const u = (unit || '').replace(/ \(.*$/, '');
  if (u === '%') return fmtNum(v) + '%';
  if (u.charAt(0) === '$') return '$' + fmtNum(v) + esc(u.slice(1));
  return fmtNum(v) + (u ? ' ' + esc(u) : '');
}
function itemResultHTML(it, sc) {
  if (it.kind === 'text') {
    const v = S.answers[it.id];
    return '<div class="res-text"><div class="res-label">' + esc(it.label) + '</div><div class="res-quote">' + (v ? esc(v) : '<em>(no answer)</em>') + '</div></div>';
  }
  if (it.kind === 'formula') {
    let allOk = true, earned = 0, yours = esc(it.template), right = esc(it.template);
    it.fields.forEach(f => {
      const r = sc.per[f.id];
      if (r.ok) earned += f.points; else allOk = false;
      const v = S.answers[f.id];
      yours = yours.replace('{' + f.key + '}', '<span class="mark ' + (r.ok ? 'ok' : 'bad') + '">' + (r.answered ? esc(v) : '—') + '</span>');
      right = right.replace('{' + f.key + '}', fmtNum(f.answer));
    });
    return resRow(it.label, '<span class="formula">' + yours + '</span>', '<span class="formula">' + right + '</span>', earned, it.points, allOk, it.rubric);
  }
  const r = sc.per[it.id];
  const v = S.answers[it.id];
  let yours, right;
  if (it.kind === 'number') { yours = r.answered ? esc(v) : '—'; right = withUnit(it.answer, it.unit); }
  else { yours = r.answered ? esc(it.options[Number(v)]) : '—'; right = esc(it.options[it.correct]); }
  return resRow(it.label, yours, right, r.ok ? it.points : 0, it.points, r.ok, it.rubric);
}
function selfRubricHTML(part) {
  if (!part.self_rubric || !part.self_rubric.length) return '';
  let h = '<div class="rubric"><div class="rubric-title">Rubric: compare your answer with the solution below and tick what you got right</div>';
  part.self_rubric.forEach(r => {
    h += '<label><input type="checkbox" class="selfchk" data-rubric="' + r.id + '"' + (S.self[r.id] ? ' checked' : '') + '> ' + esc(r.text) +
         ' <span class="rpts">(' + fmtPts(r.points) + ' pt' + (r.points === 1 ? '' : 's') + ')</span></label>';
  });
  return h + '</div>';
}
function partBox(sec, mode, sc) {
  const part = sec.part;
  let h = '<div class="qbox" id="sec-' + part.id + '">' + boxHead(sec.label, sec.points) + '<div class="qbox-body"><div class="qstem">' + fmt(part.text) + '</div>';
  if (mode === 'quiz') {
    part.items.forEach(it => { h += itemQuizHTML(it); });
  } else {
    part.items.forEach(it => { h += itemResultHTML(it, sc); });
    h += selfRubricHTML(part);
    h += '<div class="sec-score" data-sec="' + part.id + '">Points (self-graded): ' + fmtPts(sectionScore(sec, sc)) + ' / ' + fmtPts(sec.points) + '</div>';
    h += '<div class="solution"><h4>Solution</h4><pre>' + esc(part.solution) + '</pre>' + figureHTML(part.figure) + '</div>';
  }
  return h + '</div></div>';
}

// ---- Quiz screen ----
function renderQuiz() {
  let main = '<div class="note">' + esc(D.rounding_note) + '</div>';
  main += '<h2 class="parth">Part 1 — Multiple choice (' + P1_PTS + ' points)</h2>';
  SECTIONS.filter(s => s.kind === 'mcq').forEach((sec, i) => { main += mcqBox(sec, i, 'quiz'); });
  main += '<h2 class="parth">Part 2 — Problem solving (' + P2_PTS + ' points)</h2>';
  D.problems.forEach((p, pi) => {
    main += problemIntro(p, pi + 1);
    SECTIONS.filter(s => s.kind === 'part' && s.problem === p).forEach(sec => { main += partBox(sec, 'quiz', null); });
  });
  main += '<div class="submit-row"><button class="action big" id="submitbtn">Submit Quiz</button><span class="side-note" id="unans"></span></div>';
  const side = '<div class="side-box"><div class="side-title">Time Running</div><div class="timer" id="timer">–:––:––</div><div class="side-note">The quiz is submitted automatically at 0:00:00.</div></div>' +
               '<div class="side-box"><div class="side-title">Questions</div><div class="qlist" id="qlist"></div></div>' +
               '<button class="action" id="submitbtn2">Submit Quiz</button>';
  app.innerHTML = '<div class="quiz-wrap"><div class="quiz-main">' + main + '</div><aside class="quiz-side">' + side + '</aside></div>';
  updateSide();
  startTimer();
}
function updateSide() {
  const list = document.getElementById('qlist');
  if (!list) return;
  let h = '', n = 0;
  SECTIONS.forEach(sec => {
    const st = sectionState(sec);
    if (st !== 'all') n++;
    h += '<a href="#sec-' + sec.id + '" class="' + (st === 'all' ? 'answered' : (st === 'partial' ? 'partial' : '')) + '"><span class="dot">' + (st === 'all' ? '✓' : (st === 'partial' ? '◐' : '○')) + '</span>' + esc(sec.label) + '</a>';
  });
  list.innerHTML = h;
  const u = document.getElementById('unans');
  if (u) u.textContent = n ? n + ' of ' + SECTIONS.length + ' questions still without a complete answer' : 'All questions answered';
}

// ---- Results screen ----
function scoreCardHTML(sc) {
  const used = S.submitted_at && S.started_at ? Math.min(S.submitted_at - S.started_at, LIMIT_MS) : 0;
  return '<div class="score-card" id="scorecard"><div class="big">Part 1, multiple choice: ' + fmtPts(sc.auto) + ' / ' + fmtPts(sc.autoMax) + ' points</div>' +
    '<div class="score-sub">Graded automatically. Part 2, problems (graded by you with the rubric lines below): <strong>' + fmtPts(sc.selfPts) + ' / ' + fmtPts(sc.selfMax) + '</strong> · Total: <strong>' + fmtPts(sc.total) + ' / ' + fmtPts(sc.max) + '</strong></div>' +
    '<div class="score-sub muted">Submitted ' + (S.submitted_at ? new Date(S.submitted_at).toLocaleString() : '') + ' · time used ' + hms(used) +
    (S.auto_submitted ? ' · submitted automatically when the time ran out' : '') + '</div></div>';
}
function renderResults() {
  stopTimer();
  const sc = computeScore();
  let h = '<main class="results">' + scoreCardHTML(sc) + '<div class="note">' + esc(D.results_note) + '</div>';
  h += '<h2 class="parth">Part 1 — Multiple choice (' + P1_PTS + ' points)</h2>';
  SECTIONS.filter(s => s.kind === 'mcq').forEach((sec, i) => { h += mcqBox(sec, i, 'results'); });
  h += '<h2 class="parth">Part 2 — Problem solving (' + P2_PTS + ' points)</h2>';
  D.problems.forEach((p, pi) => {
    h += problemIntro(p, pi + 1);
    SECTIONS.filter(s => s.kind === 'part' && s.problem === p).forEach(sec => { h += partBox(sec, 'results', sc); });
  });
  h += '<div class="submit-row"><button class="action secondary" id="retakebtn">Retake the quiz (erases this attempt)</button></div></main>';
  app.innerHTML = h;
  storeScore(sc);
}
function refreshScore() {
  const sc = computeScore();
  const card = document.getElementById('scorecard');
  if (card) card.outerHTML = scoreCardHTML(sc);
  document.querySelectorAll('.sec-score').forEach(el => {
    const sec = SECTIONS.find(s => s.id === el.dataset.sec);
    if (sec) el.textContent = 'Points (self-graded): ' + fmtPts(sectionScore(sec, sc)) + ' / ' + fmtPts(sec.points);
  });
  storeScore(sc);
}

// ---- Figures for the solutions (inline SVG) ----
function figureHTML(f) {
  if (!f) return '';
  if (f.kind === 'sd') return '<div class="figs">' + sdSVG(f) + '</div>';
  if (f.kind === 'sd2') return '<div class="figs">' + f.panels.map(sdSVG).join('') + '</div>';
  if (f.kind === 'dmr') return '<div class="figs">' + dmrSVG(f) + '</div>';
  return '';
}
// Supply and demand in a 0-100 box: demand P = a - Q, supply P = b + Q; the second
// value in f.d / f.s (if any) is the shifted curve.
function sdSVG(f) {
  const W = 330, H = 260, L = 46, R = 16, T = 38, B = 40;
  const X = q => L + (q / 100) * (W - L - R);
  const Y = p => H - B - (p / 100) * (H - B - T);
  const eq = (a, b) => ({q: (a - b) / 2, p: (a + b) / 2});
  const n = ++figCounter;
  const arrow = (x1, y1, x2, y2) => '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" class="shift" marker-end="url(#arr' + n + ')"/>';
  let s = '<svg viewBox="0 0 ' + W + ' ' + H + '" class="sdfig" role="img" aria-label="' + esc(f.title || 'Supply and demand') + '">';
  s += '<defs><marker id="arr' + n + '" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#444"/></marker></defs>';
  if (f.title) s += '<text x="' + (W / 2) + '" y="14" text-anchor="middle" class="ft">' + esc(f.title) + '</text>';
  s += '<line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(100) + '" y2="' + Y(0) + '" class="ax"/>';
  s += '<line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(0) + '" y2="' + Y(100) + '" class="ax"/>';
  s += '<text x="' + X(100) + '" y="' + (Y(0) + 28) + '" text-anchor="end" class="fl">Quantity</text>';
  s += '<text x="' + (X(0) + 4) + '" y="' + (Y(100) - 6) + '" class="fl">Price</text>';
  const dLine = (a, cls, label) => {
    const q2 = Math.min(a, 100);
    return '<line x1="' + X(0) + '" y1="' + Y(a) + '" x2="' + X(q2) + '" y2="' + Y(a - q2) + '" class="' + cls + '"/>' +
           '<text x="' + (X(q2) + 3) + '" y="' + (Y(a - q2) - 4) + '" class="cl">' + label + '</text>';
  };
  const sLine = (b, cls, label) => {
    const q2 = 100 - b;
    return '<line x1="' + X(0) + '" y1="' + Y(b) + '" x2="' + X(q2) + '" y2="' + Y(100) + '" class="' + cls + '"/>' +
           '<text x="' + (X(q2) + 3) + '" y="' + (Y(100) + 4) + '" class="cl">' + label + '</text>';
  };
  s += dLine(f.d[0], 'dem', 'D');
  if (f.d.length > 1) s += dLine(f.d[1], 'dem dashed', "D'");
  s += sLine(f.s[0], 'sup', 'S');
  if (f.s.length > 1) s += sLine(f.s[1], 'sup dashed', "S'");
  // py / qx: extra offsets for the axis labels, used when P1 would sit on top of P0 (or Q1 on Q0)
  const mark = (e, name, pl, ql, cls, py, qx) =>
    '<line x1="' + X(0) + '" y1="' + Y(e.p) + '" x2="' + X(e.q) + '" y2="' + Y(e.p) + '" class="guide"/>' +
    '<line x1="' + X(e.q) + '" y1="' + Y(0) + '" x2="' + X(e.q) + '" y2="' + Y(e.p) + '" class="guide"/>' +
    '<circle cx="' + X(e.q) + '" cy="' + Y(e.p) + '" r="3.5" class="pt ' + cls + '"/>' +
    '<text x="' + (X(e.q) + 6) + '" y="' + (Y(e.p) - 6) + '" class="cl">' + name + '</text>' +
    '<text x="' + (X(0) - 4) + '" y="' + (Y(e.p) + 4 + py) + '" text-anchor="end" class="al">' + pl + '</text>' +
    '<text x="' + (X(e.q) + qx) + '" y="' + (Y(0) + 13) + '" text-anchor="middle" class="al">' + ql + '</text>';
  const e0 = eq(f.d[0], f.s[0]);
  s += mark(e0, 'E', 'P0', 'Q0', 'p0', 0, 0);
  if (f.d.length > 1 || f.s.length > 1) {
    const e1 = eq(f.d.length > 1 ? f.d[1] : f.d[0], f.s.length > 1 ? f.s[1] : f.s[0]);
    const dy = Y(e1.p) - Y(e0.p), dx = X(e1.q) - X(e0.q);
    const py = Math.abs(dy) < 12 ? (dy <= 0 ? -(12 - Math.abs(dy)) : (12 - Math.abs(dy))) : 0;
    const qx = Math.abs(dx) < 24 ? (dx <= 0 ? -(24 - Math.abs(dx)) : (24 - Math.abs(dx))) : 0;
    s += mark(e1, "E'", 'P1', 'Q1', 'p1', py, qx);
    if (f.d.length > 1) { const pp = e0.p - 20; s += arrow(X(f.d[0] - pp), Y(pp), X(f.d[1] - pp), Y(pp)); }
    if (f.s.length > 1) { const pp = e0.p + 20; s += arrow(X(pp - f.s[0]), Y(pp), X(pp - f.s[1]), Y(pp)); }
  }
  return s + '</svg>';
}
// Linear demand P = a - bQ with its marginal revenue MR = a - 2bQ, in real units.
function dmrSVG(f) {
  const W = 400, H = 280, L = 54, R = 16, T = 38, B = 48;
  const qmax = f.a / f.b;
  const X = q => L + (q / qmax) * (W - L - R);
  const Y = p => H - B - (p / f.a) * (H - B - T);
  let s = '<svg viewBox="0 0 ' + W + ' ' + H + '" class="sdfig wide" role="img" aria-label="Demand and marginal revenue">';
  s += '<text x="' + (W / 2) + '" y="14" text-anchor="middle" class="ft">Demand and marginal revenue</text>';
  s += '<line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(qmax) + '" y2="' + Y(0) + '" class="ax"/>';
  s += '<line x1="' + X(0) + '" y1="' + Y(0) + '" x2="' + X(0) + '" y2="' + Y(f.a) + '" class="ax"/>';
  s += '<text x="' + X(qmax) + '" y="' + (Y(0) + 36) + '" text-anchor="end" class="fl">' + esc(f.xlabel || 'Quantity') + '</text>';
  s += '<text x="' + (X(0) + 4) + '" y="' + (Y(f.a) - 6) + '" class="fl">Price ($)</text>';
  s += '<text x="' + (X(0) - 4) + '" y="' + (Y(f.a) + 4) + '" text-anchor="end" class="al">' + fmtNum(f.a) + '</text>';
  s += '<text x="' + X(qmax) + '" y="' + (Y(0) + 13) + '" text-anchor="middle" class="al">' + fmtNum(qmax) + '</text>';
  s += '<line x1="' + X(0) + '" y1="' + Y(f.a) + '" x2="' + X(qmax) + '" y2="' + Y(0) + '" class="dem"/>';
  s += '<text x="' + (X(qmax) - 4) + '" y="' + (Y(0) - 8) + '" text-anchor="end" class="cl">Demand</text>';
  s += '<line x1="' + X(0) + '" y1="' + Y(f.a) + '" x2="' + X(qmax / 2) + '" y2="' + Y(0) + '" class="mr"/>';
  s += '<text x="' + (X(qmax / 2) + 4) + '" y="' + (Y(0) - 8) + '" class="cl">MR</text>';
  (f.points || []).forEach((pt, i) => {
    s += '<line x1="' + X(0) + '" y1="' + Y(pt.p) + '" x2="' + X(pt.q) + '" y2="' + Y(pt.p) + '" class="guide"/>';
    s += '<line x1="' + X(pt.q) + '" y1="' + Y(0) + '" x2="' + X(pt.q) + '" y2="' + Y(pt.p) + '" class="guide"/>';
    s += '<circle cx="' + X(pt.q) + '" cy="' + Y(pt.p) + '" r="3.5" class="pt' + (i ? ' p1' : '') + '"/>';
    s += '<text x="' + (X(pt.q) + 7) + '" y="' + (Y(pt.p) - 6) + '" class="cl">' + esc(pt.label) + '</text>';
    s += '<text x="' + (X(0) - 4) + '" y="' + (Y(pt.p) + 4) + '" text-anchor="end" class="al">' + fmtNum(pt.p) + '</text>';
    s += '<text x="' + X(pt.q) + '" y="' + (Y(0) + (i ? 25 : 13)) + '" text-anchor="middle" class="al">' + fmtNum(pt.q) + '</text>';
  });
  if (f.mrpoint) {
    const m = f.mrpoint;
    s += '<line x1="' + X(0) + '" y1="' + Y(m.mr) + '" x2="' + X(m.q) + '" y2="' + Y(m.mr) + '" class="guide"/>';
    s += '<circle cx="' + X(m.q) + '" cy="' + Y(m.mr) + '" r="3.5" class="pt"/>';
    s += '<text x="' + (X(m.q) + 7) + '" y="' + (Y(m.mr) + 4) + '" class="cl">' + esc(m.label) + '</text>';
    s += '<text x="' + (X(0) - 4) + '" y="' + (Y(m.mr) + 4) + '" text-anchor="end" class="al">' + fmtNum(m.mr) + '</text>';
  }
  if (f.mc) {
    // constant marginal cost: a horizontal line, and the point where it meets MR
    const c = f.mc, qc = (f.a - c.value) / (2 * f.b);
    s += '<line x1="' + X(0) + '" y1="' + Y(c.value) + '" x2="' + X(qmax) + '" y2="' + Y(c.value) + '" class="mc dashed"/>';
    s += '<text x="' + (X(qmax) - 4) + '" y="' + (Y(c.value) - 5) + '" text-anchor="end" class="cl">' + esc(c.label) + '</text>';
    s += '<circle cx="' + X(qc) + '" cy="' + Y(c.value) + '" r="3.5" class="pt"/>';
    if (c.point_label) s += '<text x="' + (X(qc) + 8) + '" y="' + (Y(c.value) - 6) + '" class="cl">' + esc(c.point_label) + '</text>';
    s += '<text x="' + (X(0) - 4) + '" y="' + (Y(c.value) + 4) + '" text-anchor="end" class="al">' + fmtNum(c.value) + '</text>';
  }
  return s + '</svg>';
}

// ---- Events (delegated) ----
app.addEventListener('change', e => {
  const t = e.target;
  if (t.matches('input[type=radio][data-item]')) {
    S.answers[t.dataset.item] = Number(t.value); saveState();
    const box = t.closest('.choices');
    if (box) { box.querySelectorAll('label').forEach(l => l.classList.remove('selected')); t.closest('label').classList.add('selected'); }
    updateSide();
  } else if (t.matches('select[data-item]')) {
    S.answers[t.dataset.item] = t.value === '' ? null : Number(t.value); saveState(); updateSide();
  } else if (t.matches('input.selfchk')) {
    S.self[t.dataset.rubric] = t.checked; saveState(); refreshScore();
  }
});
app.addEventListener('input', e => {
  const t = e.target;
  if (t.matches('input.num[data-item], textarea[data-item]')) { S.answers[t.dataset.item] = t.value; saveState(); updateSide(); }
});
app.addEventListener('click', e => {
  const t = e.target;
  if (t.id === 'startbtn') start();
  else if (t.id === 'submitbtn' || t.id === 'submitbtn2') confirmSubmit();
  else if (t.id === 'retakebtn') retake();
});

// ---- Init: resume an attempt in progress, show results if submitted, else the start screen ----
function init() {
  if (S.status === 'in_progress') {
    if (S.started_at + LIMIT_MS - Date.now() <= 0) {
      S.status = 'submitted'; S.submitted_at = S.started_at + LIMIT_MS; S.auto_submitted = true; saveState();
      renderResults();
    } else renderQuiz();
  } else if (S.status === 'submitted') renderResults();
  else renderStart();
}

__CALC_JS__

init();
</script>
"""


def safe_embed(obj):
    s = json.dumps(obj, ensure_ascii=False)
    return s.replace("</script>", "<\\/script>")


def nav_html(current_slug):
    parts = []
    cls = ' class="active"' if current_slug == "index" else ""
    parts.append(f'<a href="index.html"{cls}>All modules</a>')
    for key, label, title, slug in MODULES:
        cls = ' class="active"' if slug == current_slug else ""
        parts.append(f'<a href="{slug}.html"{cls}>{label}</a>')
    # The mock midterm is unlisted: students reach it only through a link they are
    # given, so its tab appears only on the mock page itself.
    if current_slug == MOCK["slug"]:
        parts.append(f'<a href="{MOCK["slug"]}.html" class="active">Mock Midterm</a>')
    return "".join(parts)


# ---------------- write module pages ----------------
# Page order is file order, except a question may carry "order": N to move it;
# the sort is stable, so everything without "order" keeps its place.
by_mod = {m[0]: sorted((q for q in QUESTIONS if q["module"] == m[0]),
                       key=lambda q: q.get("order", 0))
          for m in MODULES}
for key, label, title, slug in MODULES:
    qs = by_mod[key]
    assert qs, f"{key} has no questions"
    data = {"module": {"key": key, "label": label, "title": title}, "questions": qs}
    page = (PAGE_TMPL
            .replace("__CSS__", CSS)
            .replace("__PAGETITLE__", f"{label} · MGMT 405 Practice")
            .replace("__SUB__", f"{label}: {title}")
            .replace("__NAV__", nav_html(slug))
            .replace("__CALC_HTML__", CALC_HTML)
            .replace("__CALC_JS__", CALC_JS)
            .replace("__DATA__", safe_embed(data)))
    assert "__DATA" + "__" not in page, f"{slug}: unresolved placeholder"
    (DOCS / f"{slug}.html").write_text(page, encoding="utf-8")

# ---------------- write index ----------------
cards, mods_meta = [], []
for key, label, title, slug in MODULES:
    qs = by_mod[key]
    n_open = sum(1 for q in qs if q["format"] == "open")
    n_mcq = len(qs) - n_open
    cards.append(
        f'<a class="card" href="{slug}.html">'
        f'<div class="mlabel">{label}</div>'
        f'<div class="mtitle">{title}</div>'
        f'<div class="mmeta">{len(qs)} questions · {n_open} open + {n_mcq} multiple choice</div>'
        f'<div class="mprog" data-slug="{slug}"></div>'
        f'</a>')
    mods_meta.append({"slug": slug, "label": label, "title": title,
                      "ids": [q["id"] for q in qs]})
index = (INDEX_TMPL
         .replace("__CSS__", CSS)
         .replace("__NAV__", nav_html("index"))
         .replace("__CARDS__", "".join(cards))
         .replace("__DATA__", safe_embed({"modules": mods_meta})))
(DOCS / "index.html").write_text(index, encoding="utf-8")

# ---------------- write the mock midterm ----------------
mock_page = (MOCK_TMPL
             .replace("__CSS__", CSS)
             .replace("__MOCKCSS__", MOCK_CSS)
             .replace("__NAV__", nav_html(MOCK["slug"]))
             .replace("__CALC_HTML__", CALC_HTML)
             .replace("__CALC_JS__", CALC_JS)
             .replace("__DATA__", safe_embed(MOCK)))
assert "__DATA" + "__" not in mock_page and "__CALC" + "_" not in mock_page, "mock: unresolved placeholder"
(DOCS / f"{MOCK['slug']}.html").write_text(mock_page, encoding="utf-8")

# GitHub Pages: skip the Jekyll build, serve files as-is
(DOCS / ".nojekyll").write_text("", encoding="utf-8")

# ---------------- report ----------------
print(f"Wrote {len(MODULES)} module pages + index.html + {MOCK['slug']}.html to docs/")
print(f"\n{'key':6s}{'page':24s}{'open':>5s}{'mcq':>5s}{'total':>6s}")
for key, label, title, slug in MODULES:
    qs = by_mod[key]
    n_open = sum(1 for q in qs if q["format"] == "open")
    print(f"{key:6s}{slug + '.html':24s}{n_open:5d}{len(qs)-n_open:5d}{len(qs):6d}")
print(f"\nTotal: {len(QUESTIONS)} questions")
