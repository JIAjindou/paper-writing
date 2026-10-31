---
name: paper-writing
description: Jindou Jia's conventions for writing robot-learning papers in LaTeX (Overleaf git clone) and their figures. Use when drafting, revising, or polishing any section, caption, table, bib entry, or matplotlib figure of one of the user's papers, or when the user annotates paper.tex in Chinese.
---

# Paper writing (Jindou Jia's style)

Distilled from the ODE Policy paper (2026-10) and the earlier A2A paper (*Action-to-Action Flow Matching*,
arXiv 2602.07322, RSS 2026). The user decides what goes in. You draft, they cut. Default to fewer words.

## 1. Working protocol

- Reply in plain, concise Chinese, conclusion first. The paper is in English.
- The project is a git clone of Overleaf. **Pull before every edit** (`GIT_TERMINAL_PROMPT=0 git pull --ff-only`),
  then **commit and push right after each edit**, then verify with `git fetch && git status -sb`
  (a silent push failure happened once because Overleaf had diverged; rebase onto `origin/main` and push again).
  Never print tokens. Never commit a local CLAUDE.md.
- Local LaTeX usually cannot compile the template. Ask the user to compile on Overleaf; check `\cite` keys by grep.
- The user annotates in Chinese directly in the .tex on Overleaf. Revise per the note, then delete the note.
- Numbers come from the experiment logs/results files only. Never invent a number. Missing results become `\TODO{}`.
- When the user reverses a decision, apply it without arguing; if a choice is ambiguous, pick one and say so.
- Do not carry out a plan you proposed until the user answers that exact question. A short "ok" in a message about something else is not approval.
- Shell `rm`/`cp` may be aliased to interactive. Use `/bin/rm -f`, `\cp -f`.
- When asked to fix one thing (split a long sentence, add connectives), change only that. Rewriting the rest
  was rejected ("改的太多了"). Keep the user's own Overleaf edits unless told otherwise.
- To check float placement or a new LaTeX construct, compile a scratch copy with stub packages and render pages
  with `gs -sDEVICE=png16m`. Delete stale `.aux` files after removing a package. Prefer constructs that do not
  depend on package versions (an old `titletoc` leaked hyperref anchors, so the appendix contents is hand-written).

## 2. Language rules (check every edited paragraph before pushing)

1. **No colons and no semicolons** anywhere in prose, captions, or tables. Split into two sentences, or join with a comma, "and", "where", or parentheses (e.g., "(1 if ... and 0 if ...)" instead of "(1: ...; 0: ...)"). Generated tables need the fix in the generator too.
2. **Abbreviations.** Define once (`imitation learning (IL)`), then use only the abbreviation. Titles never use
   abbreviations, and bold run-in headings count as titles (`\textbf{{Reinforcement learning.}}`).
3. **Every new variable gets its domain at first appearance**, scalars included:
   $\mathbf{s}_t\in\mathbb{R}^{d_s}$, $H\in\mathbb{N}$, $\rho\in(0,1)$. Name parameters ($\theta$) and operators
   ($\odot$, sg). Never reuse a symbol for two things.
4. **Non-scalars are bold**, including vector-valued functions ($\boldsymbol{\pi}$, $\mathbf{f}_\theta$).
   Model names like $\pi_{0.5}$ stay unbolded.
5. **Person-named terms are italic**: \textit{Gaussian}, \textit{Euler}, \textit{Runge--Kutta}, \textit{Lipschitz},
   also \textit{adjoint}. Comparisons use \textit{vs.}
6. **Method names that are not abbreviations are lowercase** ("diffusion policy", `\m{}~policy`, "seamless chunking").
7. Present tense, "we". Notation introduced in prose ("Let ... denote", "where ... represents"). Equations numbered.
   Citations woven into sentences with `\citep`. Transitions: "Notably", "To this end", "However", "Instead".
