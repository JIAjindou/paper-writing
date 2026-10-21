"""Match the colors of frames cut from a rollout video to the frames of Fig. real (user, 2026-10-20).

The frames of Fig. real were brightened and tinted blue by hand. This fits one affine color map (3x3 and an
offset) that sends five anchor colors of the new frames (green screen, white table, dark and mid gray of the
robot, brown vase) to those of data/real/flower_*.jpg, and applies it to every new frame.
Usage: python3 real_color_match.py OUT_PREFIX frame1.png frame2.png ...   (writes OUT_PREFIX_1.jpg, ...)
"""
import sys, glob, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))


def load(fs):
    return np.concatenate([np.asarray(Image.open(f).convert('RGB')).reshape(-1, 3) for f in fs]).astype(float)


def anchors(a):
    green = a[(a[:, 1] > a[:, 0] + 30) & (a[:, 1] > a[:, 2] + 5)].mean(0)
    white = a[(a.min(1) > 170) & (a.max(1) - a.min(1) < 40)].mean(0)
    dark = a[(a.max(1) < 70) & (a.max(1) - a.min(1) < 25)].mean(0)
    mid = a[(a.min(1) > 90) & (a.max(1) < 150) & (a.max(1) - a.min(1) < 20)].mean(0)
    brown = a[(a[:, 0] > a[:, 1] + 12) & (a[:, 0] > a[:, 2] + 5) & (a.max(1) < 170) & (a.max(1) > 40)].mean(0)
    return np.stack([green, white, dark, mid, brown])


if __name__ == '__main__':
    prefix, raws = sys.argv[1], sys.argv[2:]
    ref = anchors(load(sorted(glob.glob(os.path.join(HERE, 'data', 'real', 'flower_*.jpg')))))
    src = anchors(load(raws))
    w = np.array([1, 1, 1, 1, 1.5])[:, None]  # the vase weighs more, otherwise it turns pink
    M = np.linalg.lstsq(np.hstack([src, np.ones((5, 1))]) * w, ref * w, rcond=None)[0]
    for k, f in enumerate(raws, 1):
        a = np.asarray(Image.open(f).convert('RGB')).astype(float); x = a.reshape(-1, 3)
        y = np.hstack([x, np.ones((len(x), 1))]) @ M
        Image.fromarray(np.clip(0.9 * y + 0.1 * x, 0, 255).reshape(a.shape).astype(np.uint8)).save(f'{prefix}_{k}.jpg', quality=92)
