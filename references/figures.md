# Figure rules

Code: copy `../assets/style.py` into the paper's `plots/` and `from style import *` in every script.
Data in `plots/data/*.csv`; PDFs to `Figs/`; PNG previews to `plots/preview/` (git-excluded). Always
render the PNG and look at it before pushing.

## Ink, font, size
- Everything that would default to black (text, axes, ticks, legend) is `#44546A`.
- Arial (Helvetica / Nimbus Sans on servers). Sized for 10 pt body at 6.5 in text width:
  8 pt labels and titles, 7 pt ticks and legend, about 6.5 pt in-plot text.
- **Full-width figures are exactly 6.5 in wide**: call `fit_width(fig)` before `savefig` (tight bbox shrinks them otherwise).
- Embed fonts as TrueType (`pdf.fonttype 42`).

## Color
- Default: blue-green ramp, ours darkest.
  `ramp = LinearSegmentedColormap.from_list('ramp', SPECTRAL[4:])`,
  colors `ramp(v)` for `v in np.linspace(1.0, 0.12, n)` in legend order (ours first).
- Full strip when many methods are needed: `palette_for(ORDER)` (ours `#CA324C`, baselines a contiguous run
  ending at the blue end). The user found red/yellow too saturated on line plots, so prefer the ramp.
- Heatmaps: white → green → teal → blue from the same strip.
- Colors as given: no darker edges, no white marker rims, no glow.
- Lines and markers alpha 0.65; error bands alpha 0.2. "透明度 X%" means transparency, so alpha = 1 − X%.
- To distinguish a second factor on bars (e.g., epoch), use hatching or outline, not lighter shading.

## Layout
- Open frame (no top/right spines), light grid at tick positions.
- Panel titles bold and centered over their panel (user 2026-10-19): "(a) Training epochs". Each panel title distinct
  and meaningful. Raise a title with `pad` when in-plot labels sit near the top.
- Log axes are labeled as such: "Training epoch (log scale)".
- Std over seeds as bands (lines) or whiskers (bars). With one seed, the band is the std over suites, and the caption
  says so. Placeholder std only when the user asks, flagged in the caption.
- When panels show different method sets, each panel gets its own legend (no shared legend that lists methods a
  panel does not have).
- A figure with little content may be narrower than the text width (e.g., 5.0 in), centered, rather than stretched.
- Text and labels must not overlap curves; inset/annotation boxes move to empty space. Tick labels kept off lines.
- No separate legend when an inset or direct labels already identify the methods.
- Gains shown as arrows with the value (e.g., "+12.3") rather than extra whiskers. When the gap is small or the
  curves crowd the point, use a slim bracket beside it with a rotated label, outside the curves.
- Keep the first x tick close to the y axis; make room for labels with brackets, not with a wide empty margin.
- Zoom insets: dashed outline, tick labels off.
- Images inside plots (robots, tasks) at reduced alpha (≈0.55), zorder below grid-sensitive elements, shadows removed.
  Flag brand/copyright concerns for third-party images.

## Annotations and photo figures (journal style)
- Plain text annotations: no background boxes, no shadows, no glow or light cones ("太AI了"). Thin leader
  ending in a small dot, thin motion arrows in one accent color. White text on dark regions, ink on light ones.
- Zoom insets of photos keep a thin ink border; no connecting cone.
- Real-robot montages: same frame size across figures, row labels in the left margin, "Step k  Name" above
  frames, success-rate bars to the right, centered vertically on the frames.
- Keep execution montages and quantitative plots (inference time, smoothness) as separate figures rather than
  stacking them.
- Frames can be cut from the rollout videos. Make a 1 s contact sheet with timestamps, pick one frame per step,
  crop to the frame aspect of the other montages (775x480), and match the color of the earlier frames, which the
  user brightened and tinted blue by hand. Use `assets/real_color_match.py` (an affine color map through five anchor
  colors: green screen, table, dark and mid gray of the robot, the vase). Per-channel histogram matching turned the
  gray robot purple, and four anchors without the vase turned it pink. Compare the new figure next to an old one.

