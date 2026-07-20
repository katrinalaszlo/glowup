# CLI glowup — patterns, lenses, and implementation

Read this before a look or feel pass on a CLI or developer tool. For skill targets, use
`skill-design.md` instead.

## Contents

- [Layout patterns](#layout-patterns)
- [Design lenses](#design-lenses)
- [The feel pass — UX glowup](#the-feel-pass--ux-glowup)
- [Implementation: lift these, don't re-derive them](#implementation-lift-these-dont-re-derive-them)

## Layout patterns

- **RECEIPT** — itemized lines + dashed rules + a TOTAL. For anything measurable and
  cumulative (costs, tokens, sizes, time). Right-align every number. The total is the
  hero. (Worked example: `npx context-receipt`.)
- **SCORECARD** — one big grade/score + a short list of contributing checks with
  pass/fail marks. For audits, linters, health checks.
- **WRAPPED** — "your week/session/year in numbers": 3–5 oversized stats with one-line
  labels. For usage tools where periodic comparison supports the user's goal.
- **BADGE** — a single stat rendered huge in a bordered card. For one-number tools.
- **RANKED TABLE** — a leaderboard where the user's own row is highlighted. For anything
  comparative.
- **STREAK/PROGRESS** — a bar or run of marks showing accumulation. For habit-shaped
  tools.

Treat these as candidates, not required templates. A clearer table, short list, or plain
sentence is often better than a branded layout. Match the information and task before
selecting a pattern.

## Design lenses

- **Prioritize the task.** Make the information needed for the next decision easiest to
  find. When the user chose shareability, keep the key view near 24 rows × 60 columns;
  otherwise let the task determine the size.
- **Give numbers context.** When a value has a meaningful whole, show its denominator or
  comparison. Use single-width solid bars such as `██──────── 20%` only when they improve
  comprehension. Do not manufacture a denominator or turn every metric into a hero.
- **Promote, don't demote.** Hierarchy built by dimming most of the screen reads as
  washed-out, not organized. Body text stays at full brightness; dim is for fine print
  only (footer, disclaimers, explanations); accent/bold lift the one or two heroes.
- **End with a door, not a wall.** Every screen closes with a next action or a declared
  result. Offer an interactive action only when it is safe, relevant, and clearly
  optional. Piped and noninteractive output stays static.
- **Use robust glyphs.** Prefer single-width `█`, `─`, and plain marks. Avoid `▓▒░`,
  which can render as dither, and test any emoji or CJK content with `wcwidth`.
- **Siblings share one system.** If the tool has multiple views (a main view and a
  picker, say), style them as one family.
- **Alignment is the aesthetic.** Right-aligned numbers, consistent column edges,
  box-drawing characters (`─ │ ┌ ┐ └ ┘`) over ASCII dashes. One outer frame maximum;
  nested boxes read as clip-art.
- **Color: one accent + neutrals.** ANSI 16/256 only. Must survive BOTH dark and light
  terminals — test the accent on white. Never encode meaning in color alone (add a
  mark: ✓ ✗ ▲). Bold is a color. Dim is a color.
- **Match the voice.** Use emoji, warmth, and celebration only when they fit the tool and
  the moment. Incident response, destructive operations, and routine output usually
  benefit from restraint.
- **Keep attribution optional.** Add an install command or source line only when the
  user chose a shareable artifact and the target product wants attribution. Never add
  promotional copy to another tool by default.
- **Whitespace is a feature.** One blank line above and below the frame; breathing room
  often beats density, but do not make routine output longer without a reason.

## The feel pass — UX glowup

When asked to improve the CLI's UX (not just its looks), run classic usability heuristics
adapted for terminals. Audit against these, fix what fails, report as a checklist:

- **First run teaches.** Bare `toolname` with no args does something useful or shows a
  guided start when that fits the command. Otherwise show concise task-oriented help and
  a meaningful usage exit. `--help` leads with 2–3 real example commands, not only
  synopsis grammar (recognition over recall).
- **Errors are directions.** One line: what failed. One line: what to run next. Meaningful
  exit codes. Actionable error text helps both people and agents recover.
- **Defaults carry the common case.** Zero flags for the 80% path. Destructive actions get
  a confirm or `--yes`, and ideally a dry-run or undo (reversibility beats warnings).
- **Status is honest.** Long operations show progress; instant ones stay silent. No
  spinner theater on a 40ms task.
- **Empty and success states explain the outcome.** Make nothing-to-fix feel intentional,
  not broken. State what was checked, what the result means, and whether there is a next
  action. Calibrate celebration to the stakes and the tool's voice.
- **Claims state their true unit.** Per-session, per-prompt, per-run — the copy's meter
  must match the mechanic (skill listings load per session; "per prompt" invites the
  correction, "burned" claims full price for cached tokens). Before any number ships in
  output or README, ask: is this the unit the system actually charges in?
- **Names follow convention.** Consistent verbs (list/add/remove), conventional flags
  (`--json`, `-q`, `--no-color`). Clever aliases are a tax on every new user.
- **The bar:** a stranger reaches their first success in under a minute without anyone
  explaining anything. Time it for real; don't assume.

The look pass makes the interface clear. The feel pass makes it worth returning to.

## Implementation: lift these, don't re-derive them

Prefer raw ANSI over adding chalk/gradient dependencies to someone's zero-dep CLI.
Start every glowup from this helper block (JavaScript; translate idiomatically for
other languages):

```js
// Return from --json and every other machine format before this rendering layer.
const args = new Set(process.argv.slice(2));
const structured = args.has("--json"); // Extend for the target's other machine formats.
const forceColor = args.has("--color");
const noColorEnv = Boolean(process.env.NO_COLOR);
const colorBlocked = structured || args.has("--no-color");
// An explicit --color overrides the NO_COLOR default for this invocation.
const paint = !colorBlocked &&
  (forceColor || (!noColorEnv && Boolean(process.stdout.isTTY)));
const styled = (code, t) => (paint ? `\x1b[${code}m${t}\x1b[0m` : t);
const bold = (t) => styled("1", t);
const dim = (t) => styled("2", t);
const accent = (t) => styled("1;36", t);   // one accent; 36=cyan survives dark+light
const warn = (t) => styled("33", t);

// ANSI-safe width: measure the visible string, never the escaped one.
const visibleLength = (t) => t.replace(/\x1b\[[0-9;]*m/g, "").length;
const padTo = (t, w) => t + " ".repeat(Math.max(0, w - visibleLength(t)));
```

The safest pattern for human output: build each line as plain text with ordinary `padEnd`, then
style the whole padded line (`console.log(dim(paddedLine))`). Whole-line styling means
ANSI codes never enter the width math at all — `visibleLength` is for the cases where
you must mix styles within one line.

- Box-drawing width: stick to single-width glyphs; emoji and CJK are double-width and
  will shear columns (the `wcwidth` package measures them correctly if you must).
