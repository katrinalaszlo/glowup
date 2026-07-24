#!/usr/bin/env python3
"""Build the glowup before/after card from REAL terminal text.

Both panels are literal captured characters rendered in a <pre>, so spacing is
exact by construction — no hand-placed coordinates to drift out of sync.
"""
import html
import re
import pathlib

SCRATCH = pathlib.Path(__file__).parent

# ANSI SGR -> CSS. Only the codes debloat actually emits.
COLORS = {
    "2": "dim",
    "1": "b",
    "33": "yellow",
    "32": "green",
    "31": "red",
    "36": "cyan",
    "1;36": "cyan b",
}

ANSI_RE = re.compile(r"\x1b\[([0-9;]*)m")


def ansi_to_html(text):
    """Convert ANSI SGR sequences to nested spans, preserving every character."""
    out = []
    open_spans = 0
    pos = 0
    for m in ANSI_RE.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        code = m.group(1)
        if code in ("", "0"):
            out.append("</span>" * open_spans)
            open_spans = 0
        else:
            cls = COLORS.get(code)
            if cls:
                out.append(f'<span class="{cls}">')
                open_spans += 1
        pos = m.end()
    out.append(html.escape(text[pos:]))
    out.append("</span>" * open_spans)
    return "".join(out)


# The real 2026-07-17 capture of context-receipt, plain printf, no styling.
BEFORE = """ CONTEXT RECEIPT
 claude code · vault
 2026-07-17 18:23
 ──────────────────────────────────────────────
 LOADED BEFORE YOUR PROMPT             tokens*
 claude code system prompt               ~6.8k
 CLAUDE.md (global)                       1.5k
 MEMORY.md (auto-memory index)            3.7k
 skill listing, user (20 skills)          1.8k
 ──────────────────────────────────────────────
 TOTAL                                  ~24.8k

 DEAD WEIGHT — on disk, NOT loaded
   AGENTS.md                       17.8k chars
     not read unless @imported from CLAUDE.md
 * chars÷4 estimate · reconcile with /context
 npx context-receipt"""

after_ansi = (SCRATCH / "after.ansi").read_text().strip("\n")

CSS = """
* { box-sizing: border-box; }
body {
  margin: 0; background: #0a0e14;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 1180px; height: 868px; padding: 34px 40px;
}
.head { display: flex; align-items: baseline; gap: 18px; margin-bottom: 26px; }
.mark {
  font-family: ui-sans-serif, -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-size: 34px; font-weight: 800; color: #f2f5f8; letter-spacing: -0.5px;
}
.tag { font-size: 16px; color: #8b95a1; }
.repo { margin-left: auto; font-size: 14px; color: #6e7681; }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: stretch; }
.col { display: flex; flex-direction: column; }
.lbl { font-size: 12px; letter-spacing: 1.6px; margin-bottom: 12px; text-align: center; }
.lbl.a { color: #8b95a1; }
.lbl.b { color: #39c5cf; font-weight: 700; }
.term { background: #161b22; border: 1px solid #30363d; border-radius: 9px; overflow: hidden;
        flex: 1; display: flex; flex-direction: column; }
.bar { padding: 11px 14px; border-bottom: 1px solid #21262d; display: flex; align-items: center; gap: 7px; }
.dot { width: 11px; height: 11px; border-radius: 50%; }
.cap { margin-left: auto; margin-right: auto; font-size: 11px; color: #6e7681; }
pre {
  margin: 0; padding: 16px 14px; font-size: 12.5px; line-height: 1.5;
  color: #c9d1d9; white-space: pre; overflow: visible;
}
.dim { color: #6e7681; }
.b { font-weight: 700; color: #e6edf3; }
.cyan { color: #39c5cf; }
.yellow { color: #d29922; }
.green { color: #3fb950; }
.red { color: #f85149; }
.foot { margin-top: 26px; display: flex; justify-content: center; }
.cmd {
  background: #11161d; border: 1px solid #30363d; border-radius: 9px;
  padding: 14px 30px; font-size: 15px; color: #d7dde3;
}
.cmd .p { color: #6e7681; margin-right: 10px; }
"""


def panel(caption, body_html):
    return f"""<div class="term">
  <div class="bar">
    <span class="dot" style="background:#ff5f57"></span>
    <span class="dot" style="background:#febc2e"></span>
    <span class="dot" style="background:#28c840"></span>
    <span class="cap">{caption}</span>
  </div>
  <pre>{body_html}</pre>
</div>"""


doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="head">
  <span class="mark">glowup</span>
  <span class="tag">a design skill for the terminal</span>
  <span class="repo">github.com/katrinalaszlo/glowup</span>
</div>
<div class="cols">
  <div class="col">
    <div class="lbl a">BEFORE</div>
    {panel("context-receipt · 2026-07-17", html.escape(BEFORE))}
  </div>
  <div class="col">
    <div class="lbl b">AFTER</div>
    {panel("npx debloat · real output", ansi_to_html(after_ansi))}
  </div>
</div>
<div class="foot">
  <div class="cmd"><span class="p">$</span>npx skills add katrinalaszlo/glowup -g</div>
</div>
</body></html>"""

(SCRATCH / "card.html").write_text(doc)
print("wrote card.html")
