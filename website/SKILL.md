---
name: project-website
description: Jindou Jia's conventions for building and updating a paper's project website (static GitHub Pages site with a video cover, real-robot videos, web-native interactive charts drawn from the paper data, and animated method figures). Use when creating, redesigning, or editing a project page for one of the user's papers, adding experiment videos to it, or redrawing paper figures for the web.
---

# Project website (Jindou Jia's style)

Distilled from the ODE Policy page (https://jiajindou.github.io/ODE/, repo `JIAjindou/ODE`, 2026-10).
Reply in concise Chinese, conclusion first. The page is in English. The user decides the content; draft, then let them cut.

## 1. Stack and workflow

- One static page. `page.html` is the source (head content, nav, sections, one inline script). `build.py` wraps it
  into `index.html` (doctype, charset, viewport) for GitHub Pages. Also `README.md`, `.nojekyll`, `assets/`
  (`figs/`, `video/`, `data.js`), `tools/export_data.py`.
- Its own git repo. Commit and push after each change, then tell the user to wait 1-2 min and hard refresh
  (Ctrl+Shift+R). Copy the git identity from the paper repo before the first commit.
- Raw material the user uploads (videos, GBs) goes to `raw_videos/`, listed in `.gitignore`, never pushed. The user
  drags files from their Windows desktop into that folder in the VS Code explorer. Wait until the folder size is
  stable (background loop) before processing.
- Put the project page link into the paper (`\metadata[Project Page]{\url{...}}`) once the site is live.

## 2. Structure and tone

Order: **cover → epigraph → idea → results → method → BibTeX**. Concise and high-end ("精简高端").
- **Cover**: once there are many tasks, a full-screen 4x4 grid of short autoplay rollouts (480x270, crf 30, 1-4x,
  a small task label per tile) gives the first impression (user, 2026-10-31). Shuffle the tiles so the same robot is
  never next to itself, reuse tasks with several modes (both modes of a multi-modal task), 2 columns on phones.
  Before that, the best real-robot demo fills the first screen (autoplay, muted, loop, playsinline), dark gradient at
  the bottom-left, title, authors, buttons (Paper / Code "soon", BibTeX) over it, a small "Autonomous · 2×" tag.
- **Epigraph** on its own band, large italic serif (Instrument Serif), translation and author small below.
- **Idea**: one sentence, then the core comparison as two animations side by side (no toggle buttons).
- **Results first, method after.** A gallery of all real-robot tasks (one card per task with the ODE video, a
  one-line description, and bars for ours against the best baseline), grouped by robot, pending tasks marked
  "coming soon".
- **Results**: a row of four headline numbers, then one block per claim in the order of the paper
  (learns fast, executes precisely and smoothly, generalizes, multi-modality). In each block, videos first, then charts.
- **Method**: numbered steps. Each step is a row with title and text on the left and its equation (KaTeX) in a card
  on the right, with the visual full width below. Separate steps with a thin rule. Every step gets an equation.
- No eyebrow labels, subtitles, chips, or other non-core annotations. Section titles large (40-60 px); step and
  block numbers ("01", "1") the same size as their heading, in the accent blue.
- Fonts: Inter Tight (display; Bricolage Grotesque was rejected for its odd "ff" ligature), Source Sans 3 (body),
  JetBrains Mono (labels). Text in figures and charts close to the body size (14.5-16 px), never 11-12 px.
- **Dark background by default**, with a sun/moon toggle in the nav, saved in localStorage (try/catch). Define colors
  as tokens on `:root`, redefine under `[data-theme="dark"]`, set the theme in a head script before the first paint,
  and redraw charts on toggle.

## 3. Videos

- `ffprobe` every file, make 8-frame contact sheets, and pick representative clips per section: one ODE success per
  task plus one typical failure per baseline. Highlight videos that show our method is better.
- Prefer rollouts without network stalls. Detect pauses with frame differences (160x90 gray at 10 fps, motion
  below a threshold for more than 0.6 s inside the active part) and pick the clip with none.
- Encode with libx264 (the anaconda ffmpeg lacks it, use the static binary from the `imageio-ffmpeg` wheel):
  cover 1920 px crf 21, main players 1280 px crf 23, thumbnails crf 25, `-an`, `+faststart`, speed-up 2-3× with a
  speed badge on the video. Lazy-load with an IntersectionObserver (`data-src`), pause when out of view.
- Real-robot player: large ODE video on the left, task name, one-line description, success rates, and three
  baseline thumbnails (label plus failure reason) on the right. A click swaps the clicked clip with the large one:
  scroll the large player into view if needed, draw the current thumbnail frame into a canvas, fly it to the large
  player with the Web Animations API (arc, shadow, ~0.7 s), load the new video as a layer on top and cross-fade it in,
  keep `currentTime`. Never dim to black.

## 4. Charts

- Redraw the paper figures as web-native SVG from the paper data, not as images: `tools/export_data.py` reads the
  paper's `plots/data/*.csv` (and constants of the figure scripts) into `assets/data.js`.
- Each chart is a card with a title, a legend, the plot, and a caption "**Figure n.** ...". Captions state what is
  shown and the takeaway, and every claim is checked against the data (e.g., do not write "smoother than the
  demonstrations" where one metric is not). Mark illustrations as such.
- Hover tooltips with the values (mean ± std), legend hover highlights a series, reveal left to right the first
  time a chart is seen, redraw at the width of the box on resize. Segmented buttons for toggles (epoch, setting).
- Keep the paper colors (blue-green ramp, ours darkest) but space the baselines apart from ours. Gain brackets
  ("+33.5") to the right of the points. A difference heatmap (ours minus baseline) beats two side-by-side heatmaps.
- Small multiples (e.g., RL tasks) with nice ticks and their own titles.

## 5. Animated figures (canvas)

- Draw in virtual coordinates (`vstage`, a desktop and a phone layout) and size the backing store from the canvas'
  own `clientWidth` at `devicePixelRatio`. Measuring the parent with padding and borders made the canvas 2 px too
  wide and blurry.
- Lay out every label explicitly: nothing clipped at the edges, no text on curves, subscripts drawn as real
  subscripts (`rich()` helper), the dot of ȧ drawn by hand (the combining dot drifts in canvas text).
- Use analytic paths when the meaning requires it (all routes leave the start and meet exactly at the goal).
- Interactive demos play by themselves (e.g., the control rate cycles 20/40/80 Hz); no sliders or buttons needed.

## 6. Pitfalls and checks

- `-x ** 2` is a SyntaxError in JavaScript and silently kills the whole script. Use a helper `sq(x)`.
- `[hidden]{display:none!important}`, otherwise a lightbox with `display:grid` covers the page in gray.
- The first `requestAnimationFrame` delta can be negative. Clamp progress values.
- Verify in a real browser before every push: Playwright installed into the scratchpad (`pip --target`,
  `PLAYWRIGHT_BROWSERS_PATH`, `chromium-headless-shell`), open the page as `file://` (ports on the shared host are
  taken by other servers), full-page and element screenshots at desktop and 390 px width, `pageerror` must be empty,
  click through toggles and players, check there is no horizontal scroll.
