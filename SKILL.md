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
Now: Choose Display, Flow, or Both.
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
   - If the target command or screen cannot be inferred, ask only for the missing command,
     screenshot, or pasted output. Do not download or install a target merely to preview
     it without explicit approval.
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
   issue scope, or visual directions. Reserve **Both** for the Display + Flow focus; use
   **All findings** when referring to multiple issues. Before opening the choice, put the
   captured evidence and recommendation in normal conversation. If using AskUserQuestion,
   give each option only a label and short description; do not attach a preview panel.
   Describe confirmed observations, not suspected causes. Do not promote a finding into
   an option merely because a code search suggests it; reproduce it first or label it as
   a hypothesis for the selected pass.
   For a skill target, recommend the highest-leverage focus and ask one similarly
   consequential question only when it cannot be inferred.
4. **Preview — preview before editing.** Put the review in the conversation by default. Show the
   captured **Before** beside or immediately before a clearly labeled **Proposed After**,
   using the same command, data, and terminal dimensions.
   - **Display:** use a fenced monospace mockup. When visual fidelity materially affects
     the decision and the tool can run safely, render the proposal in an isolated
     temporary copy and capture a fixed-size image. Label mockups as concepts and
     temporary renders as previews; neither is the implemented result.
   - **Flow:** show the current and proposed interaction as short transcripts. Use a
     recording only when timing, motion, or key sequences affect the decision.
   - **Both:** combine the static comparison with the shortest useful flow transcript.
   Stack large captures instead of shrinking them; if a detail is cropped, keep the full
   capture available for context. Do not open two terminals or generate an HTML report by
   default. In standard Claude Code, do not rely on an option `preview` field; it requires
   a separately configured Agent SDK host.
   Only after the user chooses the focus, show the complete Proposed After in normal
   conversation. Then ask the user to **Apply**, **Revise the preview**, or **Change
   focus** before editing; do not combine focus selection with implementation approval.
5. **Choose the change boundary.**
   - **Look pass:** change presentation only. Keep logic and all machine behavior intact.
   - **Feel pass:** improve interaction behavior such as first run, recovery, progress,
     or reversibility. Show the proposed flow and obtain explicit approval before editing.
     Preserve documented inputs, structured outputs, exit meanings, and noninteractive
     paths; add compatibility tests for any intentionally changed human-facing behavior.
   - **Skill pass:** improve triggering, instructions, progressive disclosure, judgment
     boundaries, user checkpoints, safety, or validation. Preserve the skill's stated
     purpose and any tool contracts; obtain approval before broadening its authority or
     product scope.
6. **Port the reason, not the rule.** For each recommendation, name the reader, the
   protected human or system constraint, what changes in this medium, and the observable
   test. Use a heuristic only when its underlying constraint transfers.
7. **Implement & Verify — confirm orientation and capture baselines.** After the user approves the preview,
   restate the target, selected pass, change boundary, contracts that will remain
   unchanged, and the next stopping point. If the user redirects the preview, update it
   before continuing. For a CLI, only now capture the relevant compatibility baselines:
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
   At the end, ask **What should I do next? Select all that apply.** Use a multi-select
   question when the host supports it, with these applicable actions:
   - **Export Before/After** — Markdown with linked text or image captures, or a short
     terminal recording when interaction matters.
   - **Share on GitHub** — prepare a public Before/After issue for the glowup repository.
   - **Commit changes** — stage and commit only the approved product changes.
   - **Continue Glowup** — begin another Display or Flow pass.
   - **Finish here** — leave the verified changes as they are; select this alone.

   Do not represent the additive actions as mutually exclusive radio options or make
   **No export** an action. If multi-select is unavailable, ask the user to list every
   desired action in one response. If Export and Commit are both selected, keep the
   export outside the target repository unless the user explicitly approves adding it.
   When **Export Before/After** is selected, create the export and open its primary
   artifact in the appropriate local viewer by default; the selection authorizes both
   local actions. If the bundle has several files, open one comparison index that links
   the captures rather than opening every asset. If local opening is unavailable, provide
   one clear clickable path and the exact command for opening it. Opening locally never
   authorizes uploading, publishing, or sharing the artifact.

   When **Share on GitHub** is selected, prepare the comparison even if Export was not
   also selected. Redact it, then show the exact issue title, body, links, and images that
   would become public. Obtain confirmation on that final draft before creating the issue
   in the glowup repository. After creation, open the published issue for the user. If
   authenticated issue creation is unavailable, open the repository's Before/After issue
   form and provide the prepared content to paste. Never treat Export alone as permission
   to share publicly.

   HTML may wrap exported captures but is not the default preview or source of truth.
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

   Do not finish with only raw After output and an implementation summary.

## Pass playbooks

Load the depth for the pass you are running, nothing else:

- **Look or feel pass (CLI or developer tool):** read `references/cli-glowup.md` first —
  layout patterns, design lenses, the terminal usability checklist, and ANSI
  implementation helpers to lift rather than re-derive. The design canon
  (`references/canon.md`) holds Nielsen/Gestalt translated to terminals plus best-in-class
  exemplars; read it before a look pass and hold the tool to its genre's best, not a
  generic standard. A worked before/after with its exact code change is in
  `references/example.md` — pattern-match against it instead of inventing.
- **Skill pass:** read `references/skill-design.md` first — it contains the working
  checklist, heuristic translation, and self-QA protocol.

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
