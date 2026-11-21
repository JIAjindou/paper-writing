# Section templates (from the ODE Policy and PolicyPilot papers)

## Naming (title and method name)

The user's names (jiajindou.com): ADAPT, APEX, MOSS, FLASH, MARS, TOPS, EVOLVER, FORESEER, ODE Policy, PolicyPilot.
Two patterns are fine. One is an all-caps real word whose letters come from the subtitle (MOSS = Mode-Oriented
Source Shaping, APEX = Adaptive Policy EXecution). The other is a CamelCase compound in the style of BeyondMimic
(PolicyPilot). Title shape is "Name: <what it does> for <domain>" or "Name: <short claim>", with no abbreviation
after the colon (no "MPC" in the title).

Process used for PolicyPilot (2026-11-19):
1. Read the paper's abstract and method, then propose three or four names in a table with meaning, title, and risk.
   Do not pull letters from inside words (the old "ReSTRIDE" took the I from "predIctive").
2. The user refines by feel ("too broad", "not focused"). LocoPilot was too broad, because "Loco" is all of
   locomotion and "Pilot" suggests MPC is in charge. PolicyPilot kept the copilot metaphor and named what is
   assisted. Offer ways to narrow (name the target, name the role, or move the domain into the subtitle).
3. Before editing, check collisions with web searches on arXiv, GitHub, and the field (the exact name, a spaced
   variant, and a "Copilot" variant). Report unrelated products separately from papers in the field.
4. Then change `\papertitle`, the Introduction's "we propose" sentence, and every placeholder such as
   `\textcolor{red}{our method}`. Leave the author's plain "our method" alone unless asked.

## Introduction, last paragraph for a staged submission

```latex
This paper focuses on the formulation of PolicyPilot and its validation on representative disturbance scenarios.
In the second stage, we plan to validate command generalization on hardware, beyond the simulation results
reported here. We further plan an integrated hardware demonstration in which a single deployment encounters
payloads, stairs, and lateral pulling in sequence.
```

## Experiments for a control or hardware paper (PolicyPilot)

Without benchmarks or seeds, the section reads:
- Intro with **(1)–(3)** questions on the core claims (robustness, generalization beyond training, online cost),
  then one sentence for ablations and the real robot.
- `Task Formulation` with the shared prior and one bold run-in per task for its references and extra cost terms.
- `Robustness in Simulation` with bold run-ins Setup / Baselines / Metrics / Results. Each ablation baseline is
  explained by what it removes ("RL+DO ... uses the same estimate without predictive optimization"), and the
  oracle variant is called an upper reference.
- `Hardware Deployment` with the setup, then run-ins Results and Disturbance estimation.
- `Command Generalization` and `Computational Cost`, each opening with a transition sentence.

## Conclusion (one paragraph)

```latex
We presented PolicyPilot, in which MPC acts as a copilot that corrects a frozen RL policy online. A proprioceptive
observer estimates the external wrench, and MPC turns it into contact-force corrections under explicit objectives
and constraints. In simulation and on hardware, PolicyPilot improves robustness to payloads and lateral pulling and
control beyond the training range, without retraining and at $0.541$\,ms per cycle. Next, we plan to verify
command generalization on hardware, ...
```

## Experiments intro

```latex
We evaluate \m{}~policy on four questions. \textbf{(1)} Does it learn faster and from less data than
conventional discrete policies, in both IL and RL? \textbf{(2)} Does it generate actions faster and more
smoothly? \textbf{(3)} Does it generalize robustly to unseen perturbations? \textbf{(4)} Can it represent
multi-modal behavior? Moreover, we ablate each component of \m{}~policy to verify its contribution.
```

Subsections then follow the question order, one subsection per question, ablations last.

## Setup paragraph

```latex
\textbf{{Benchmarks.}} For visuomotor IL, we train one model on the four LIBERO suites (...) jointly~\citep{...},
with 40 tasks and 50 demonstrations per task, and evaluate each suite separately. ...
```

Unfinished items in setup are explicit: `\TODO{VLA baseline}`, `\TODO{seeds}`, `\TODO{real robot}`.

## Results paragraph

```latex
\textbf{{Chunk length.}} We train and execute \m{}~policy with $H$ from 1 to 16
(Fig.~\ref{fig:ablation}(a, b)). Chunking matters. With $H=1$, the policy reaches only 75.0\% at epoch 100
and needs 3.5\,ms per action, since the encoder runs at every step. From $H=4$ on, ... This is consistent
with previous findings that chunking mitigates the compounding errors of behavioral cloning~\citep{...}.
Chunking is therefore essential, and $H=8$ balances success rate and inference time.
```

Shape: setting + figure ref → a short claim → numbers → mechanism → link to prior work → concluding sentence.
Remove side remarks that do not support the paragraph's claim (they can stay in an appendix table).

## Ablation opening

```latex
We ablate the design choices of \m{}~policy one at a time, keeping all other settings fixed. The first
group concerns ..., namely ... (Fig.~\ref{fig:ablation}). The second concerns the components of
Section~\ref{sec:method}, namely ... (Fig.~\ref{fig:ablation2}), as well as ... (Fig.~\ref{fig:ablation_k}).
```

## Caption

```latex
\caption{\textbf{Learning efficiency in imitation learning.} Success rates
on LIBERO ... \textbf{(A)} ... \textbf{(B)} ... \TODO{replace placeholder std after seeds 0 and 1}}
```

## Discussion (open tone)

```latex
Beyond the results above, viewing a policy as a vector field in the physical time of the robot opens uses
that discrete policies do not naturally offer. We share two of them with preliminary experiments, as
starting points rather than finished solutions.
...
This hints that the velocity could be modulated by the phase of a task, e.g., fast in free space and slow
near contact, which is natural to express with a vector field but hard with discrete actions.
```

## Loss with optional term

Mark optional terms in the total objective with `\underbrace{...}_{\text{optional}}` rather than prose caveats.