8. No marketing language ("remarkably", "significantly" without a test, "unprecedented").
   Prefer concrete numbers with units (`3.5\,ms`, `22.8 hours`, `95.0\%`).
9. Name components by what they do, not how they are implemented (e.g., "contractive perturbation" over
   "start-point perturbation"; "seamless chunking" over "continuous execution").
9b. Name the class of baselines by the property that contrasts with ours, and check it cannot be misread in a
   neighbouring literature. "Discrete policy" was read as "quantized action tokens", so ODE Policy uses
   "direct-action policies" (the network outputs the action values themselves) with a one-sentence definition
   in Preliminaries.
10. Say "three random seeds", never list seed numbers.
11. Hedge what is not verified and scope claims to what was tested: "likely because ...", "on three of the four
    tasks", "on most tasks", "occurs in only a small part of robot tasks" (not "is rare"). A reason given as a
    fact must be tested; otherwise mark it as likely.
12. Panel letters are Science-style capitals (user 2026-10-30): bold "A", "B" in the figures (no parentheses),
    `\textbf{(A)}` in captions, "Fig.~\ref{fig:rl}(B)" in the text. Panel ranges use a single hyphen,
    "Fig.~\ref{fig:rl}(A-D)". "Fig." for panels of one figure, "Figs." only
    for several figures.
13. **No overlong paragraphs** (main text and appendix). When a paragraph covers several groups (e.g., simulated
    benchmarks, then tasks of each robot), split it into one bold run-in paragraph per group
    ("Simulated benchmarks." / "Dual-arm robot tasks." / "Dexterous-hand tasks."). A shared fact goes once at the
    start of the paragraph it applies to (user, 2026-10-30, appendix Benchmarks paragraph).
14. **Short sentences by default**, one idea each (user, 2026-10-31). Keep a long sentence only where its structure
    carries the meaning, e.g., a parallel list or a cause and effect that belong together. Split chains of
    "and ..., which ..., while ..." into separate sentences, and check that a merged clause stays logical (e.g.,
    training cost is not caused by the data, so it gets its own sentence).

## 3. Section patterns

See `references/sections.md` for templates. The essentials:

- **Experiments intro** poses numbered bold questions **(1)–(4)**, then one sentence on ablations.
- **Setup** has bold run-in paragraphs: Benchmarks / Baselines / Implementation / Evaluation. Details go to an
  appendix section "Experimental Details"; the main text keeps only what the reader needs.
- **Results paragraph** = what was run (with figure ref) → key numbers → why → **one concluding sentence**
  that states the takeaway ("Chunking is therefore essential, and $H=8$ balances ...").
  Emphasise our absolute best result rather than derived ratios (e.g., highest success, not "retention ratio").
  Prefer words over numbers for what a figure already shows, but keep every number that no figure shows (e.g., an
  absolute return when the figure plots only gains, a baseline absent from the plot, failure counts). Never compress
  those away (user 2026-10-31).
- **Ablations** open with one paragraph grouping the ablations and pointing to figures, then one bold run-in
  paragraph per factor. Relate findings to prior work with citations where they agree.
- **Captions** open with a bold title that names only what is tested, not the result
  (`\caption{\textbf{Learning efficiency in imitation learning.} Details ...}`, user 2026-10-14), then describe
  panels with `\textbf{(A)}`. Each figure gets a distinct title. The takeaway goes in the text, not the title.
- **Every subsection opens with a transition** that says what this part does ("We next examine how fast ..."),
  not with a summary of the result (user 2026-10-17). The takeaway comes at the end of the paragraph.
- **Experiments intro**: numbered questions only for the core claims. Real-robot deployment and ablations are
  stated as sentences ("We then deploy ... and finally ablate ..."), not as questions.
