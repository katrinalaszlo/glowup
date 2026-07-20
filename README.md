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
this skill,” or “audit this skill's interaction design.”

## How a run works

glowup keeps one progress marker visible as the work moves through five stages:

```text
Capture → Choose → Preview → Implement & Verify → Compare & Finish
```

At each transition it states what is happening now and what comes next, without
narrating every command.

1. **Capture the Before.** glowup performs a quick orientation and runs one
   representative path to record the real command, output, interaction, and
   terminal dimensions. This opening pass stays read-only and does not create
   fixtures, spawn reviewers, or diagnose every path.
2. **Choose the focus when needed.** If your request is ambiguous, glowup
   recommends **Display**, **Flow**, or **Both**. If you already named the focus,
   it skips the question. On a bare `/glowup`, these are the only opening options;
   findings support the recommendation instead of becoming another intake menu.
3. **Review the Proposed After.** Display changes use a terminal mockup or an
   isolated rendered snapshot. Flow changes use a short interaction transcript.
   Both use the same command and representative data as the Before.
4. **Approve before implementation.** Apply the direction, revise the preview,
   or change focus. No product code changes before approval. Deeper compatibility
   baselines run only after approval and stay scoped to the selected change.
5. **Compare the verified result.** glowup runs the implemented tool, replaces
   the preview with a real Final After, verifies machine contracts, and offers an
   optional export. Its final response always includes the original Before, the
   Final After, confirmed changes and checks, and the next-action checklist.

At the end, select one or more next actions: **Export Before/After**, **Share on
GitHub**, **Commit changes**, or **Continue Glowup**. **Finish here** is the only
exclusive option.

When you select Export, glowup creates the comparison and opens its primary file
in your local viewer automatically. If the environment cannot open files, it
provides one direct path instead. Export never means upload or publish.

When you select Share, glowup prepares and redacts a Before/After issue, shows
you the exact public draft, and posts it to the glowup repository only after you
approve it. The published issue opens automatically.

The default review stays in the conversation. High-fidelity snapshots,
recordings, and HTML export pages are optional. When the target is not runnable
locally, you can provide a screenshot or pasted output; glowup does not download
or install it without permission.

## What a run produces

For a CLI, the result is the same machine contracts with a clearer and more
useful human experience:

![A CLI before glowup and after glowup, with the same data organized into a clearer visual hierarchy.](assets/before-after.svg)

At the end, glowup can save a Markdown comparison with linked terminal captures
or screenshots, or a short recording when the interaction itself changed.

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
and share what you noticed—what worked, what didn't, or what you would
change. If you have a pattern, principle, or example that belongs in the skill,
fork the repository and open a pull request.

You don't need to be a designer. Experience from design, engineering, and
everywhere in between will make glowup better. You can also
[open a feedback issue](https://github.com/katrinalaszlo/glowup/issues/new?template=feedback.yml).

[MIT](LICENSE)
