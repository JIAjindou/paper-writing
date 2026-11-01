---
name: promo-video
description: Jindou Jia's conventions for a paper's short promo film (about 90 s, no narration, Remotion, music-synced cuts of real-robot rollouts, headline numbers, and the website's method animations). Use when creating, revising, or exporting a promo or overview video for one of the user's papers.
---

# Promo video (Jindou Jia's style)

Distilled from the ODE Policy film (`Desktop/ODE/video/ODE_promo`, 2026-11). Reply in concise Chinese. The user
reviews every cut, so show half-resolution previews and change only what they name.

## 1. Stack and workflow

- Remotion project in its own folder of the paper workspace (copied from an earlier film of the user, e.g. the
  SANE/MARS template). Code in `src/promo/`: `theme.ts` (colors, fonts, easing), `Tile.tsx` (video tile, logo),
  `Fx.tsx` (background, sound effects, progress), `Scenes.tsx` (one component per page), `Promo.tsx` (the list of
  pages with their length in beats). Scripts in `scripts/`: `cut_clips.py`, `make_bgm.py`, `make_sfx.py`,
  `capture_method.py`, `set_cover.py`.
- Node and ffmpeg via winget on Windows. Preview `npx remotion render src/promo/index.ts Promo out/<name>.mp4
  --scale 0.5 --crf 24`, stills with `npx remotion still ... --frame=N --scale=0.5` to check single pages.
- **Render only half-resolution previews until the user asks for the 1080p export** ("先别导出 1080p"). Give each
  preview a new file name, since a preview open in the user's player is locked and stitching fails. Delete old ones.
- 1080p export with `--crf 18`, then embed the cover (`set_cover.py`). For the website, re-encode to about 13 MB
  (`libx264 -preset slow -crf 26 -movflags +faststart`, AAC 128k) and a 1280x720 JPG poster.

## 2. Story and rhythm

- About 90 s, no voice-over. Visual language only: videos, short keywords, big numbers, animations.
- **Results first, method after**: wall of rollouts, count of tasks, coverage (robot types and policy roles such as
  visuomotor policy, VLA, WAM, RL actor), one page per robot type, headline numbers, generalization,
  multi-modality, RL, then the idea and the method, then the outro.
- The opening shot shows the most impressive task (the user chose humanoid loco-manipulation). Start the clip where
  the whole robot is in view (head included).
- Every cut lands on a beat of the music (pages measured in beats, BPM from the track). Give number pages and
  generalization videos enough time to read (slower than feels natural to the editor).
- Method: as few techniques as possible, one short line per step, no equations. Reuse the website's method
  animations instead of drawing new diagrams.
- Leave out pages that only repeat a fairness note ("same demos, same training") or a detail ("no stutter between
  chunks").

## 3. Look

- Light, warm paper background (`#F6F4EE`, a touch of cream), not black and not pure white. Text in the paper's own
  dark ink (`#1F2A37`, `#44546A`), accents in the logo's blue-teal ramp.
- Video tiles rounded with a soft shadow, no black frames. Labels below the video, success rates in a small white pill
  on it (ours against the baseline).
- Titles in sentence case, never all caps. **Fonts large enough for a phone**: at 1080p nothing under about 28 px
  (tile labels 28+, rate pills 32+, footnotes 27, page titles 60+).
- Logo of the paper's Fig. 1 (with POLICY between two thin rules) at the start and the end.
- Arrows and connectors minimal, just enough to carry the meaning. "Not high-end enough" means simpler, more space,
  fewer decorations.
- Clip grading matches the paper figures (e.g. a light blue grade, a quarter of the first attempt, which was too
  strong). Tone-map HDR phone videos.
- Cover: the teaser figure without panel letters.

## 4. Sound

- The user supplies the music. The track fades out at the end (about 4.5 s). No extra sound at the end.
- Sound effects rare and quiet, at most about five in the film (a riser before the idea, a few accents), none on the
  title reveal.

## 5. Website animations in the film

- Record the canvas animations of the project page frame by frame with Playwright: replace `requestAnimationFrame`
  and `performance.now` with a fake 30 fps clock, force the light theme (`localStorage`, `color_scheme='light'`,
  check it, since the dark theme's light text vanishes on the paper background), grab each canvas with a
  transparent background, and encode VP9 WebM with alpha. Play with `OffthreadVideo transparent`, no card or
  background behind the animation.
- Do not blur, rescale small captures up, or redraw them. Capture at about 0.7x the film size with a 2x backing
  store so lines come out crisp.
- The site's animations loop. **Play exactly one cycle and freeze on its last frame** (`<Freeze>`), with the cycle
  length read from the page code, so a page never shows the start of a second loop.

## 6. Checks before showing a preview

- Stills of every changed page: no overlapping or clipped text, nothing too small, transitions not cut mid-animation.
- Numbers, task names, and baselines match the paper (the paper is the source of truth). Run a paper / website /
  video consistency pass before the final export.
