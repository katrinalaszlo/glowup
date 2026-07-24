# Terminal constraints — the material

Read this before drawing any mockup. A terminal is a character grid you do not control:
the user picks the font, the size, the theme, the window width, and whether color exists
at all. Nothing here is a picture. Everything is text plus a small set of escape codes,
interpreted by someone else's configuration.

Design with the right-hand column below directly. Do not sketch the GUI version and
translate — that is how unrenderable mockups get made.

## Contents

- [What a terminal cannot do](#what-a-terminal-cannot-do)
- [Hierarchy without font sizes](#hierarchy-without-font-sizes)
- [ANSI attribute inventory](#ansi-attribute-inventory)
- [Glyph safety tiers](#glyph-safety-tiers)
- [Known theme failure cases](#known-theme-failure-cases)
- [The three degradation environments](#the-three-degradation-environments)

## What a terminal cannot do

| GUI affordance | Why it's unavailable | Terminal-native substitute |
| --- | --- | --- |
| Font sizes / type scale | One monospace font, one size, chosen by the user | Blank lines, indentation, bold, SPACED CAPS, `▌` block prefixes; bar length for magnitude; digits built from `█` across 5 rows when one number must dominate |
| Font families, italics, letter-spacing | User's terminal config | Weight (bold/dim) and case are the whole type system |
| Logos / images | Character grid only | Wordmark in text, optionally one narrow glyph (`▸ ✦`) as a mark — `⚡` is double-width, so keep it on unpadded free-text lines only. Branding otherwise belongs to an exported image wrapped around a real capture |
| Precise colors / brand hex | ANSI slots are theme-mapped by the user | Choose *slots*, not colors: accent slot + neutrals + semantic green/yellow/red |
| Padding in pixels | Grid cells only | Blank lines (vertical) and spaces (horizontal), in whole cells |
| Cards, shadows, rounded borders | No 2D drawing | Box-drawing lines, or better: indentation plus a dim rule. Frames are expensive; one outer frame maximum |
| Reflowing columns | Fixed grid, unknown window width | Design to a stated width (80 default, 100 for developer audiences); pad-to-column alignment |
| Hover states / tooltips | No pointer | Everything visible must be self-explanatory; help lives in `--help` and inline hints |
| Buttons / click targets | Text in, text out | Named commands and flags; TUIs get keybinding hints in a dim footer |
| Animation / transitions | Line-oriented output | Spinners and progress bars for duration only, never decoration; must clear cleanly |
| Charts / data viz | No canvas | `█` bar runs with `▏▎▍▌▋▊▉` fractions, sparklines (`▁▂▃▅▇`), aligned numeric columns |
| Guaranteed rendering | User's font may lack glyphs | Stay in well-supported ranges; ASCII fallbacks for exotic glyphs |

Two consequences worth stating plainly. **Magnitude is the job bars do**, because size is
the one variable the medium removes — a receipt with several values to compare wants bars,
not a single enlarged total. And **a rendered share image is not a terminal design**: it
may frame a real capture, but every claim it makes about the tool's output must hold in
the tool's actual output.

## Hierarchy without font sizes

One font, one size. Hierarchy comes from four levers, strongest first:

1. **Space** — blank lines and indentation. A blank line above a section does more than
   any color. Indentation encodes containment; use consistent two-space steps.
2. **Weight and dimming** — bold for the few things that must be read, dim for metadata
   and chrome. Most of the screen stays default weight.
3. **Case and glyphs** — CAPS or `▌` prefixes as headers, sparingly. Box-drawing builds
   structure; prefer light-weight lines and never mix light and heavy in one frame.
4. **Color** — last, because it is the lever the user's theme can take away or invert.

If the design reads correctly with color stripped, the hierarchy is sound. If it does
not, fix levers 1–3 before touching 4.

## ANSI attribute inventory

| Attribute | Code | Reliability | Use for |
| --- | --- | --- | --- |
| Bold | `1` | Universal | The few must-read items |
| Dim | `2` | Very good | Metadata, chrome, rules, counts |
| Italic | `3` | Spotty | Avoid as a load-bearing signal |
| Underline | `4` | Good | Links (with OSC 8 where supported); rarely else |
| Inverse | `7` | Universal | Selection/cursor in TUIs; heavy, use rarely |
| 16-color foreground | `30–37`, `90–97` | Universal | The palette — design in these |
| 256-color | `38;5;n` | Very good | Only with a 16-color fallback |
| Truecolor | `38;2;r;g;b` | Good, not universal | Only when the design demands it, with fallback |

Strikethrough (`9`) exists. Treat blink (`5`) as forbidden.

## Glyph safety tiers

Widths below are Unicode East Asian Width (EAW), which is what determines whether a glyph
shears a column. Verify with `wcwidth` / `string-width` rather than by eye.

- **Genuinely narrow (EAW=Neutral) — safe anywhere:** ASCII, `✓ ✗ ⚠ ▸ ✦`, braille
  spinners (`⠋⠙⠹`).
- **Safe in default Western configs, but EAW=Ambiguous:** light box-drawing
  (`─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼`), blocks (`█ ▌ ▐`), sub-cell blocks (`▏▎▍▌▋▊▉`), sparkline
  bars (`▁▂▃▄▅▆▇█`), and the common marks `→` and `•`. These render single-width in
  default Western terminals, so the practical guidance holds — but under a CJK
  "ambiguous = wide" configuration this entire tier doubles and every aligned column
  shears. If the audience may run CJK-wide settings, verify there.
- **Genuinely double-width (EAW=Wide) — never inside a frame or aligned column:** emoji
  and emoji-adjacent signs, including `⚡` (U+26A1). These are fine on a free-text line
  that is not padded to a column width; they are not fine anywhere the column math has
  to hold. `◆` is Ambiguous; `▸` and `✦` are Neutral, so both are safer marks.
- **Risky for other reasons:** Nerd Font glyphs (require patched fonts; only if the
  audience demonstrably has them), heavy or double box-drawing mixed with light, and
  `▓▒░`, which can render as dither — prefer solid `█` for bars.

## Known theme failure cases

Test the accent and any bright colors against these before locking:

- **Solarized (both modes) — the bright slots are not colors.** Solarized deliberately
  remaps the eight *bright* ANSI slots to grayscale base tones: bright cyan is `#93a1a1`,
  bright green `#586e75`, bright yellow `#657b83`. Against the Solarized Light background
  (`#fdf6e3`), bright cyan approaches invisibility — but the more dangerous case is bright
  green and yellow, which stay perfectly readable as *dark gray* and are simply no longer
  green or yellow. Bright yellow is literally the body-text color. So any semantic state
  carried in a bright slot silently degrades into indistinguishable gray rather than
  failing visibly. Use the non-bright slot for anything meaning-bearing: Solarized maps
  plain cyan (`36`) to real cyan, `#2aa198`.
- **macOS Terminal "Basic" (light)** — bright yellow unreadable, cyan weak.
- **One Light / GitHub Light** — bright cyan weak.
- **Muted dark palettes (Gruvbox, Nord)** — verify the accent still separates from neutrals.

If an accent fails on light themes, prefer the non-bright slot of the same hue, or shift
hierarchy weight onto bold/dim so color becomes enhancement rather than signal. Do not
hunt for a "better" hue you still do not control. This is also the second reason never to
encode meaning in color alone: a remapped slot takes the meaning with it.

## The three degradation environments

Check all three before locking:

1. **`NO_COLOR=1` or `TERM=dumb`** — all SGR stripped; hierarchy must survive on space,
   glyphs, and case alone. This falls out for free if levers 1–3 carried the design.
2. **Light theme** — accent legible on at least two common light themes.
3. **Piped (`| cat`, not a TTY)** — no color, no spinners, no cursor movement; alignment
   preserved, greppable, one record per line where the output is data.

A fourth reader shares the plain path: screen readers consume the terminal linearly, so
spinners, progress redraws, and cursor movement become repeated noise or vanish entirely.
The plain path doubles as the screen-reader path when it is append-only — each state
change is a new line, never a rewrite of an old one. If the tool renders anything in
place, verify the plain path replaces it with append-only equivalents rather than merely
stripping color.
