# Materials and Methods: established writing standard

## Purpose and shape

Write reproducible, compact descriptions in authentic experimental order:

`subjects/models → grouping or treatment → major steps → key parameters → measurement/readout → analysis`.

- Usually use past tense and natural passive voice. Write ordinary methods as coherent paragraphs, not numbered bench-protocol instructions, unless a protocol is requested.
- Start directly with `Cells were seeded...`, `Tissue sections were incubated...`, `The supernatant was collected...`; avoid repetitive `Briefly,`, `To evaluate...`, `To determine...`.
- Use the shortest complete explanation, not an arbitrary word quota. Simple methods often need only a few sentences; complex procedures need enough detail for reproducibility.
- Keep authentic cell line, cell number, volume, concentration, temperature, time, optics, imaging or absorbance wavelength, measurement software, controls, and statistical readout.
- Use exact supplier product names. Do not call an alternative basement membrane matrix product `Matrigel` unless its actual manufacturer/product name supports it.
- Clearly distinguish observed conditions from illustrative/reference-protocol settings. A source article's method is a **reference**, not automatically the user's method.

## Information placement: two distinct profiles

1. **TPH@Pd-TTF materials/nanomedicine manuscript:** Manufacturer, catalog number, instrument brand/model go in a centralized Materials and Instrumentation section if the paper follows that structure. Do not mechanically repeat them in every experimental subsection; retain essential method conditions and readout.
2. **ABBS cell/molecular biology manuscript:** Retain relevant first-mention antibody catalog numbers, reagent manufacturer and instrument model when useful for reproducibility, as required by the actual manuscript/journal; avoid repeated duplicative manufacturer information.

Do not universalize one profile to the other.

## Coverage and source checks

For every result panel, confirm the matching method exists. Separate or clearly distinguish:

- Clinical biospecimens, IHC, WB, cell culture, lentiviral stable knockdown, transient siRNA and plasmid transfection.
- Growth curves, colony formation, EdU incorporation, MTT, wound healing, Transwell migration/invasion.
- Conditioned-medium preparation, HUVEC migration/tube formation, **direct HUVEC knockdown** as its own setup.
- RhoA-GTP pull-down, immunofluorescence localization, qRT-PCR, promoter reporter luciferase, ChIP-qPCR.
- Subcutaneous xenograft vs tail-vein experimental pulmonary colonization; mouse tissue H&E/IF; statistical analysis.

For each assay, include only real parameters and note omitted ones needing validation (e.g., WB membrane type/blocking composition, ChIP crosslinking/shearing, wound healing mitomycin-C concentration, transfection reagent, luciferase normalization, paired clinical statistics).

## Common experimental distinctions

- **Western blotting:** cell vs tissue extraction; RIPA; BCA; SDS-PAGE; NC/PVDF; blocking reagent/time; primary dilution/incubation; post-primary washes; secondary ID/duration; post-secondary washes; detection and ImageJ normalization. Do not infer blocking buffer from a primary antibody diluent.
- **IHC:** fixation, 4 µm if stated, deparaffinization, peroxidase block, antigen retrieval, blocking, primary/secondary conditions, detection system, counterstain. Clarify whether `Dako EnVision` is itself the secondary detection system—do not invent a second layer.
- **H&E/IF:** actual PFA fix time, thickness, antigen retrieval if used, incubation temps/times and staining/mounting/readout.
- **MTT:** verify seeding density, 5 mg/mL or actual stock, dispensed µL, incubation time, DMSO volume, readout wavelength, reader model, background correction. Standard sample settings are not user data.
- **Tube formation:** collect matched HCT116 control/knockdown conditioned medium and centrifuge if done; plate coating matrix name/volumes/polymerization; HUVEC count; treatment; observation time; nodes/loops/branch length as actually counted. Direct gene knockdown in HUVECs is a distinct experiment.
- **Luciferase:** ensure cell line (e.g., COS-7 when supplied), promoter construct coordinates, plasmids, transfection, control vectors, kit/read time, normalization. A *firefly-only* assay must not be described as dual-luciferase or imply Renilla co-transfection.
- **ChIP-qPCR:** anti-target antibody vs IgG, input normalization where used, crosslink/sonication conditions, promoter region, enriched vs physical single-base binding inference.
- **Statistical methods:** paired surgical tissues are paired observations; do not default automatically to unpaired t-test. Specify method actually applied or flag `TO VERIFY`.
- **Cell culture:** exact cell line media and atmosphere require records; supplier-recommended conditions must not replace actual study conditions. Confirm unique catalog/number formatting.

## English model (illustrative wording only)

`Cells were seeded in six-well plates and incubated overnight. Following the indicated treatment, cell lysates were collected and analyzed by western blotting. Protein band intensities were quantified using ImageJ software.`

This is a style example, not a complete protocol. Never insert its unprovided details into the user's paper.
