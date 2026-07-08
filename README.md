# opencode-skills

A collection of [OpenCode](https://opencode.ai) skills for PMs and technical folks who build demos and presentations.

## Skills

| Skill | What it does |
|---|---|
| [`terminal-demo`](./skills/terminal-demo/SKILL.md) | Create polished terminal/CLI demo recordings as mp4 or gif |
| [`thought-partner`](./skills/thought-partner/SKILL.md) | Structured product thinking framework -- JTBD, friction diagnosis, SCAMPER -- before committing to a solution |
| [`prd-generator`](./skills/prd-generator/SKILL.md) | Generate a Product Requirements Document from customer evidence and context |

---

## Install

### One skill at a time

```bash
npx skills add rchandnaWUSTL/opencode-skills@terminal-demo -g
```

### Manually (no CLI needed)

1. Create the skills directory if it doesn't exist:
   ```bash
   mkdir -p ~/.config/opencode/skills/terminal-demo
   ```

2. Copy the skill file:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/rchandnaWUSTL/opencode-skills/main/skills/terminal-demo/SKILL.md \
     -o ~/.config/opencode/skills/terminal-demo/SKILL.md
   ```

3. Restart OpenCode.

---

## Usage

Once installed, OpenCode will automatically load the skill when relevant. You can also trigger it explicitly:

```
Make a terminal demo showing how to search and filter workspaces
```

Or load it manually in any session:

```
/skill terminal-demo
```

---

## What the `terminal-demo` skill does

Gives OpenCode a complete playbook for creating professional terminal recordings:

- Formats API output as clean tables instead of raw JSON
- Applies a consistent color system (purple headers, green commands, teal success)
- Times each line to reading speed so demos feel natural
- Uses JetBrains Mono at 20px -- survives h264 compression
- Produces a `.cast` -> `.gif` -> `.mp4` pipeline using `agg` and `ffmpeg`
- Keeps demos under 90 seconds for presentation embeds

---

## Requirements

To run the full pipeline you'll need:

- [`agg`](https://github.com/asciinema/agg) -- converts asciinema casts to gif
- [`ffmpeg`](https://ffmpeg.org) -- converts gif to mp4
- [`JetBrains Mono`](https://www.jetbrains.com/legalforms/fonts/) -- font for rendering

Install on macOS:
```bash
brew install agg ffmpeg
```

---

## Contributing

PRs welcome. Each skill lives in `skills/<name>/SKILL.md`.
