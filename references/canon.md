# Canon — UX principles and best-in-class CLIs to steal from

## The thesis

Applying principles that already exist to a surface that was overlooked. Not reinventing
the wheel — the unique thing added is the connection.

Terminal experience went undesigned for decades because designer-developers were rare.
Now AI has made everyone a builder, and the terminal is the fastest-growing UI surface
with the least design attention on it. The move: take what product teams already know —
UX, UI, activation, retention — and apply it to developers in their own UI.

## The audience — weird and exacting, at the same time

Developers want to feel something. They are not a boring audience — if anything they're
weirder than most (the neofetch rigs, the ASCII art, the terminal theming subculture,
the entire Charm phenomenon exist because of it). AND they are the most oversell-hostile
audience alive: every number gets audited, every claim gets a correction reply, "burned"
gets fact-checked to "loaded" within the hour.

Design consequence, and the skill's core tension: **emotion in the pixels, precision in
the copy.** The celebration card can sparkle; the number on it must be airtight. Delight
and accuracy aren't a trade-off here — delight without accuracy reads as marketing, and
this audience treats marketing as a bug.

And celebration is credible only when it's earned. It comes from a place of accuracy and
honesty, then lands warm when the moment is real — the model is the reviewer with
nothing to flag who says so plainly: "Hey, I didn't have any notes. You did a great
job." Praise from a system that never inflates is the only praise this audience
believes; that's the entire value of the ✨. Dose it to the user's own tone and the
tool's register — an incident-response CLI earns trust dry, a stats tool can sparkle —
but the vibe is the constant: honest first, warm when earned.

## Prior art — this is curation, not invention

