# CLI glowup — patterns, lenses, and implementation

Read this before a look or feel pass on a CLI or developer tool. For skill targets, use
`skill-design.md` instead.

## Contents

- [What a terminal cannot do](#what-a-terminal-cannot-do)
- [Layout patterns](#layout-patterns)
- [Design lenses](#design-lenses)
- [Hero output — designing for the screenshot](#hero-output--designing-for-the-screenshot)
- [Where output travels — distribution surfaces](#where-output-travels--distribution-surfaces)
- [The feel pass — UX glowup](#the-feel-pass--ux-glowup)
- [Implementation: lift these, don't re-derive them](#implementation-lift-these-dont-re-derive-them)

## What a terminal cannot do

Read `terminal-constraints.md` before drawing any mockup. It holds the substitution
table (each unavailable GUI affordance and its terminal-native replacement), the ANSI
attribute inventory, glyph safety tiers, named light-theme failure cases, and the three
degradation environments.

The consequence that gates this workflow: **every element in a Proposed After must name
its concrete implementation** — the exact ANSI attribute, the exact glyph, the exact
alignment mechanism. "A subtle divider" is not a design decision; "a dim `─` rule
spanning the content width" is. An element that cannot name its implementation is not
renderable, and showing it commits the user to a promise the tool cannot keep.

## Layout patterns

- **RECEIPT** — itemized lines + dashed rules + a TOTAL. For anything measurable and
  cumulative (costs, tokens, sizes, time). Right-align every number. The total is the
  hero — by weight and position, not by size: when several line items invite comparison,
  bars carry the magnitude and the total leads in bold. Reserve enlarged block-glyph
  digits for BADGE, where one number is the entire screen. Even in an invented concept
  mockup, the total must equal the sum of the shown line items — verify the arithmetic
  before presenting it; a receipt that doesn't add up breaks the one thing this pattern
  promises.
- **SCORECARD** — one big grade/score + a short list of contributing checks with
  pass/fail marks. For audits, linters, health checks.
- **WRAPPED** — "your week/session/year in numbers": 3–5 oversized stats with one-line
  labels. For usage tools where periodic comparison supports the user's goal.
- **BADGE** — a single stat rendered huge in a bordered card. For one-number tools.
- **RANKED TABLE** — a leaderboard where the user's own row is highlighted. For anything
  comparative.
- **STREAK/PROGRESS** — a bar or run of marks showing accumulation. For habit-shaped
  tools.
- **GROUPED LIST** — items under headers, with a status mark in the first column and one
  aligned column per fact. For inventories where entries share a repeated attribute
  (config file, host, namespace, package). Promoting that attribute to a header removes
  it from every row, which is usually the single largest saving available; a status mark
  plus a status word keeps the scan possible without color. Put the count summary at the
  top, not the bottom — the reader wants the verdict before the enumeration.

Treat these as candidates, not required templates. A clearer table, short list, or plain
sentence is often better than a branded layout. Match the information and task before
selecting a pattern.

## Design lenses

- **Prioritize the task.** Make the information needed for the next decision easiest to
  find. When the user chose shareability, target ~24 rows × 60 columns and treat 30 rows
  as the hard cap — past that a screenshot needs scrolling. Otherwise let the task
  determine the size.
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
  which can render as dither; test CJK content with `wcwidth` and emoji with `string-width`.
- **Siblings share one system.** If the tool has multiple views (a main view and a
  picker, say), style them as one family.
- **Alignment is the aesthetic.** Right-aligned numbers, consistent column edges,
  box-drawing characters (`─ │ ┌ ┐ └ ┘`) over ASCII dashes. One outer frame maximum;
  nested boxes read as clip-art.
- **Color: one accent + neutrals + semantic states.** ANSI 16/256 only. The accent
  carries brand and interactive affordances. Semantic states are a separate category
  that predates GUI brand palettes — test runners and linters have used green, yellow,
  and red as *meaning* for decades, and readers do not parse them as extra accents. The
  constraint is that a state color never appears decoratively: if a color is not
  reporting a state, it is not that color. Reserve red for failure, so a normal run
  never looks like an error. Must survive BOTH dark and light terminals — bright cyan on
  Solarized Light and default light macOS Terminal is a known failure case, so verify on
  a light theme, not just on white. Design so the hierarchy still holds with color
  stripped entirely: position, bars, alignment, whitespace, and caps carry it, and color
  only enhances. Run the target with `NO_COLOR=1` and read it — if the structure
  collapses, the design was leaning on color. Never encode meaning in color alone (add a
  mark: ✓ ✗ ▲). Bold is a color. Dim is a color.
- **Match the voice.** Use emoji, warmth, and celebration only when they fit the tool and
  the moment. Incident response, destructive operations, and routine output usually
  benefit from restraint.
- **Keep attribution optional.** Add an install command or source line only when the
  user chose a shareable artifact and the target product wants attribution. Never add
  promotional copy to another tool by default. One carve-out: when the user selects
  Share, glowup may sign the card frame it draws itself (title, border, footer). The
  captured output inside that frame stays exactly what the target produced.
- **Whitespace is a feature.** One blank line above and below the frame; breathing room
  often beats density, but do not make routine output longer without a reason.

## Hero output — designing for the screenshot

For build-in-public tools, the primary marketing asset is a screenshot of the output,
posted by a user. That makes shareability a design requirement on exactly one screen —
not a license to decorate the whole tool.

Identify the **hero output**: the single screen someone would screenshot to show another
person. Usually the results summary, the before/after, or the final receipt. Design that
screen to a higher standard than the rest, against these criteria:

- **Self-explanatory to a stranger.** It must work with no README and no memory of the
  command that produced it. The framing line names the problem, the frequency, and the
  stakes. `~19.9k tokens total` is a measurement; `19.9k tokens loaded every session
  before your first word` is an argument. Text is the native material here — a full
  sentence costs nothing in layout, so when terseness and context conflict on the hero
  screen, context wins. Compromise available: terse panel label plus a full-sentence
  footer.
- **One number carries the story.** Viral screenshots have a headline stat — the delta,
  the saving, the count. Make it the boldest thing on screen and let the rest support it.
  Ten numbers of equal weight is a report; one number with receipts underneath is a post.
- **Crops cleanly.** Target ~24 rows × 60 columns, 30 rows hard cap, so it captures
  without scrolling; visually bounded top and bottom so a lazy crop still looks deliberate.
  Screenshots overwhelmingly show dark themes, so compose dark-first — while still
  passing the light-theme gate for actual use.
- **One flourish is allowed here.** A single mark, a blunt label (`DEAD WEIGHT`), or an
  earned result line is what makes someone want to share it. This is the one screen where
  restraint relaxes by exactly one notch. The contrast with quiet routine output is what
  makes it land. Mind the width: `⚡` is double-width, so it belongs on an unpadded
  headline, never inside a frame or aligned column — `▸` and `✦` are narrow alternatives.
- **Signature stays consented.** A tool naming itself in its own hero output turns every
  share into distribution, and that is legitimate when the user owns the tool and asked
  for a shareable artifact. It is not a default: see "Keep attribution optional" above.
  Never add an install line or promotional copy to someone else's tool.

The tension to manage: virality pulls loud, craft pulls quiet. Resolve it per element and
deliberately. Never let the tidier option win by default on the hero screen, and never let
the louder option leak into routine output.

## Where output travels — distribution surfaces

The screenshot is pull-based: a user chooses to share it, rarely. Most of a tool's output
reaches strangers without anyone choosing — and those surfaces fire far more often. During
Capture, inventory where this tool's output lands in front of people who never installed
it, because the highest-frequency surface is the real hero output, whatever the
interactive summary looks like:

- **CI logs.** Every push, read by the whole team at the worst moment — the build failed
  and they're hunting. Non-TTY rules apply in full (plain, no ANSI unless the CI supports
  it, greppable line prefixes), and the reader's question is always "was it this tool, and
  what do I do." A summary line that answers both in one glance is the best first
  impression a teammate ever gets of the tool.
- **PR surfaces.** A tool or skill that posts comments or opens PRs is publishing to every
  reviewer on the thread — the highest-leverage distribution surface a dev tool can have,
  and the easiest to get banned from. Two rules govern it. *Speak on signal:* comment or
  annotate when there is a finding; stay silent on pass. A rare, correct comment gets
  screenshotted; routine LGTMs train reviewers to ignore the bot, then to remove it.
  *The PR body is a hero output:* title states the change in the repo's own convention,
  body shows evidence (what was found, what changed, how it's verified — a test beats an
  assertion), and it reads self-explanatory to a reviewer who has never heard of the tool.
- **Errors.** The most-traveled output any tool produces — pasted into issues, chat, and
  LLM conversations, always stripped of context. "Errors are directions" (feel pass) is
  also distribution: an error that names the problem and the fix represents the tool well
  in places its maintainer will never see; one that doesn't is a complaint about the tool
  filed in someone else's tracker.
- **Committed and linkable artifacts.** Reports, badges, and HTML pages a tool generates
  are its most durable public surface — they persist in repos and travel as links. Hold
  them to hero-output criteria (self-explanatory to a stranger, one number carries the
  story) and to their own material's rules: an HTML report is not a terminal capture, so
  hierarchy comes from real typography, and it must be self-contained — no external
  scripts or fonts that rot or phone home.
- **Agents.** Output is read by coding agents that summarize it to their humans and
  recommend tools to them. Structured, plainly-worded output with stated units and
  actionable errors is what an agent can quote and act on; `--json` is what it can build
  on. Designing for the agent reader is distribution to every human that agent advises.

The governing rule across all of these: **never tax the surface.** Attribution,
install hints, and promotional lines belong only where "Keep attribution optional"
already allows them — on artifacts the user chose to share. On push surfaces (CI, PR
comments, errors) they convert goodwill into resentment at exactly the rate the surface
fires. What earns distribution there is precision, not signage.

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
  Graduate the confirmation to the stakes: `y/N` for routine destructive actions,
  type-the-resource-name for irreversible ones. Every prompt has a flag twin —
  interactive is the on-ramp, flags are the highway. If stdin is not a TTY, fail fast
  and name the flag to use instead of hanging on a prompt nobody can answer.
- **Status is honest.** Long operations show progress; instant ones stay silent. No
  spinner theater on a 40ms task. Timing rules of thumb (Nielsen's response-time limits,
  ported): under ~100 ms say nothing, under ~1 s no spinner needed, past ~1 s a spinner
  naming the verb, past ~10 s real progress — count, bar, or ETA. When it finishes, say
  what happened, not just that it finished.
- **Interruption is a designed state.** Ctrl-C, errors, resize, and exit leave the
  user's data and terminal usable. Full-screen interfaces restore cursor visibility,
  echo, and input mode on every exit path.
- **Empty and success states explain the outcome.** Make nothing-to-fix feel intentional,
  not broken. State what was checked, what the result means, and whether there is a next
  action. Calibrate celebration to the stakes and the tool's voice.
- **Claims state their true unit.** Per-session, per-prompt, per-run — the copy's meter
  must match the mechanic (skill listings load per session; "per prompt" invites the
  correction, "burned" claims full price for cached tokens). Before any number ships in
  output or README, ask: is this the unit the system actually charges in?
- **Help never lies.** A feel pass that changes behavior updates every surface that
  describes it in the same change: `--help` text, README examples, shell completions,
  man pages. Stale help is worse than no help — it teaches the old interface with the
  new one's confidence, and it burns both readers: the person follows an example that
  no longer works, and the agent asserts flags that no longer exist. Verify by rerunning
  `--help` and every changed example after the edit, not by remembering to.
- **Names follow convention.** Consistent verbs (list/add/remove), conventional flags
  (`--json`, `-q`, `--no-color`). Clever aliases are a tax on every new user. Pick one
  command grammar — noun-verb (`gh pr create`) or verb-noun — and never mix them. Respect
  the reserved short flags (`-h`, `-v`, `-q`, `-o`) and pair short with long, since long
  forms self-document in scripts. Past the first positional argument, prefer named flags:
  `deploy prod app-3 true --skip 2` is unreadable where
  `deploy app-3 --env prod --force --retries 2` reorders freely and says what it means.
- **The bar:** a stranger reaches their first success in under a minute without anyone
  explaining anything. Time it for real; don't assume.

The look pass makes the interface clear. The feel pass makes it worth returning to.

Several of these checks are also growth mechanics wearing UX names, and it is honest to
treat them that way: the under-a-minute bar is an activation metric, the empty and
success states are onboarding destinations, and "end with a door" is the step ladder
that turns a first run into a habit. Growth design is a legitimate part of UX — the
craft of getting a user to the tool's first proof of value, borrowed from onboarding
and first-run practice on the web. The gate that keeps it legitimate in a terminal:
every mechanism must serve the user's success first, with distribution as the byproduct.
A designed aha moment, a next-step door, a share-worthy hero screen — yes. Nags,
phone-home telemetry, unsolicited signatures, or friction added to force a funnel —
never. If a growth mechanism would survive being explained out loud to the user, it
belongs; if it depends on them not noticing, it doesn't.

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
  will shear columns. `wcwidth` measures CJK correctly but misjudges many modern emoji
  (ZWJ sequences, skin-tone modifiers); use `string-width` for emoji-heavy content.
