---
name: glowup
description: Make a CLI's output screenshot-worthy and its experience worth a second run. Two passes — look (restyle into receipt/scorecard/wrapped/badge/table layouts, shown as side-by-side previews with the tool's real data before choosing) and feel (CLI usability heuristics — first-run, errors as directions, designed empty states, honest status). Never breaks machine use (--json, pipes, exit codes survive). Always produces a before/after pair. Use when asked to "glowup my CLI", "make my CLI cute", "make this shareable", "make it screenshot-worthy", "improve my CLI's UX", "audit my CLI's usability", or when a user is about to launch a CLI with printf-debug output.
---

# glowup — make CLI output worth screenshotting

People don't share tools. They share **screenshots of tools showing their own numbers**.
A CLI goes viral when one screen of its output is worth posting: neofetch rigs, ccusage
cost tables, wrapped-style summaries, context-receipt receipts. This skill restyles a
CLI's output into that screen — without breaking a single pipe.

## Process

1. **Run the tool first.** Capture the real current output (the "before"). Never restyle
   from imagination.
2. **Find the shareable unit.** The one screen a user would post. It must contain THEIR
   result — their total, their score, their rank, their streak. People share mirrors,
   not ads. If the output has no personal number in it, find one or say so; no layout
   can rescue output that isn't about the user.
3. **Show options, don't decree.** Mock the 2–3 best-fitting layout patterns using the
   tool's REAL captured data (never lorem numbers) and present them side by side for the
   user to choose — in Claude Code, use AskUserQuestion with a `preview` per option, which
   renders each mockup in a monospace box. This is the chef's-kiss moment: seeing your own
   data as a receipt vs a scorecard vs wrapped, then picking. Where tone matters (empty
   states, celebrations, hints), offer the same screen in 2–3 registers too — dry, warm,
   sparkle — same data, different voice; the user picks the register once and it governs
   the whole tool. Never blend patterns; blends read as clutter.
4. **Restyle to the chosen pattern.** Apply the taste rules. Modify only presentation
   code; logic untouched.
5. **Verify both audiences — and only trust a real terminal for the human one.** ANSI
   output cannot be judged from piped/captured text; ask the user to run it in their
   actual terminal and screenshot it back, then iterate on what they SEE. Have them PIN
   the version (`npx tool@x.y.z`) — npx serves stale cached builds and you will debug a
   ghost. Then confirm `--json`, piped output (`| cat`), and exit codes are byte-identical.
   Coach the screenshot itself: terminal wide enough that no line wraps, crop starting at
   the money line (not the shell prompt/install noise), and frame the full story arc
   (graph + celebration card) in one shot.
6. **Deliver the before/after pair** side by side. The pair is itself the launch asset —
   "I ran /glowup on my CLI" is a before/after post, the most shareable genre there is.

## Layout patterns

- **RECEIPT** — itemized lines + dashed rules + a TOTAL. For anything measurable and
  cumulative (costs, tokens, sizes, time). Right-align every number. The total is the
  hero. (Worked example: `npx context-receipt`.)
- **SCORECARD** — one big grade/score + a short list of contributing checks with
  pass/fail marks. For audits, linters, health checks.
- **WRAPPED** — "your week/session/year in numbers": 3–5 oversized stats with one-line
  labels. For usage tools. Invites comparison, which invites posting.
- **BADGE** — a single stat rendered huge in a bordered card. For one-number tools.
- **RANKED TABLE** — a leaderboard where the user's own row is highlighted. For anything
  comparative.
- **STREAK/PROGRESS** — a bar or run of marks showing accumulation. For habit-shaped
  tools.

## Taste rules (non-negotiable)

- **One-screen rule.** The shareable unit fits ~24 rows × ~60 columns — a phone
  screenshot and a tweet crop. Detail can scroll below it; the money shot cannot.
