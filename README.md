# CS6750 Individual Project — Full Report Draft (Canonical Repository)

**Project:** Safer Email Sending and Recovery  
**Current status:** Working draft with all **13 graded sections** in the exact assignment order, plus **10 appendices**. The medium-fidelity MailFlow HTML prototype and video are now documented in the report. Final evaluation results remain **TODO** until real participant responses are collected; no results are fabricated.

## Files
- `jdf-starter.tex`: the comprehensive final-project draft, replacing the old Check-In 3 document.
- `jdf.cls`: existing JDF class.
- `Figures/prototype_a.tex`, `prototype_b.tex`, `prototype_c.tex`: the three original low-fidelity storyboards used in the draft.

## Requirements mapping
1. Introduction (5)
2. Needfinding Plan (5): participant activity AND three-heuristic existing-interface inspection
3. Needfinding Results (5): survey findings, heuristic observations, at least three insights, raw data
4. Initial Brainstorming Plan (5): rationale, bias mitigation, AI transcript if used
5. Brainstorming Results (5): options, reasons for three selections, textual prototypes
6. Initial Prototyping (10): three low-fidelity designs, at least one image each, design rationale
7. Evaluation Planning (5): participant procedure, quantitative and qualitative measures and analysis
8. Evaluation Results (10): actual participants, statistics/p-values, qualitative analysis
9. Second Iteration Planning (5): evaluation-derived needs and evidence-based design decision
10. Final Prototype (15): real medium-fidelity design, multiple screenshots, rationale
11. Video Prototype (15): ~5-minute narrated demonstration, accessible URL and instructions
12. Final Evaluation Planning (5): separate participant study, quantitative + qualitative instruments
13. Final Evaluation Results (10): actual outcomes and analysis

**Appendices:** survey and raw results; heuristic observations; brainstorming and AI transcript; initial prototype screens; first evaluation script; first evaluation raw data; medium-fidelity screens; final evaluation questions; final evaluation raw data; completion checklist.

## Mandatory submission requirements
- **Deadline:** November 9, 2026, 9:00 AM.
- **Max 25 pages of body text** (references and appendices excluded).
- Compose and compile in **Overleaf with the JDF class**, submit **one PDF** to Canvas, and provide an **Overleaf edit-share link in the submission comment**. A GitHub link does not replace this.
- External videos/prototypes must be accessible to anyone with a Georgia Tech account.
- Cite sources and quotes, and use only your own genuine study observations; the TODO fields are not submission-ready.

## Highest-priority uncompleted work
1. Execute and document the three-heuristic review of existing Outlook sending/recall behavior.
2. Complete the first participant evaluation and report the preselected Friedman test if sufficient matched data are available.
3. Use first-round results to select/refine the medium-fidelity prototype, then capture screenshots.
4. Record and host the narrated video walkthrough.
5. Complete the separate final evaluation, statistics and qualitative thematic analysis.
6. Restore original full survey data/brainstorming notes in appendices and finish citations.

The report intentionally distinguishes existing counts (18 survey responses, with 15 forgotten-attachment and 10 wrong-recipient reports) from unverified or still-unperformed study results.

## Repository transition
This is the canonical repository for future project edits. The prior `Individual-Project` repository remains an archival reference. The final report draft was migrated from its main branch and references the two Recall images already present in this repository. Confirm image privacy before public submission.

## Final prototype and video (Nov 2026)
- MailFlow V4 is an interactive HTML prototype with four preset drafts, contextual missing-attachment/sensitive-visa-attachment/wrong-recipient warnings, configurable 10/30/60-second Undo Send, Send Now, and conditional Recall.
- Direct Recall is available when the recipient has not opened the message, regardless of elapsed time. Opened messages require simulated recipient approval. This is a proposed design, not an actual email-service guarantee.
- Narrated video: https://gtvault-my.sharepoint.com/:v:/g/personal/zzheng399_gatech_edu/IQCoDjijGlvxSLOoSAevYqpdAXLGodNvVcylA2DDLUJvwW8
- The report's Section 10 (Final Prototype), Section 11 (Video Prototype), Section 12 (Final Evaluation Planning), and Appendices G/H have been updated. Video access permissions, screenshots, HTML hosting, and final evaluation results still require completion.

## Hosting the interactive prototype
The complete MailFlow V4 site is committed as [`index.html`](./index.html). **It is not yet a verified public GitHub Pages site.** This report repository is private. To give survey respondents a direct, no-login interactive link, create a separate **public** repository named `mailflow-prototype`, copy `index.html` to its root, and enable Settings → Pages → Deploy from a branch → `main` / `(root)`. The resulting URL is expected to have the form `https://ZihanZheng2000.github.io/mailflow-prototype/` after GitHub reports successful deployment. Verify in an incognito browser before inserting the URL in the report and survey. Do not make the entire report repository public merely to host the demo.

The six uploaded final-prototype figures are referenced with proper captions and labels in Section 10 and Appendix G. Their LaTeX blocks were moved before `\\end{document}` so they can compile.
