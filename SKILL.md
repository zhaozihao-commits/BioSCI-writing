---
name: sci-manuscript-writing
description: Apply the user's established SCI manuscript writing, Methods, Results, Discussion, reviewer-rebuttal, figure-legend, reference, and submission-QA standards. Use when drafting, translating, polishing, revising, or auditing English scientific papers or point-by-point reviewer responses, especially molecular oncology, nanomedicine, or materials research. Do not activate for unrelated general English writing or assume project-specific experimental details without source evidence.
---

# SCI manuscript writing and rebuttal standards

Use this skill for accurate, concise, evidence-calibrated English scientific writing. The user normally discusses edits in Chinese and requests publication-ready English text. Preserve the user's meaning and exact experimental record; do not introduce facts merely to make text look complete.

## Non-negotiable rules

1. **Source of truth:** Use user-provided experiments, data, source files, final figures, supplementary tables, and journal instructions. Never invent concentrations, time points, instruments, reagents, data, statistics, references, controls, or experiments. Mark missing details `待核实` / `TO VERIFY`, or ask a single focused question only if essential and reasonable.
2. **Match strength of claims to evidence:** Distinguish correlation, functional association, rescue, putative mechanism, direct binding, and clinical utility. Computational predictions do not establish experimental binding. A reporter assay shows promoter response; it does not alone establish direct DNA occupancy.
3. **Write directly:** Concise, natural academic English; prefer past tense for completed experiments and results, present tense for established knowledge. Use passive voice appropriately, not mechanically. Avoid repetitive sentence starters such as `Briefly,`, `To evaluate...`, `To investigate...`, and repeated `We...`.
4. **No silent fabrication or correction:** If materials conflict, flag them. Do not claim two siRNAs were used in functional tests when only three candidates were screened and one advanced. Do not infer precise methods from common protocols.
5. **Keep everything cross-consistent:** Experimental group names, Figures, Supplementary Figures, Tables, references, dosage units, cell lines, gene/protein symbols, and descriptions in the rebuttal must match the final manuscript. State what remains unverified.
6. **Honor scope:** If asked to list corrections, report problems with location, severity, exact proposed fix, and evidence; do not silently edit or generate a document. If asked for a paragraph, give a ready-to-paste paragraph, not a long tutorial. Do not change any source file unless requested.

## Select task-specific guidance

Read the relevant reference files; do not load everything by default.

| User request | Read |
| --- | --- |
| Draft/polish experimental protocol or Materials and Methods | `references/methods.md` |
| Results, Discussion, abstract, mechanism, limitations | `references/results-discussion.md` |
| Reviewer response, editor cover letter, second-round revision | `references/reviewer-response.md` |
| Figure captions, gene symbols, abbreviations, references, tables | `references/figures-terminology-references.md` |
| Nanomedicine / MOC / TPH@Pd-TTF or biological ABBS/H1.5 project context | `references/project-profiles.md` |
| Full draft audit, rebuttal–manuscript comparison, final submission | `references/submission-audit.md` |

## Working procedure

1. **Determine source and task.** Identify the journal, manuscript version, section, user-supplied data, and desired output. If a document is attached, inspect the actual document; do not rely on earlier versions or file names as proof of content.
2. **Determine profile.** For TPH@Pd-TTF materials papers use centralized Materials/Instrumentation metadata; for ABBS mechanism manuscripts follow the manuscript's section-by-section vendor/part-number conventions. See `references/project-profiles.md`.
3. **Draft/edit only the requested portion.** Preserve named entities, all actual parameters, biological distinctions, and figure labels. Use precise verbs and scientific hedging proportional to evidence.
4. **Perform cross-checks.** Before answering, verify every added factual claim, reference, figure/table locator, and stated change against provided sources. Mark unverified cross-file items explicitly.
5. **Deliver in the requested format.** For paragraph-writing: English revised prose first, then brief Chinese note only if needed. For audits: ordered issues with `位置 → 问题 → 解决策略 → 优先级` and a concise assessment. Distinguish confirmed errors, likely issues, and items requiring raw records.

### Core scientific evidence boundaries

- `functional association` is **not** `direct physical binding` (e.g., COL6A5–ANTXR1).
- AlphaFold/modeling is hypothesis-generating, not biochemical proof of binding.
- Luciferase reporter experiments reveal promoter activity, not necessarily direct binding of MRTF-A to one precise CArG motif; ChIP-qPCR reports enrichment within a region.
- A secondary predicted CArG site with limited effect in one condition is not proven universally inactive.
- Tail-vein injection chiefly assays experimental lung colonization, not the complete spontaneous-metastasis cascade.
- Conditioned-medium effects on HUVECs are not the same experiment as direct gene knockdown in HUVECs.
- `knockdown` must not be silently changed to `knockout` or `deletion`.

## Optional local consistency scan

For a text or `.docx` draft, Codex may run the read-only helper when a full QA/audit is requested:

```bash
python scripts/manuscript_lint.py /path/to/Manuscript.docx
```

It flags mechanical patterns only; **a clean scan does not mean scientific or citation accuracy**. Always perform a manual evidence and cross-document check.

## Never claim these without evidence

- That references or DOIs have been verified when not checked.
- That image duplication, plagiarism, or statistical issues are absent without analyzing the actual final assets and underlying data.
- That a protocol was executed merely because it was drafted.
- That added experimental details are correct because they are common in the literature.
- That the last uploaded file is the submission-ready final version unless it has been checked.
