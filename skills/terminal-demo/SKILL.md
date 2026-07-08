---
name: terminal-demo
description: Create polished terminal/CLI demo recordings as mp4 or gif. Use when asked to record a CLI demo, make a terminal recording, produce a demo video, or animate command-line output.
---

# Skill: terminal-demo

Create polished terminal/CLI demo recordings as mp4 or gif.
Use when asked to record a CLI demo, make a terminal recording, or produce a demo video.

---

## What makes a great terminal demo

1. **Tables over raw JSON** -- reformat all API output as aligned tables with color headers
2. **Color as information, not decoration** -- every color means something specific and consistent
3. **Pacing matched to reading speed** -- ~200wpm technical reading speed
4. **Real data** -- values from real API calls, not mocked output
5. **Font matters for video** -- JetBrains Mono survives h264 compression; use 20px for embeds

---

## Script structure

```
HEADER       -- context, what problem we're solving
PROBLEM 1    -- section header + comment + command + table output + summary comment
PROBLEM 2    -- same pattern
PROBLEM 3    -- same pattern
SUMMARY      -- clean results table, one line per problem solved
```

- No role labels ("an engineer needs to...") -- let the action speak
- Each section: header in accent color -> one-line comment -> command -> table -> one-line result

---

## Color system

| Role | Color | Hex |
|---|---|---|
| Section header | Purple | `#B87FFF` |
| Tool / command | Green | `#4CAF50` |
| Success | Teal | `#14B8C8` |
| Primary text | Off-white | `#F5F7FA` |
| Supporting text | Gray | `#B9BCC5` |
| Dim / structural | Dark gray | `#60636E` |
| Background | Near-black | `#1F2023` |

### ANSI variables (bash)
```bash
BOLD=$'\e[1m'; RESET=$'\e[0m'
GREEN=$'\e[38;2;76;175;80m'
PURPLE=$'\e[38;2;184;127;255m'
TEAL=$'\e[38;2;20;184;200m'
WHITE=$'\e[38;2;245;247;250m'
GRAY=$'\e[38;2;185;188;197m'
LGRAY=$'\e[38;2;96;99;110m'
```

---

## Pacing

| Line type | Delay |
|---|---|
| Divider (`───`) | 0.2s |
| Empty line | 0.6s |
| Section header | 2.0s |
| Comment (`# ...`) | 1.2s |
| Command (`$ ...`) | 1.5s |
| Success marker (`✓`) | 0.8s |
| Table header | 0.6s |
| Regular output | 0.45s |
| End of demo | 2.5s |

---

## Font

- JetBrains Mono, 20px, line height 1.4 for presentation embeds
- 16px for README/docs embeds

---

## agg settings

```bash
agg \
  --font-family "JetBrains Mono" --font-size 20 --line-height 1.4 \
  --cols 120 --rows 36 \
  --theme "1F2023,F5F7FA,1F2023,FF6B6B,4CAF50,F4BF75,6B9BFF,B87FFF,14B8C8,F5F7FA,3A3D42,FF8A8A,6FCF6F,FFD080,8AB4FF,C99FFF,3DD8E8,FFFFFF" \
  --idle-time-limit 3 --last-frame-duration 4 \
  demo.cast demo.gif
```

Theme color order: bg, fg, black, red, green, yellow, blue, magenta, cyan, white, then 8 bright variants.

---

## ffmpeg conversion

```bash
ffmpeg -y -i demo.gif \
  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" \
  -c:v libx264 -pix_fmt yuv420p -crf 16 \
  demo.mp4
```

CRF 16 = high quality. Use 18 for smaller files, 14 for maximum quality.

---

## Terminal dimensions

| Use case | Cols x Rows |
|---|---|
| Presentation embed | 120 x 36 |
| README / docs | 100 x 28 |
| Full screen hero | 160 x 42 |

---

## Pipeline

```bash
bash demo-script.sh > /tmp/demo-output.txt 2>&1   # 1. capture real output
python3 build-cast.py                              # 2. build .cast with timing
agg [flags] demo.cast demo.gif                     # 3. render with theme
ffmpeg [flags] demo.gif demo.mp4                   # 4. convert to mp4
```

---

## What NOT to do

- Don't dump raw JSON -- always reformat as tables
- Don't fake slow character-by-character typing -- use line-level timing instead
- Don't add role labels ("an SRE needs to...") -- let the action speak
- Don't use color for decoration -- every color must have a consistent semantic meaning
- Don't use pure `#FFFFFF` as foreground -- causes halation under h264. Use `#F5F7FA`
- Don't record interactively against a live environment -- use script + capture for repeatability
- Keep demos under 90 seconds for presentation embeds -- 60s is ideal