- **Abstract**: short sentences, but keep the connectives (Concretely, Moreover, In experiments, The results show,
  Notably) so it does not read as a list. Experiments named in parallel by role ("as a visuomotor policy, as the
  action head of ..., and as the actor of ..."). Results as one ratio per claim against one named baseline
  (e.g., flow matching), no parenthesised clutter, and say when they are a subset ("Among the results in IL").
  One sentence for RL without numbers is fine.
- **Intro results paragraph** keeps the user's bold key benefits (\textbf{learns remarkably fast}, ...).
- **Paragraph to paragraph**: end a paragraph with the requirement the next one fulfils, then open the next with
  "To this end" rather than restating it.
- **Epigraph** (optional, Introduction): right-aligned, italic Latin, small ink-colored translation in parentheses,
  then "--- \textsc{Name}, year".
- **Discussion** is open and suggestive, not a to-do list. Frame items as possibilities the method opens
  ("This hints that ...", "might even ...", "natural to express with ... but hard with ..."), never
  "is left for future work" or "we will".

## 3b. Adding an experiment

A new task (e.g., a further real-robot task) touches every place where the tasks are listed, not only a new
paragraph. Check the Setup list of tasks, the subsection opening sentence, a bold run-in results paragraph with
figure, the evaluation protocol sentence (trials, epochs), and the appendix details (demonstrations, cameras).
Ask for trials, epochs, and the number of demonstrations if they are missing, and leave Intro, abstract, and
Discussion to the user.

## 4. TODOs

- `\TODO{}` lives in the .tex prose, never inside generated `tables/*.tex` or figure files.
  A TODO about a figure goes inside that figure's caption.
- Placeholder data in a figure (e.g., std before seeds finish) only when the user asks, always flagged by a caption TODO.

## 4b. Appendix

- Appendix figures and tables are numbered S1, S2, ... (reset counters after `\appendix`, set `\theHfigure`).
- No appendix table that only repeats the numbers of a main-text figure. Move such tables to a standalone
  `tables_removed.tex` (kept, not input) and drop "Numbers are listed in Table ..." from captions.
- Every appendix subsection has at least a few sentences of text, never a bare table or figure.
- A short contents list at the start of the appendix, numbers and pages from `\ref*`/`\pageref*`.
- Fairness tables list what differs in the method, not infrastructure that invites misreading (GPU count, batch,
  steps per epoch). State fairness in one clause instead ("each epoch is one pass over the same data").

## 5. Bibliography

- Reuse existing keys; grep before adding. New entries go at the end in the same style.
- Uniform format: all conferences "Proceedings of the ..." without edition numbers (no "9th"), all journals one
  style. No `doi` and no `url` fields, except for web-only sources such as blog posts.
- Do not cite a framework or tool to support a claim it does not make (e.g., Orbit for RL sample cost).
- Flag arXiv IDs, venues, and years that cannot be verified (recent preprints, future venues) for manual checking.
- **Any entry written from memory must be flagged to the user for checking**, listing the keys.
  Also append it to `notes/bib_to_check.md` in the paper repo (key, entry as written, where it is cited, what to
  verify, a checkbox), so the user can check all of them later (user, 2026-10-31).

## 6. Figures

Follow `references/figures.md` and reuse `assets/style.py` (copy into the paper's `plots/`). Key rules:
ink `#44546A` instead of black, Arial, full-width figures exactly 6.5 in via `fit_width(fig)`,
blue-green ramp with ours darkest, lines alpha 0.65 / bands alpha 0.2, open frame, bold panel titles,
text never overlapping curves. Render to PNG and look at it before pushing.
Figures go `[!tbp]` and close to their first reference (raise `topnumber`, `topfraction`); Fig. 1 goes `[t]`
at the top of page 2, never above the abstract. Section numbers, links, and caption labels use the figure blue.

## 6b. Project website

The project page has its own skill in `website/SKILL.md` (linked as `~/.claude/skills/project-website`).

## 7. Iterating on this skill

When the user gives a correction that is a standing preference (not specific to one sentence), add it to the
right section here (or the reference file) with a one-line reason, and tell the user the skill was updated.
Paper-specific facts (method details, result numbers, notation) belong in that project's CLAUDE.md, not here.
