"""Shared figure style (Jindou Jia's papers). Copy into <paper>/plots/ and `from style import *`.

Arial (Helvetica; Nimbus Sans on servers). Sizes are set for a figure at the full text width (6.5 in)
next to 10 pt body text.
"""
import os
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap, to_hex

TEXT_WIDTH = 6.5  # inches, letter paper with 2.5 cm margins

for d in [os.path.expanduser('~/.fonts'), os.path.expanduser('~/.local/share/fonts')]:
    if os.path.isdir(d):
        for f in os.listdir(d):
            if f.lower().endswith(('.ttf', '.otf')):
                font_manager.fontManager.addfont(os.path.join(d, f))

INK = '#44546A'  # every element that would default to black
LINE_ALPHA, BAND_ALPHA = 0.65, 0.2

mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'Nimbus Sans', 'DejaVu Sans'],
    'font.size': 8, 'axes.labelsize': 8, 'axes.titlesize': 8, 'axes.titleweight': 'bold',
    'xtick.labelsize': 7, 'ytick.labelsize': 7, 'legend.fontsize': 7,
    'text.color': INK, 'axes.edgecolor': INK, 'axes.labelcolor': INK, 'axes.titlecolor': INK,
    'xtick.color': INK, 'ytick.color': INK, 'legend.labelcolor': INK,
    'axes.linewidth': 0.8, 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': True, 'grid.color': '#E3E6EC', 'grid.linewidth': 0.6,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'savefig.dpi': 300, 'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02,
})

# The user's palette strip, red (ours in the full-strip mode) to blue.
SPECTRAL = ['#CA324C', '#EB6046', '#F99655', '#FED993', '#D5ECBB', '#8ECFB0', '#57B1AB', '#397DB7']
RAMP = LinearSegmentedColormap.from_list('ramp', SPECTRAL[4:], N=256)  # #D5ECBB -> #397DB7


def ramp_colors(methods, lo=0.12):
    """Default: blue-green ramp in legend order, the first method (ours) darkest."""
    return {m: to_hex(RAMP(v)) for m, v in zip(methods, np.linspace(1.0, lo, len(methods)))}


def palette_for(methods):
    """Full strip: ours #CA324C, baselines a contiguous run ending at the blue end (gradient order kept)."""
    k = len(methods) - 1
    assert k <= len(SPECTRAL) - 1, 'more baselines than colors in the strip'
    run = SPECTRAL[len(SPECTRAL) - k:] if k > 0 else []
    return {m: c for m, c in zip(methods, [SPECTRAL[0]] + run)}


def fit_width(fig, width=TEXT_WIDTH, tol=0.005):
    """Widen the canvas until the saved (tight-bbox) figure is exactly `width` inches."""
    for _ in range(8):
        fig.canvas.draw()
        bb = fig.get_tightbbox(fig.canvas.get_renderer())
        w = bb.width + 2 * mpl.rcParams['savefig.pad_inches']
        if abs(w - width) < tol:
            break
        fig.set_size_inches(fig.get_figwidth() + (width - w), fig.get_figheight())
