# ✨ glowup

**The design skill for your CLI.**

![Before: every line the same weight. After: title in cyan, TOTAL bold, fine print dimmed.](assets/before-after.svg)

## 🚀 Install

```bash
git clone https://github.com/katrinalaszlo/glowup ~/.claude/skills/glowup
```

Restart Claude Code. Run `/glowup` or say **"make my CLI cute."**

## 🧩 What you get

- 📸 **Six layouts:** receipt, scorecard, wrapped, badge, ranked table, streak
- 🎨 **Taste rules:** one accent color, aligned columns, emoji budget of two, one screen
- 🔒 **Machine path untouched:** `--json` byte-identical, pipes stay plain, exit codes
  intact, `NO_COLOR` respected
- 🧭 **Usability pass:** first-run, errors with directions, empty states, honest status
- 🚀 **Before/after pair:** your launch post, already written

## ⚡ How it works

1. Runs your tool, captures the real before
2. Finds the one screen with the user's own number in it
3. Shows layout previews built from your real output. You pick
4. Restyles under the taste rules
5. Verifies `--json`, pipes, exit codes, `NO_COLOR`
6. Hands you the before/after pair

Real runs with the exact code changes: [`references/example.md`](references/example.md)
Design canon: [`references/canon.md`](references/canon.md)

## Share your before and after!

In the spirit of user research, I'd love to see your before and after screenshots to keep improving the skill. Or make a fork and contribute :) 

MIT
