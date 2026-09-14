"""Build the MGMT 405 practice site.

Reads src/practice_questions.py + src/practice_mcqs.py, validates every
question, and writes one page per module to docs/ plus a docs/index.html
overview. GitHub Pages serves the docs/ folder, so each module gets a stable
URL the course calendar can link to directly, e.g. .../module-4-part-1.html

Do not edit docs/*.html by hand -- edit the sources and rerun this script.
"""
import json, sys, pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from practice_questions import QUESTIONS, MODULES
from practice_mcqs import ADDITIONAL_MCQS

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
    # Each page carries one rounding note at the top, so no question repeats it
    for field in ("stem", "ask"):
        low = q[field].lower()
        assert "decimal place" not in low and "round to" not in low, \
            f"{q['id']} repeats the rounding instruction in {field}"

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
  <div class="note">Please round all numbers to one decimal place (e.g., 43.6791 &rarr; 43.7).</div>
  <div id="main"></div>
</main>

<button class="calc-toggle" id="calctoggle">🖩 Calculator</button>
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
</div>

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

// ---- Calculator ----
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
});

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
    return "".join(parts)


# ---------------- write module pages ----------------
by_mod = {m[0]: [q for q in QUESTIONS if q["module"] == m[0]] for m in MODULES}
for key, label, title, slug in MODULES:
    qs = by_mod[key]
    assert qs, f"{key} has no questions"
    data = {"module": {"key": key, "label": label, "title": title}, "questions": qs}
    page = (PAGE_TMPL
            .replace("__CSS__", CSS)
            .replace("__PAGETITLE__", f"{label} · MGMT 405 Practice")
            .replace("__SUB__", f"{label}: {title}")
            .replace("__NAV__", nav_html(slug))
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

# GitHub Pages: skip the Jekyll build, serve files as-is
(DOCS / ".nojekyll").write_text("", encoding="utf-8")

# ---------------- report ----------------
print(f"Wrote {len(MODULES)} module pages + index.html to docs/")
print(f"\n{'key':6s}{'page':24s}{'open':>5s}{'mcq':>5s}{'total':>6s}")
for key, label, title, slug in MODULES:
    qs = by_mod[key]
    n_open = sum(1 for q in qs if q["format"] == "open")
    print(f"{key:6s}{slug + '.html':24s}{n_open:5d}{len(qs)-n_open:5d}{len(qs):6d}")
print(f"\nTotal: {len(QUESTIONS)} questions")