The practitioners already wrote it down; hold every glowup to their consensus:
- **[clig.dev](https://clig.dev/)** (Prasad, Firshman, Tashian, Parish) — the field's
  codified guidelines: human-first, composable, discoverable, conversational.
- **[Primer CLI](https://primer.style/design/native/cli/)** — GitHub's actual design
  system for `gh`: reduce cognitive load (their accessibility frame), predictability via
  parallel commands, optimize the common workflow, brand that survives in a terminal.
- **[12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)**
  (Jeff Dickey, Heroku) — help docs matter more than in web apps; no table borders;
  prefer flags to arguments; behave differently when piped.
- **[Charm](https://charm.land/)** — the taste ceiling; "make people feel something."
- **Jakob Nielsen's heuristics** — the upstream source most of the above descend from;
  translated to the terminal in the principles section below.
- **[Evil Martians on progress displays](https://evilmartians.com/chronicles/cli-ux-best-practices-3-patterns-for-improving-progress-displays)** —
  the three progress patterns and when each applies: spinner (unknown duration),
  X-of-Y (countable work), progress bar (measurable fraction). Choosing by determinacy
  is the craft; a spinner on countable work wastes information the user wants.
- **[Warp](https://www.warp.dev/modern-terminal)** — the block model: each command's
  input + output grouped as one visual unit. Even in a plain CLI, design output as a
  discrete block with a clear start and end, not a stream that bleeds.
- **Progressive discovery** ([Relay](https://relay.sh/blog/command-line-ux-in-2020/)) —
  users arrive knowing nothing and learn the tool while solving a problem; every
  surface teaches a little more, no surface requires knowing everything.

**The five-point consensus across all of them:** (1) humans first, pipes always;
(2) reduce cognitive load — no affordances means help carries the weight; (3) defaults
carry the common case; (4) predictability through parallel structure; (5) feel is a
differentiator, not decoration.

## What the best ones share (researched 2026-07-17)

- **Human-first, machine-preserved.** clig.dev's core tenet: if humans use it primarily,
  design it for humans first — while keeping UNIX composability (pipes, exit codes)
  intact. Every great CLI serves both without compromising either.
- **They make people feel something.** Charm's stated philosophy, and the reason their
  tooling is in 25,000+ applications: aesthetics in the terminal aren't decoration,
  they're the differentiator. Emotion is why output gets screenshotted.
- **Known patterns over novelty.** clig.dev: follow patterns that have proved to work;
  discoverability and a conversational feel beat cleverness. (Their counterweight —
  the "chaos" principle — licenses deliberate innovation, not accidental inconsistency.)
- **Speed is a feature with emotional weight.** fzf, uv, starship: fast enough feels
  native; slow enough feels broken. No styling survives sluggishness.

## The growth funnel, mapped to a CLI

The funnel product teams instrument for apps exists in every CLI, uninstrumented:

- **Acquisition** = the screenshot. Shareable output is the ad (this skill's look pass).
- **Activation** = time to first success. Under a minute, no explanation needed — the
  create-next-app standard. First-run behavior is the onboarding flow.
- **Retention** = the verdict line and the reason to run it again (a number that changes,
  a state to check, a next action).
- **Referral** = the attribution footer. The screenshot travels linkless; the pixels
  carry the install command.

Audit a CLI the way a growth team audits a funnel: where do users bounce?

## Dashboard onboarding patterns, CLI-ified

Every pattern a SaaS dashboard uses to activate users has a terminal translation —
Claude Code's own plan mode (option cards, previews, checklists in a TTY) is the proof
it works. Steal the vocabulary:

| Dashboard pattern | CLI translation |
|---|---|
| Setup wizard | First-run interactive flow: few questions, smart defaults, skippable (`--yes`) |
| Onboarding checklist | `tool status`: setup completeness as ▓░ checklist ("2 of 4 configured") |
| Aha-moment engineering | The wizard's last line is the first real command to run, pre-filled |
| Guided empty state | Empty view ships a CTA, not a blank ("no projects yet — start: `tool init`") |
| Tooltips / hints | git-style `hint:` lines after relevant commands; one line, dismissible via config |
| Product tour | Numbered first-run walkthrough, or a `tour` command; never forced |
| Completion celebration | The ✓ victory line at real milestones — sparingly, or it's confetti spam |
| "What's new" modal | One dim line on first run after upgrade: "new in 0.3: X · changelog: <url>" |
| Option pickers | Choice lists with rendered previews of each option (plan-mode style; gum choose) |

Sources: [clig.dev](https://clig.dev/) · [Charm](https://charm.land/) and their
[100k post](https://charm.land/blog/100k/) · [Speakeasy on building a best-in-class
CLI](https://www.speakeasy.com/blog/how-we-built-cli)

## Named principles, translated to the terminal

- **Visibility of system status** (Nielsen 1): long ops show progress; state changes get
  confirmed ("disabled 54 skills · 3.7k off every session"). Silence only for instant ops.
- **Match the real world** (Nielsen 2): borrow metaphors people already read — receipts,
  scorecards, leaderboards, "wrapped." The metaphor does the explaining.
- **User control & freedom** (Nielsen 3): `--dry-run`, reversible actions, undo paths.
  Reversibility beats confirmation prompts.
- **Consistency & standards** (Nielsen 4): internal verb grammar + platform conventions
  (clig.dev is the codified standard: `--json`, `--quiet`, `NO_COLOR`, exit codes).
- **Recognition over recall** (Nielsen 6): help text leads with copy-pasteable examples,
  not synopsis grammar. Flags people saw once should be guessable.
- **Aesthetic & minimalist** (Nielsen 8): the one-screen rule is this with a ruler.
- **Errors as recovery** (Nielsen 9): what failed + what to run next. Rust's compiler made
  teaching-errors famous; agents make them mandatory (they follow error text literally).
- **Gestalt: proximity + alignment ARE the layout engine.** Monospace has no CSS; grouping
  by whitespace and hard column edges is all you get, so use them with discipline.
- **Progressive disclosure**: hero screen first; detail behind a flag (`--all`, `--brief`
  inverse). The screenshot is the summary; the flags are the appendix.

## Best-in-class CLIs — what to steal from each

| Tool | Steal this |
|---|---|
| **gh** (GitHub CLI) | verb-noun grammar, `--json` on everything, help with real examples |
| **stripe** | errors that include the fix and a docs link; `stripe listen` live feedback |
| **cargo / rustc** | the teaching error message: what broke, why, what to type next |
| **create-next-app** | first-run wizard: sensible defaults, few questions, fast to success |
| **fzf** | speed as a feature; interaction so fast it feels native |
| **bat / eza** | the drop-in glowup genre: same command, strictly better output |
| **httpie** | human-formatted output by default, machine format on request |
| **starship / neofetch** | output as identity — people screenshot their own setup |
| **charm (gum, glow)** | the taste ceiling for terminal visuals; restraint + one palette |
| **ollama / uv** | progress bars that inform (size, speed, ETA) without decorating |
| **ccusage** | the numbers-people-compare genre: personal stats in a shareable table |

Use the table as a pattern-match: identify which genre the target tool belongs to, then
hold it to that genre's best exemplar, not to a generic standard.

## Cross-surface imports — what CLI people haven't looked at

Principles proven on other surfaces that terminal design has mostly ignored:

- **Game "juice"** (game feel literature): feedback amplification makes actions feel
  significant — the reason a ✓ victory line works. The same literature warns juice has a
  dose curve: comparative studies find "juicy" beats "dry" for engagement only up to a
  point. Terminal translation: amplify *milestones* (first success, cleanup complete),
  never routine output.
- **Microinteractions** (Saffer): every user action gets an acknowledgment, however
  small — a disable prints what changed, a config write confirms where. Silence after
  an action is the terminal's most common microinteraction failure.
- **Motion discipline**: determinate beats indeterminate (X-of-Y beats spinner when work
  is countable — the skeleton-screen lesson from web); spinner cadence is the terminal's
  only easing curve, so respect it — one spinner per screen, never nested.
- **Editorial layout**: the receipt, the scorecard, the box score are *print genres*
  with a century of reader training behind them. Borrowing a genre borrows its
  readability for free — that's why the layout patterns in this skill are named after
  artifacts, not abstractions.
- **Accessibility as a hard floor**: WCAG thinking applies — dim text on dark themes is
  a contrast decision, not just a style one; meaning never rides on color alone; honor
  NO_COLOR. The terminal's accessibility story is decades behind the web's; imports
  here are cheap and differentiating.
- **Sound**: the terminal bell exists; almost always the wrong import. Named so nobody
  rediscovers it enthusiastically.

## Architecture lesson from the 107k-star neighbor

`ui-ux-pro-max` (107k★, web UI's design-intelligence skill) scales not through prose but
through **data**: 84 styles, 192 palettes, 161 reasoning rules as searchable databases
with a generator on top, plus anti-patterns and pre-delivery checklists. glowup's v2
direction when this document outgrows prose: layout patterns, terminal-safe palettes,
and per-genre reasoning rules as structured data a search can rank — "generate a design
system for your CLI" as the flagship, with **tone as a data dimension** (patterns and copy
templates tagged dry/warm/sparkle; the generator asks the register question once and emits
everything in that voice). For v1, prose curation is the right size.
