---
name: glowup
description: Improve the display or interaction flow of a CLI, developer tool, or agent skill using product-design principles. For terminal tools, capture the real Before, infer or ask whether to improve the Display, Flow, or Both, show a clearly labeled Proposed After before editing, implement only after approval, then verify and optionally export the Final After without breaking machine contracts. Also improve skill discovery, instructions, safety, and validation. Use for "glowup my CLI", "improve this terminal interface", "improve this tool's UX", "glow up this skill", "audit this skill's interaction design", or a pre-launch design review.
---

# glowup — design the developer experience

CLIs and agent skills are interfaces. Their hierarchy, feedback, first run, errors,
instructions, and recovery deserve the same design attention as a web or mobile product.
Apply established product-design principles to the reader's real constraints: the person
directing the work, the agent interpreting it, and any program consuming the result.
Inspect first, ask only consequential questions, and preserve documented contracts.

## Keep the user oriented

Expose one stable five-stage journey:

`Capture → Choose → Preview → Implement & Verify → Compare & Finish`

At the start and whenever the stage changes, show a compact marker in normal conversation:

```text
Glowup 2/5 · Choose
Now: Choose what to glow up.
Next: I’ll show the Proposed After before editing.
```

Use the same names and order throughout the run. Update the marker only on a stage change,
after a meaningful wait, or when resuming from an interruption; do not narrate every tool
call. Never say implementation is underway while still previewing. If blocked, keep the
current stage visible and state what is needed to continue.

## Process

1. **Capture — name the target, readers, and layer.** Distinguish a CLI or developer tool from an
   agent skill. Identify whether each important path serves a person, an agent, a program,
   or more than one. Name whether the proposed change affects policy that guides, a
   contract that makes failure detectable, or enforcement that blocks invalid behavior.
   Do not assume that a human-readable surface and a machine contract need the same
   treatment. Infer this from the request and repository when possible; do not begin with
   an intake interview.
2. **Capture — run a fast orientation pass.** Never design from imagination, but do not front-load
   a full audit before the user chooses a focus.
   - Read only enough documentation, source, and tests to identify the entry point, common
     task, safety constraints, and existing fixtures before executing unfamiliar commands.
   - For a CLI, run one safe representative human path and capture its command, data,
     terminal dimensions, visible output, and interaction. Stop there for the opening
     decision; do not exercise every subcommand or machine path yet.
   - Keep the opening pass read-only and single-agent. Do not create fixtures, write into
     the project, spawn reviewers, or trace root causes before focus selection. If the
     representative path needs setup, use an existing fixture or ask for a screenshot or
     pasted output instead.
   - For a skill, read `SKILL.md` completely and load only the references and assets
     relevant to a concrete request. Capture how a fresh session discovers, interprets,
     executes, and validates the skill.
   - If the target command or screen cannot be inferred, or more than one plausible target
     exists in the working directory, ask a short question naming the detected candidates
     rather than improvising an open-ended one. If none exist, ask the user to point to a
     CLI, developer tool, or skill directory instead of stopping on a bare "none found." Do
     not download or install a target merely to preview it without explicit approval.
   - Obtain explicit approval before any authenticated, networked, destructive,
     production-affecting, privacy-sensitive, or potentially costly execution.
3. **Choose — choose what to glow up.** For a CLI or developer tool, make the first choice
   concrete: **Display**, **Flow**, or **Both**.
   - **Display:** improve visual hierarchy, spacing, alignment, scanability, and emphasis.
   - **Flow:** improve commands, prompts, options, feedback, recovery, and next steps.
   - **Both:** improve the presentation and the interaction as one experience.
   If the request already names one of these focuses, skip the question. Otherwise, after
   inspection, ask **What should I glow up?** with exactly those three options. Recommend
   one from the captured evidence, but do not replace the options with findings, fixes,
   issue scope, or visual directions. Reserve **Both** for the Display + Flow focus.
   Before opening the choice, put the captured evidence and recommendation in normal
   conversation. If using AskUserQuestion,
   give each option only a label and short description; do not attach a preview panel.
   Describe confirmed observations, not suspected causes. Do not promote a finding into
   an option merely because a code search suggests it; reproduce it first or label it as
   a hypothesis for the selected pass.
   For a skill target, the focus options are **discovery**, **instructions**, **safety**,
   or **validation** (the boundaries in `references/skill-design.md`). Recommend the
   highest-leverage one and ask one similarly consequential question only when it cannot
   be inferred.