- **The number is the hero — give it a denominator and a bar.** Bold alone is not a
  moment. "24.9k tokens" is inert; "▓▓░░░░ 12% of a 200k window" is a screenshot. If a
  number has a meaningful whole, show the share visually (▓░ bars need no color and
  can't break column math). Lists become shapes; shapes get posted.
- **Promote, don't demote.** Hierarchy built by dimming most of the screen reads as
  washed-out, not organized. Body text stays at full brightness; dim is for fine print
  only (footer, disclaimers, explanations); accent/bold lift the one or two heroes.
  (Field lesson: a receipt with dimmed headers, metadata, and notes looked WORSE than
  its unstyled predecessor.)
- **End with a door, not a wall.** Every screen closes with a next action or a declared
  win — and on a TTY, the strongest close is an *offered* action ("trim these now?
  [y/N]", numbered options) that launches the next step, picker-style. A report that
  just stops is a cul-de-sac; the user's words from the field: "there's no direction
  out of it." Piped output stays static — doors are for humans.
- **Solid fills only: █, never ▓▒░ for bars.** Shade glyphs render as checkerboard
  dither in many terminal fonts and read as broken output, not data. This is the #1
  cause of "why does my chart look ugly" — verified on a real screenshot, twice.
- **Siblings share one system.** If the tool has multiple views (a main view and a
  picker, say), style them as one family. A rich view next to a plain one makes the
  plain one read as broken — users compare apples to oranges and blame the tool.
- **Alignment is the aesthetic.** Right-aligned numbers, consistent column edges,
  box-drawing characters (`─ │ ┌ ┐ └ ┘`) over ASCII dashes. One outer frame maximum;
  nested boxes read as clip-art.
- **Color: one accent + neutrals.** ANSI 16/256 only. Must survive BOTH dark and light
  terminals — test the accent on white. Never encode meaning in color alone (add a
  mark: ✓ ✗ ▲). Bold is a color. Dim is a color.
- **Emoji budget: two.** As markers, never as decoration rows.
- **Self-attribution footer.** Screenshots travel without links, so the pixels carry the
  citation: one dim line at the bottom with the install command (`npx toolname`). Quieter
  than the content, always present. This is how the screenshot recruits.
- **Whitespace is a feature.** One blank line above and below the frame; breathing room
  beats density in screenshots.

## Never break the machine path

- ANSI styling ONLY when `stdout` is a TTY (`process.stdout.isTTY` / `sys.stdout.isatty()`).
  Piped output stays plain.
- `--json` output, exit codes, and stderr semantics must be byte-identical before/after.
  Cute is a rendering layer, never a behavior change.
- Respect `--no-color` and the `NO_COLOR` env var.
- Errors get designed too: one line of what failed + one line of what to run next. No
  stack vomit. (Agents read and follow error text — an actionable error is agent UX.)

## The feel pass — UX glowup (optional second pass)

When asked to improve the CLI's UX (not just its looks), run classic usability heuristics
adapted for terminals. Audit against these, fix what fails, report as a checklist:

- **First run teaches.** Bare `toolname` with no args does something useful or shows a
  guided start — never a usage-error dump. `--help` leads with 2–3 real example commands,
  not synopsis grammar (recognition over recall).
- **Errors are directions.** One line: what failed. One line: what to run next. Meaningful
  exit codes. Agents literally follow error text, so an actionable error is UX for both
  audiences at once.
- **Defaults carry the common case.** Zero flags for the 80% path. Destructive actions get
  a confirm or `--yes`, and ideally a dry-run or undo (reversibility beats warnings).
- **Status is honest.** Long operations show progress; instant ones stay silent. No
  spinner theater on a 40ms task.
- **Empty and success states get the FULL celebration treatment.** Not a polite line —
  a designed congratulatory moment (card, color, the number they earned). The author's
  bar, verbatim from the field: "If there is an empty state, we need to make that empty
  state exciting. Congratulatory." Never fall back to an undesigned view when there's
  nothing to recommend; nothing-to-fix is the product working, so it gets the product's
  best screen. (Found in the wild twice: a cleanup tool whose post-cleanup view looked
  broken precisely because the cleanup worked.)
- **Claims state their true unit.** Per-session, per-prompt, per-run — the copy's meter
  must match the mechanic (skill listings load per session; "per prompt" invites the
  correction, "burned" claims full price for cached tokens). Before any number ships in
  output or README, ask: is this the unit the system actually charges in?
- **Names follow convention.** Consistent verbs (list/add/remove), conventional flags
  (`--json`, `-q`, `--no-color`). Clever aliases are a tax on every new user.
- **The bar:** a stranger reaches their first success in under a minute without anyone
  explaining anything. Time it for real; don't assume.

Look pass makes them screenshot it. Feel pass makes them run it twice.

## When NOT to glow up

Skip tools whose output is never seen by humans: agent-only utilities, CI-only checks,
anything whose consumers parse rather than read. Cute output that nobody screenshots is
just bytes; say so and stop, don't decorate for an empty room.

## Implementation: lift these, don't re-derive them

Prefer raw ANSI over adding chalk/gradient dependencies to someone's zero-dep CLI.
Start every glowup from this helper block (JavaScript; translate idiomatically for
other languages):

```js
// TTY-only styling; respects NO_COLOR and --no-color; --color forces (for capture).
const paint = (process.stdout.isTTY || process.argv.includes("--color")) &&
  !("NO_COLOR" in process.env) && !process.argv.includes("--no-color");
const styled = (code, t) => (paint ? `\x1b[${code}m${t}\x1b[0m` : t);
const bold = (t) => styled("1", t);
const dim = (t) => styled("2", t);
const accent = (t) => styled("1;36", t);   // one accent; 36=cyan survives dark+light
const warn = (t) => styled("33", t);

// ANSI-safe width: measure the visible string, never the escaped one.
const visibleLength = (t) => t.replace(/\x1b\[[0-9;]*m/g, "").length;
const padTo = (t, w) => t + " ".repeat(Math.max(0, w - visibleLength(t)));
```

The safest pattern of all: build each line as PLAIN text with ordinary `padEnd`, then
style the whole padded line (`console.log(dim(paddedLine))`). Whole-line styling means
ANSI codes never enter the width math at all — `visibleLength` is for the cases where
you must mix styles within one line.

- Box-drawing width: stick to single-width glyphs; emoji and CJK are double-width and
  will shear columns (the `wcwidth` package measures them correctly if you must).
- A real worked before/after — actual outputs plus the exact code change that produced
  them — is in `references/example.md`. Pattern-match against it instead of inventing.
- The design canon — Nielsen/Gestalt principles translated to terminals, plus a table of
  best-in-class CLIs (gh, stripe, cargo, fzf, charm, ccusage…) and what to steal from
  each — is in `references/canon.md`. Read it before the look pass; hold the target tool
  to its genre's best exemplar, not a generic standard.
