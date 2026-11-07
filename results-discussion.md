# Results, Abstract, Discussion, and scientific-claim calibration

## Results

Present an interpretable result sequence: prior question/context → actual comparison and measured result → exact panel locator → limited interpretation.

- Prefer concrete verbs: `increased`, `decreased`, `attenuated`, `partially restored`, `was associated with`, `supported`, `suggested`.
- Do not imply a completely restored phenotype when only partial rescue is shown.
- An apparent lack of effect is `had a relatively limited effect` or `no appreciable effect under the tested conditions`, **not** proof the site is nonfunctional.
- Describe which group was compared to which and distinguish statistical evidence from visual trend.
- Do not overinterpret cellular viability as exclusively apoptosis, or decreased MTT as necessarily reduced cell number, without corroboration.
- Use `Fig. 1A`, `Fig. S1A`, `Fig. 6D and 6G` precisely.
- Avoid repeating the same mechanistic summary every paragraph.

## Abstract

Summarize only demonstrated results and their significance. Do not present unverified binding or an inferred regulatory circuit as an established physical mechanism. If a study supports only partial mechanistic validation, prefer `support a potential positive regulatory feedback mechanism` over `established a definitive feedback loop`.

## Discussion

Use context → major evidence → mechanistic interpretation → alternative explanations and boundaries → limitations → justified implications. Keep limitations concise but explicit; do not hide them in a footnote.

Evidence hierarchy:

| Supported experiment | Safe interpretation | Unsafe upgrade |
| --- | --- | --- |
| Differential expression / cohort association | `associated with prognosis` | `causes poor prognosis` |
| Knockdown / overexpression / rescue | `supports a functional association` | `proves direct receptor–ligand binding` |
| AlphaFold or docking | `predicted/putative interaction` | `validated physical binding` |
| Reporter promoter mutations | `predominant responsive motif under tested conditions` | `the only binding site` |
| ChIP-qPCR | `enrichment at the promoter region` | `direct binding to the exact base pair` |
| Tail-vein injection | `experimental pulmonary colonization` | `entire spontaneous metastatic cascade` |
| Conditioned medium altering HUVECs | `tumor-secretome-associated endothelial response` | `the secreted COL6A5 protein alone caused the response` |
| Three matched clinical patients | `in-house expression validation, n = 3` | `fully generalizable clinical validation` |

When a CArG promoter has two candidates in each gene, state both single-site and double-mutant evidence. A predominant COL6A5 P1 / ANTXR1 P2 response does not mean the other sites cannot be context-dependent.

For direct-binding caveats, acknowledge the need for biochemical assays such as Co-IP, GST pull-down, recombinant protein domain binding assays. Discuss full-length ECM protein solubility and transmembrane receptor detergent requirements without using technical difficulty as proof of binding or as proof of impossibility. Molecular masses (e.g., `288 kDa`) must be verified for the particular isoform before inclusion.

Animal limitations: Athymic nude mice lack functional T cells and do not reproduce intact human immune context; avoid `failing to recapitulate authentic tumor growth`. Tail vein experiments skip primary invasion and intravasation steps.

## Examples of appropriately cautious phrasing

- `These findings support a functional association between COL6A5 and ANTXR1 rather than establishing their direct physical interaction.`
- `The results suggest that the remaining predicted sites made relatively limited contributions under the experimental conditions examined; context-dependent functions cannot be excluded.`
- `These findings support a potential positive regulatory feedback mechanism involving COL6A5, ANTXR1, and RhoA/MRTF-A signaling.`
- `Further investigations using appropriately optimized biochemical approaches are warranted to determine whether the proteins interact directly.`
