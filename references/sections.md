# Section templates (from the ODE Policy paper)

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
on LIBERO ... \textbf{(a)} ... \textbf{(b)} ... \TODO{replace placeholder std after seeds 0 and 1}}
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