4. **Preview — preview before editing.** Put the review in the conversation by default. Show the
   captured **Before** beside or immediately before a clearly labeled **Proposed After**,
   using the same command, data, and terminal dimensions.
   - **Display:** use a fenced monospace mockup for structure — and know its limit: a
     fenced block strips ANSI, so the user is judging a colorless sketch of a colored
     design. When the proposal uses color or weight as meaning — nearly every Display
     pass — do not stop at the sketch. Render the proposal in an isolated temporary
     copy and open the colored Before/After render as the approval question arrives —
     the user decides with the colors on screen, not from memory of a monochrome
     sketch. Fall back to one copy-paste command that runs the render in the user's
     own terminal only when local opening is unavailable. The user should never have
     to ask why the mockup has no color. When variants are offered, render each one
     the same way and compose the real renders into one labeled comparison image —
     Before first, then each variant labeled A, B, C — with a visible caption telling
     the user to reply with their pick in the conversation, since an image cannot be
     clicked. Open it as the variant question arrives; the conversation question
     remains the selection mechanism, and the Final After at Compare & Finish reuses
     the same rendering path. Label mockups as concepts and temporary renders as
     previews; neither is the implemented result.
   - **Renderability gate — every mockup, without exception.** Before showing a Display
     proposal, check it against `references/terminal-constraints.md` and confirm each
     element maps to a real mechanism: ANSI attribute, glyph, or column arithmetic. Font
     size, custom fonts, logos, panel fills, and pixel placement do not exist — a mockup
     using them can never be implemented, and presenting it commits the user to a promise
     the tool will not keep. State the mechanism for anything non-obvious (for example,
     "magnitude via bar length" or "hero number via 5-row block glyphs") so the user is
     approving something buildable.
   - **Receipt check.** Shown line items must sum to the stated total, percentages to
     ~100, and before − savings = after exactly. If a figure cannot be reconciled, label
     the gap in the mockup itself. A tool whose job is measurement loses trust fastest on
     arithmetic.
   - **Shareability pass — hero output only.** When the target is shared publicly and
     this screen is the one a user would screenshot, apply "Hero output" in
     `references/cli-glowup.md`: framing line legible to a stranger, one headline number,
     crops clean under ~30 rows. Attribution stays opt-in, never added to someone else's
     tool by default. If Capture found the tool's output also lands on push surfaces —
     CI logs, PR comments or bodies, generated reports — apply "Where output travels"
     from the same reference: the highest-frequency surface outranks the interactive
     screen, and push surfaces get precision, never signage.
   - **Flow:** show the current and proposed interaction as short transcripts. Use a
     recording only when timing, motion, or key sequences affect the decision.
   - **Both:** combine the static comparison with the shortest useful flow transcript.
   - **Skill target:** the preview is a before/after excerpt of the instructions being
     changed plus the expected behavior change on a representative request — what a
     fresh session would do differently. Mockups and terminal captures do not apply.
   Stack large captures instead of shrinking them; if a detail is cropped, keep the full
   capture available for context. Do not open two terminals or generate an HTML report by
   default. If the host renders the AskUserQuestion option `preview` field (single-select
   questions only where supported), it may carry the mockup; otherwise put the mockup in
   normal conversation before asking. Never rely on a preview panel the user might not
   have seen — the conversation copy is the one being approved.
   Only after the user chooses the focus, show the complete Proposed After in normal
   conversation. Then ask the user to **Apply**, **Revise the preview**, or **Change
   focus** before editing; do not combine focus selection with implementation approval.
   - **Revise loops.** Revise is repeatable, not a single retry. Keep showing updated
     previews until the user applies or stops; never treat the second proposal as final
     by default, and never start editing to escape an iteration.
   - **Offer variants when the direction is genuinely open.** If a Display change has more
     than one defensible approach, show **two or three labeled variants side by side**
     instead of one proposal and a critique loop — reacting to options is faster and more
     accurate than describing a change in the abstract. Variants must differ in
     *approach*, not polish: for a receipt, "bars carry magnitude" versus "block-glyph
     hero number" versus "plain ranked table" are variants; three spacing tweaks are not.
     Each one passes the renderability and receipt gates independently, and each gets one
     line naming its tradeoff. When the fix is determinate — an alignment bug, a contract
     violation, one obvious hierarchy error — show a single proposal; manufacturing
     alternatives wastes the user's attention.
