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
- Panel titles bold: "(a) Training epochs". Each panel title distinct and meaningful.
- Log axes are labeled as such: "Training epoch (log scale)".
- Std over seeds as bands (lines) or whiskers (bars). Placeholder std only when the user asks, flagged in the caption.
- Text and labels must not overlap curves; inset/annotation boxes move to empty space. Tick labels kept off lines.
- No separate legend when an inset or direct labels already identify the methods.
- Gains shown as arrows with the value (e.g., "+12.3") rather than extra whiskers. When the gap is small or the
  curves crowd the point, use a slim bracket beside it with a rotated label, outside the curves.
- Keep the first x tick close to the y axis; make room for labels with brackets, not with a wide empty margin.
- Zoom insets: dashed outline, tick labels off.
- Images inside plots (robots, tasks) at reduced alpha (≈0.55), zorder below grid-sensitive elements, shadows removed.
  Flag brand/copyright concerns for third-party images.
