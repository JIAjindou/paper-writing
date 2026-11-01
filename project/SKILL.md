---
name: paper-project
description: Jindou Jia's end-to-end process for a paper project, covering the paper (Overleaf), the project website, and the promo video, how they stay consistent, and how the workspace is laid out. Use when starting a new paper project, planning what comes next after the experiments, or running a final consistency pass across paper, website, and video.
---

# Paper project pipeline (Jindou Jia)

Distilled from the ODE Policy project (2026-10/11). The details of each part live in their own skills:
`paper-writing` (paper and figures), `project-website` (site), `promo-video` (film). This file is the order of work
and the rules that tie them together.

## 1. Workspace

One folder per project, for example `Desktop/<Project>/`:
- `<Project>_overleaf/` Overleaf git clone (paper, `plots/` scripts and `plots/data/*.csv`, `Figs/`).
- `<Project>_website/` GitHub Pages repo (`page.html` → `build.py` → `index.html`, `tools/export_data.py` reads the
  paper's CSVs).
- `video/<Project>_promo/` Remotion film.
- `videos/<platform>/<task>/` raw rollouts and logs (GBs, never in git), `reports/` (benchmark and real-robot
  reports), `slides/`.
- A local `CLAUDE.md` in the paper clone with the project facts (results, trials, epochs, demos, open items),
  excluded from git, updated whenever the user gives a new fact.

## 2. Order of work

1. Experiments come in as reports and logs. Put numbers into `plots/data/` and the paper. Ask for trials, epochs,
   and demonstration counts, never guess.
2. Paper: sections, figures (real-robot rows in one shared format), appendix. Fig. 1 (teaser) on page 1.
3. Website once the paper is stable: cover wall of rollouts, results first, charts from the paper data, method
   animations on canvas. Link it from the paper (icons for Project Page and Code under the authors).
4. Promo film last, reusing the website's videos, numbers, and animations, with the teaser as its cover.
5. Every new result (a new robot, a new task) goes into all three: paper text and figure, teaser, website card and
   headline numbers, film page.

## 3. Consistency

- **The paper is the source of truth** ("一切以paper为主"). Before an export or a release, list every number, task
  name, baseline, and claim on the website and in the film, compare with the paper, and fix the other two.
- Numbers only from data files and the user's messages. A number shown nowhere in a figure stays in the text.
- Captions on the site and labels in the film use the paper's wording for baselines and tasks.

## 4. Working with the user

- Reply in concise Chinese, conclusion first. The user decides content; draft, then let them cut.
- Only carry out a plan you proposed when the user answers that exact question.
- Change only what was asked. Keep the user's own edits.
- Push the paper and the website right after each change and say so. Never commit build files, raw videos, or the
  local CLAUDE.md.
- Heavy or irreversible exports (1080p film) only when the user asks.
- When a correction is a standing preference, add it to the matching skill and push this repo.
