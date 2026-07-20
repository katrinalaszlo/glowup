# glowup

**A design skill for the terminal**

CLI design isn't new. What's new is who can participate in it.

More designers are building, and more engineers can work directly with design
guidance. The terminal is becoming a shared product surface, but most reusable
design guidance still focuses on web and mobile.

glowup is a Claude Code skill for design engineers, designers who build, and
engineers who care about the experience of a CLI, developer tool, or agent
skill. It adapts established product-design principles to the people, agents,
and programs using the interface—without weakening the contracts they depend
on.

## Install

```bash
git clone https://github.com/katrinalaszlo/glowup ~/.claude/skills/glowup
```

If this creates `~/.claude/skills` for the first time, restart Claude Code.

## Usage

Open Claude Code in the project that contains your tool or skill, then run:

```text
/glowup
```

You can also ask Claude to “glowup my CLI,” “improve this tool's UX,” “glow up
this skill,” or “QA this skill.”

glowup inspects the real experience before changing anything. It identifies the
readers and contracts, recommends the most useful design focus, and asks one
consequential question before editing. It ports the reason behind a design
principle—not its surface treatment—and defines how the improvement will be
tested.

## What a run produces

For a CLI, the result is the same machine contracts with a clearer and more
useful human experience:

![A CLI before glowup and after glowup, with the same data organized into a clearer visual hierarchy.](assets/before-after.svg)

For a skill, the before and after includes both the instruction change and its
effect on a representative request in a fresh session.

## What it considers

- **Look:** hierarchy, alignment, whitespace, color, and a layout that fits the
  information.
- **Feel:** first-run guidance, actionable errors, useful empty states, honest
  progress, and clear next steps.
- **Machine interface:** plain output when piped, unchanged `--json` and exit
  codes, and support for `NO_COLOR` and `--no-color`.
- **Skill experience:** discovery, progressive disclosure, useful questions,
  appropriate judgment, safety, validation, and context cost.

See a [worked before-and-after](references/example.md) with the exact code change,
or read the [terminal design principles and prior art](references/canon.md) behind
the CLI path and the [skill-design rubric](references/skill-design.md) for
human-agent collaboration.

## Use glowup on itself

Point glowup at its own `SKILL.md` and run the normal workflow. Self-review can
surface ambiguity and missing checks, but it is not independent validation:
compare the revised skill on the same request in a fresh session and record what
improved, regressed, or remains uncertain.

## Roadmap

glowup starts with developer interfaces that can be tested against real tasks
and real before-and-afters. The same research will expand deliberately:

- **Now:** CLI and agent-skill design
- **Next:** human-agent workflow design
- **Exploring:** agent tool design for APIs, MCP, and function schemas

Accessibility, trust, documentation, and evaluation remain part of every stage.

## Help shape glowup

glowup should improve the way good products do: by learning from real use.

Share a [before and after](https://github.com/katrinalaszlo/glowup/issues/new?template=before-after.yml)
and tell us anything you noticed—what worked, what didn't, or what you would
change. If you have a pattern, principle, or example that belongs in the skill,
fork the repository and open a pull request.

You don't need to be a designer. Experience from design, engineering, and
everywhere in between will make glowup better. You can also
[open a feedback issue](https://github.com/katrinalaszlo/glowup/issues/new?template=feedback.yml).

[MIT](LICENSE)