5. **Preview — choose the change boundary.** The boundary restates the chosen focus as
   what may change: **Display** maps to a look pass, **Flow** to a feel pass, and a
   skill target is always a skill pass. Name it before showing the Proposed After so the
   preview only contains changes the boundary allows.
   - **Look pass:** change presentation only. Keep logic and all machine behavior intact.
   - **Feel pass:** improve interaction behavior such as first run, recovery, progress,
     or reversibility. Show the proposed flow and obtain explicit approval before editing.
     Preserve documented inputs, structured outputs, exit meanings, and noninteractive
     paths; add compatibility tests for any intentionally changed human-facing behavior.
   - **Skill pass:** improve triggering, instructions, progressive disclosure, judgment
     boundaries, user checkpoints, safety, or validation. Preserve the skill's stated
     purpose and any tool contracts; obtain approval before broadening its authority or
     product scope.
6. **Preview — port the reason, not the rule.** For each recommendation, name the reader, the
   protected human or system constraint, what changes in this medium, and the observable
   test. Use a heuristic only when its underlying constraint transfers.
7. **Implement & Verify — confirm orientation and capture baselines.** After the user approves the preview,
   restate the target, selected pass, change boundary, contracts that will remain
   unchanged, and the next stopping point. If the user redirects the preview, update it
   before continuing. The Capture-stage risk gate stays in force for this phase: re-obtain
   explicit approval before any authenticated, networked, destructive, production-affecting,
   privacy-sensitive, or potentially costly command, including ones run only to capture a
   baseline or verify a result. For a CLI, only now capture the relevant compatibility baselines:
   first run, help, one error, one empty or success state, piped output, structured output,
   and exit paths. Use existing tests, fixtures, temporary configuration, sandboxes, and
   dry-run modes; skip paths unrelated to the approved change.
8. **Implement & Verify — apply the smallest coherent change.** Use the relevant lenses, not every rule in
   this file. Preserve the product's established voice. Avoid decoration or instructions
   that do not help the selected goal. Keep a routine single-command glowup single-agent;
   use separate reviewers only when complexity or risk justifies the extra time.
9. **Implement & Verify — verify every affected reader.**
   - For a CLI, rerun the human path with the same command, data, and terminal dimensions.
     Compare captured machine fixtures, then confirm piped stdout and structured output
     byte for byte, documented exit codes by value, and stderr on the same channel with
     equivalent meaning unless an approved feel pass intentionally changes its wording.
     If the real result does not match the approved direction, iterate before presenting
     it as final.
   - Do not call an interactive path verified when the command reports a non-TTY,
     simulation, or fallback mode. Report the limitation and ask the user for a real
     terminal capture when it matters. If investigation disproves a preliminary finding,
     remove it from the change count and say plainly that it was not a bug; never describe
     it as fixed.
   - For a skill, validate its structure and exercise representative requests in fresh
     sessions. Compare the agent's interpretation, actions, questions, and result against
     the captured before. Self-review is evidence generation, not independent proof; use
     a clean session or separate reviewer before calling the result validated.
   - When ANSI rendering cannot be judged directly, ask the user for a terminal
     screenshot and iterate on what they see.