## Grids
- For a grid of panels, give the legend its own empty slot and say which panels use which setting there
  (e.g., "(a)-(d) PPO", "(e)-(g) FlashSAC") instead of a caption line.
- Every panel keeps its own y tick labels when scales differ. Task titles name robot and task, aligned across rows.
- Robot icons the same size across a row, inside the axes, may sit behind the curves.

## Teaser (Fig. 1) of a method paper
Distilled from the StagePolicy teaser (2026-11-26, `2026-RSS-Jiayi/plots/fig_overview.py`, many rounds with the user).
- **Content.** One row at full text width. (a) shows how the idea differs from prior methods, (b) the main effect.
  Less information is fine, but a reader must see the contrast and the gain at a glance. Real-robot photos only
  when real data exist; otherwise simulation only.
- **Robot-like, not block-diagram-like.** The user rejected modular "AI-style" box diagrams. Draw the robot doing
  the task: a line-art arm (white links with an ink outline, dark joints with an accent-colored core, an accent
  band on each link, a two-finger gripper, a dark pedestal), a table, a target (bowl), translucent ghost poses
  for the motion, and a small accent block for a payload. The dashed desired path, the executed path and the plan
  points are drawn **above** the arm (higher zorder, thicker line, larger dots) and routed so the arm does not
  cover them (arc the path over the elbow).
- **Contrast lanes.** Baseline lane in neutral gray, ours in the paper's blue. Our method's name labels a dashed
  frame around **all** of its parts (including optional modules), not just its first block. Optional modules
  (e.g., a force channel, an online correction) are dashed and the caption says so. Each lane ends with a short
  bold italic outcome ("misses the bowl" / "reaches the bowl").
- **Networks.** A rounded pastel box with its title inside ("State predictor", "IDM net"), a small fully connected
  net of filled nodes graded light to dark along the depth, edges in the box color at low alpha. Nodes generous
  (radius about 0.05 in), never tiny.
- **Arrows and labels.** Arrows between modules in ink. Feedback as a right-angle dashed path. Label signals with
  the paper's notation (bold vectors, e.g. images $\mathbf{o}_t$, robot state $\mathbf{s}_t$, plan
  $\hat{\mathbf{s}}_{t+1:t+H}$, commands $\mathbf{a}_t$, "measured $\mathbf{s}_t,\mathbf{v}_t$"). Input groups get a
  light rounded box with an image stack and a state vector, each with a text label.
- **Type.** Larger than plot figures: about 10.5 pt panel titles, 9.5 pt lane names, 9 pt text, 8.5 pt small
  labels. Two-line labels need line spacing of at least 1.3. No text on lines or curves.
- **Colors.** After trying several custom palettes, the user went back to the skill strip: ours `#397DB7`, the
  second part of ours `#57B1AB`, test-time change accent `#EB6046`, baselines `#F99655` and `#8ECFB0`, ink
  `#44546A`. Rejected: red plus green for ours, saturated royal blue or violet for a module.
- **Panels.** No panel backgrounds, outlines or title bands (box-in-box clutter). Separate (a) and (b) with
  whitespace and one thin dashed hairline. Panel labels follow the paper ("(a) Title" in StagePolicy, by request).
- **Result panel.** A radar over all condition groups, never a selection (a subset with the smallest gaps left out
  looks cherry-picked). Labels outside the ring, anchored away from the centre, nudged by a few degrees where
  neighbours collide, no radial tick labels. Near-identical baselines differ in hue, line style and marker, with
  the dashed one drawn on top. Fill leftover space with a "mean over all conditions" number line that reuses the
  radar markers (it doubles as the legend) and an arc arrow with the gain ("+20.2"). The user rejected a bar chart
  there as off-style.
- **LaTeX.** In IEEEtran, hook `\@maketitle` and place the figure with `\captionof` (package `capt-of`). IEEEtran
  typesets the title block twice, so add `\setcounter{figure}{1}` right after `\maketitle`, or later figures
  skip a number. Check the page budget with a local compile after every size change.
