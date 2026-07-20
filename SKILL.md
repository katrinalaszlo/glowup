---
name: glowup
description: Improve a CLI, developer tool, or agent skill using product-design principles adapted to its real users and constraints. Inspect the current experience, recommend a focus, ask one consequential question, then improve human-facing hierarchy and flows or skill discovery, instructions, safety, and validation without breaking machine contracts. Use for "glowup my CLI", "improve this tool's UX", "glow up this skill", "audit this skill's interaction design", "make this easier to use or scan", or a pre-launch design review.
---

# glowup — design the developer experience

CLIs and agent skills are interfaces. Their hierarchy, feedback, first run, errors,
instructions, and recovery deserve the same design attention as a web or mobile product.
Apply established product-design principles to the reader's real constraints: the person
directing the work, the agent interpreting it, and any program consuming the result.
Inspect first, ask only consequential questions, and preserve documented contracts.

## Process

1. **Name the target, readers, and layer.** Distinguish a CLI or developer tool from an
   agent skill. Identify whether each important path serves a person, an agent, a program,
   or more than one. Name whether the proposed change affects policy that guides, a
   contract that makes failure detectable, or enforcement that blocks invalid behavior.
   Do not assume that a human-readable surface and a machine contract need the same
   treatment.
2. **Inspect the real experience safely.** Never design from imagination.
   - Read documentation, source, and tests before executing unfamiliar commands.
   - For a CLI, capture its common path, first run, help, one error, one empty or success
     state, piped output, structured output, and relevant exit paths. Use existing tests,
     fixtures, temporary configuration, sandboxes, and dry-run modes where possible.
   - For a skill, read `SKILL.md` completely and load only the references and assets
     relevant to a concrete request. Capture how a fresh session discovers, interprets,
     executes, and validates the skill.
   - Obtain explicit approval before any authenticated, networked, destructive,
     production-affecting, privacy-sensitive, or potentially costly execution.
3. **Recommend a focus.** Identify the highest-leverage opportunity: comprehension,
   hierarchy, first-run guidance, recovery, trust, efficiency, accessibility,
   discoverability, context economy, or shareability. Explain the evidence in one or two
   sentences. Do not assume the goal is visual polish or promotion.
4. **Ask one consequential question.** Recommend a focus and offer two or three
   meaningful alternatives. In standard Claude Code, show any visual directions as
   fenced monospace mockups, then use AskUserQuestion for the labeled choice. Do not rely
   on an option `preview` field; that requires a separately configured Agent SDK host.
   Use the tool's real captured data, never invented metrics.
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
7. **Confirm orientation before editing.** After the user chooses a direction, restate
   the target, selected pass, observed problem, change boundary, expected files or
   surfaces, contracts that will remain unchanged, and the next stopping point. If the
   user corrects the plan, update it before editing.
8. **Apply the smallest coherent change.** Use the relevant lenses, not every rule in
   this file. Preserve the product's established voice. Avoid decoration or instructions
   that do not help the selected goal.
9. **Verify every affected reader.**
   - For a CLI, compare captured machine fixtures, then inspect the human path in a real
     terminal. Confirm piped stdout and structured output byte for byte, documented exit
     codes by value, and stderr on the same channel with equivalent meaning unless an
     approved feel pass intentionally changes its wording.
   - For a skill, validate its structure and exercise representative requests in fresh
     sessions. Compare the agent's interpretation, actions, questions, and result against
     the captured before. Self-review is evidence generation, not independent proof; use
     a clean session or separate reviewer before calling the result validated.
   - When ANSI rendering cannot be judged directly, ask the user for a terminal
     screenshot and iterate on what they see.
10. **Deliver evidence safely.** Show the same task and data before and after, list the
   design decisions, report contract and behavior checks, and invite feedback. Separate
   observations from hypotheses. Before sharing any screenshot or transcript, review it
   for credentials, tokens, personal data, account identifiers, private endpoints, and
   local paths; redact sensitive content and obtain explicit approval for public sharing.
   Optimize the artifact for learning; make it promotional only when the user chose
   shareability.

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