10. **Compare & Finish — deliver and offer next actions.** Replace the proposed preview
   with a verified **Final After** from the implemented tool. Show the same task, data,
   and terminal dimensions as the Before; list the design decisions and contract checks.
   At the end, ask **What would you like me to do before we finish? Select any that
   apply, or say done.** Use a multi-select question when the host supports it, with
   only these additive actions:
   - **Export visual** — create and immediately open a polished Before/After image or PDF.
   - **Share Before/After** — open the image and a Show and tell composer in the glowup
     community repo.
   - **Commit changes** — stage and commit only the approved product changes.
   - **Another glowup pass** — begin another Display, Flow, or skill pass.

   Do not add **Finish here**, **No export**, or other negative actions to the multi-select.
   Saying "done" or selecting nothing ends the run. If the user combines a finish phrase
   with one or more actions, complete those actions and then stop; do not ask them to
   resolve a conflict. If multi-select is unavailable, ask the user to list every desired
   action in one response. Treat the selections as a short action queue and reuse the
   verified captures and checks already produced. Do not re-audit the repository, inspect
   unrelated history or stashes, or start extra reviewers merely to finish, export, share,
   or commit. If Export and Commit are both selected, keep the export outside the target
   repository unless the user explicitly approves adding it.
   When **Export visual** or **Share Before/After** is selected, read
   `references/export-share.md` and follow it. Do not load it otherwise. Both actions work
   only from the real Before and Final After captures; never reconstruct output from memory
   or present invented terminal text as a capture. The selection authorizes creating the
   artifact and opening it locally, so do not ask again — but opening locally is never
   permission to upload or publish, and Export alone is never permission to share.
   When the tool can run locally, capture both states directly. Otherwise use a
   user-supplied screenshot or transcript for the Before and say what could not be
   reproduced. Do not add export files to the target repository without approval. Before
   sharing any artifact, review it for credentials, tokens, personal data, account
   identifiers, private endpoints, and local paths; redact sensitive content and obtain
   explicit approval for public sharing.

   End every completed CLI run with these four items in order:
   1. **Before** — the original capture.
   2. **Final After** — a fresh capture from the implemented tool, not the preview.
   3. **Changes and checks** — confirmed changes, preserved contracts, and any unverified
      paths or disproved hypotheses.
   4. **Next actions** — offer the multi-select actions above.

   End a completed skill run with the same shape: the before fixture, the after
   instructions, the fresh-session behavior comparison from verification, and next
   actions (Export visual does not apply unless a visual was produced).

   Do not finish with only raw After output and an implementation summary.

## Review-only runs

When the request is an audit or review rather than a change — "audit this skill's
interaction design", a pre-launch design review — run Capture and the relevant
checklist, then deliver ranked findings as the final artifact: for each, the file and
line, what is wrong, why it matters to its reader, and a concrete proposed fix. Do not
edit anything and skip Preview, Implement & Verify, and Compare & Finish. If the user
then asks to apply fixes, the accepted findings become the Proposed After and the run
rejoins the journey at Preview.

## Pass playbooks

Load the depth for the pass you are running, nothing else — except references the
target itself cites, which you may open to verify the citations hold:

- **Look or feel pass (CLI or developer tool):** read `references/cli-glowup.md` first —
  layout patterns, design lenses, the terminal usability checklist, and ANSI
  implementation helpers to lift rather than re-derive. The design canon
  (`references/canon.md`) holds Nielsen/Gestalt translated to terminals plus best-in-class
  exemplars; read it before a look pass and hold the tool to its genre's best, not a
  generic standard.
- **Skill pass:** read `references/skill-design.md` first — it contains the working
  checklist, heuristic translation, and self-QA protocol.
- **Any Display mockup:** read `references/terminal-constraints.md` before drawing it —
  the renderability gate checks every element against its substitution table.
- **Export visual or Share Before/After selected:** read `references/export-share.md`
  and follow it. Do not load it otherwise.

## Never break the machine path

- Enable ANSI styling only when `stdout` is a TTY
  (`process.stdout.isTTY` / `sys.stdout.isatty()`) unless the user explicitly supplies a
  documented force-color flag. Piped output stays plain by default.
- Return from every structured-output path before human rendering. `--json` and other
  documented machine formats must remain byte-identical in a look pass.
- Preserve documented exit-code values. Keep diagnostics on stderr and data on stdout.
  A separately approved feel pass may improve human error wording while preserving the
  error's meaning and any structured error representation.
- Respect `--no-color` and the `NO_COLOR` env var.
- Test interactive, noninteractive, piped, and structured paths independently. TTY
  detection is a transport hint, not proof that the caller is human.

## When NOT to glow up

Do not add human decoration to output consumed only by programs. For agent-only or CI-only
paths, improve the contract instead: discoverability, schemas, structured errors,
noninteractive behavior, and safe retries. Do not rewrite a well-performing skill merely
to change its prose style. If the requested change has no reader or task benefit, explain
that and stop.
