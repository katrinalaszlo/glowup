# Canon — product-design principles adapted to the terminal

## Contents

- [How to use this reference](#how-to-use-this-reference)
- [Thesis](#thesis)
- [The two audiences](#the-two-audiences)
- [Prior art](#prior-art)
- [Port the reason, not the rule](#port-the-reason-not-the-rule)
- [Nielsen's heuristics in a terminal](#nielsens-heuristics-in-a-terminal)
- [The end-to-end journey](#the-end-to-end-journey)
- [Terminal patterns](#terminal-patterns)
- [Exemplars](#exemplars)
- [Cross-cutting requirements](#cross-cutting-requirements)
- [Evidence discipline](#evidence-discipline)

## How to use this reference

Treat every item as a lens, not a universal rule. Inspect the tool, its users, its
machine contracts, and the task before choosing a principle or pattern. Preserve the
underlying UX need while adapting its expression to the terminal.

Keep three kinds of statements distinct:

- **Evidence:** what a source, test, or user actually showed.
- **Inference:** what the evidence may mean in this context.
- **Recommendation:** what to try and validate next.

A heuristic evaluation finds likely problems; it does not prove that a design is usable.
Validate important changes with real tasks, before/after evidence, and feedback.

## Thesis

CLI design has a long history. The current opportunity is not to invent it, but to make
its principles more accessible to designers who are building and engineers who want to
apply product-design judgment. Agent-mediated development makes the terminal a shared
surface among people, agents, and programs, each with different needs.

The strongest pattern is a stable contract with thoughtful policy and presentation on
top:

- The **CLI contract** defines inputs, outputs, streams, exit meanings, and automation.
- The **human interface** supports comprehension, control, recovery, and efficiency.
- An **agent or skill policy** can interpret intent and guide use without weakening the
  contract.

## The two audiences

Human-readable and machine-readable paths can share logic without sharing a renderer.

For people:

- Establish hierarchy and a clear next step.
- Use familiar domain language.
- Explain state, uncertainty, and recovery.
- Support learning without slowing down experienced users.

For programs and agents:

- Offer explicit structured and noninteractive modes.
- Keep schemas, streams, and exit meanings stable.
- Return actionable, structured errors.
- Support safe retries, previews, and idempotent operations where appropriate.

TTY detection is a transport hint, not proof of identity. Humans use pipes; agents use
pseudo-terminals. Explicit modes such as `--json`, `--no-input`, `--quiet`, and
`--dry-run` are authoritative.

## Prior art

- [Command Line Interface Guidelines](https://clig.dev/) — human-first design,
  composability, discoverability, and established conventions.
- [Primer CLI](https://primer.style/design/native/cli/) — GitHub's terminal design
  guidance for consistency, accessibility, and common workflows.
- [12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46) —
  help, flags, streams, and behavior under pipes.
- [Nielsen's usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
  — broad interaction-design lenses that can be adapted across media.
- [Evil Martians on progress displays](https://evilmartians.com/chronicles/cli-ux-best-practices-3-patterns-for-improving-progress-displays)
  — choose feedback based on whether work is unknown, countable, or measurable.
- [Charm](https://charm.land/) — examples of expressive terminal interfaces and
  reusable TUI components.

Do not imply that these sources all share one lineage or endorse every recommendation
in this file. They are complementary references.

## Port the reason, not the rule

Transfer the constraint a principle protects, not its surface implementation. If the
constraint has no useful analog in the terminal, leave the rule behind.

For every principle borrowed from another field, ask:

1. What underlying human or system need does it protect?
2. How is that need expressed in the original medium?
3. What changes in a terminal or agent-mediated workflow?
4. What would fail if the original implementation were copied literally?
5. What is the adapted recommendation?
6. What observable evidence would show improvement?

Examples:

- Visibility of status does not justify progress noise on stdout. Use stderr for human
  progress and structured events for machine consumers.
- Plain-language errors do not require removing error codes. Pair a readable diagnosis
  with a stable machine-readable code when callers branch on it.
- User control can mean cancellation, undo, preview, or an approval boundary; it does
  not require adding a prompt to every command.
- Minimalism means prioritizing information for the task, not simply printing less.

## Nielsen's heuristics in a terminal

| Heuristic | Terminal adaptation |
|---|---|
| Visibility of system status | Show timely progress for long work; keep instant work quiet; do not pollute data streams. |
| Match between system and real world | Use the user's domain language and a natural command grammar, not internal architecture. |
| User control and freedom | Support cancel, safe interruption, dry-run, undo, and clearly scoped approvals where they matter. |
| Consistency and standards | Follow platform conventions for verbs, flags, streams, help, color, and exit behavior. |
| Error prevention | Validate early, choose safe defaults, constrain dangerous input, and confirm only consequential actions. |
| Recognition rather than recall | Lead help with examples, surface relevant options in context, and support completion. |
| Flexibility and efficiency | Provide a clear default path plus expert flags, shortcuts, and noninteractive operation. |
| Aesthetic and minimalist design | Focus attention on the current task; remove irrelevant decoration and repeated explanation. |
| Recognize, diagnose, and recover from errors | State what failed, why when known, and the next corrective action; preserve structured error data. |
| Help and documentation | Make help searchable, concise, task-oriented, and available at the moment it is needed. |

## The end-to-end journey

Audit the whole task, including the seams between commands:

1. **Discover:** Can the intended user find and correctly describe the capability?
2. **Orient:** Does first run or help establish the mental model?
3. **Act:** Is the common path direct, predictable, and appropriately interactive?
4. **Understand:** Can the user tell what happened and what the result means?
5. **Recover:** Can they correct mistakes without losing work or guessing?
6. **Verify:** Can a person or agent confirm that the intended state was reached?
7. **Continue:** Is the next relevant action visible, or is completion clearly stated?

Shareability can be a goal for a stats, identity, or reporting tool. It is not a required
stage in every CLI journey.

## Terminal patterns

- **First run:** provide a useful default, concise task-oriented help, or a short guided
  path. Preserve a noninteractive equivalent.
- **Help:** lead with two or three real examples, then document grammar and flags.
- **Progress:** use a spinner for unknown duration, X-of-Y for countable work, and a bar
  for a measurable fraction. Send it to stderr.
- **Errors:** show a readable diagnosis and one corrective action; retain any structured
  error representation.
- **Empty states:** state what was checked, why the result is empty, and whether there is
  a useful next step.
- **Success states:** confirm the changed state and any important consequence. Calibrate
  warmth to the stakes and voice.
- **Choice:** show the meaningful difference, cost, and risk of each option. Include a
  legitimate cancel or do-nothing path.
- **Progressive disclosure:** keep the common result focused and put secondary detail
  behind help, a flag, or a follow-up command.

## Exemplars

Pattern-match against a tool in the same genre instead of imposing a generic style:

| Tool | Useful precedent |
|---|---|
| `gh` | Parallel command grammar, structured output, and task-oriented help |
| `stripe` | Actionable errors, docs links, and live-operation feedback |
| `cargo` / `rustc` | Errors that teach diagnosis and recovery |
| `create-next-app` | A short guided first run with sensible defaults |
| `fzf` | Interaction speed and keyboard efficiency |
| `bat` / `eza` | Human presentation layered over familiar command behavior |
| `httpie` | Distinct human and machine representations |
| `ollama` / `uv` | Informative determinate progress |
| Charm tools | Expressive terminal interaction with a coherent visual system |

## Cross-cutting requirements

- **Accessibility:** never rely on color alone; avoid low-contrast dim text for essential
  information; honor `NO_COLOR`; keep keyboard operation complete; account for display
  width and screen readers.
- **Trust:** state uncertainty, scope, and side effects honestly. Do not turn another
  product's output into promotion without explicit intent.
- **Performance:** avoid interaction or decoration that makes a fast task feel slow.
- **Reversibility:** prefer preview, dry-run, undo, and idempotence for high-cost actions.
- **Compatibility:** capture machine fixtures before editing and compare them afterward.
- **Voice:** match the product and moment. Routine operations, incidents, and destructive
  actions usually require more restraint than personal stats or milestones.

## Evidence discipline

For each glowup, record:

- The task and intended audience
- The before artifact
- The observed problem
- The principle used and how it was adapted
- The approved change boundary
- The after artifact
- Machine-contract verification
- User feedback, including what became worse

Prefer concrete observations over universal claims. When evidence is limited, label the
conclusion as a hypothesis and propose the smallest useful test.
