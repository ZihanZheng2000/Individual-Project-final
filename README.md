# CS6750 Individual Project — Full Report Draft (Canonical Repository)

**Project:** Safer Email Sending and Recovery  
**Current status:** All **13 graded sections** and **9 appendices** are present; the interactive MailFlow prototype, video, two evaluation rounds (N=7 and N=20), and bibliography are documented. The latest JDF PDF build succeeds with the body ending on page 24 (39 pages including references and appendices). **Overleaf sync, links and final PDF review remain necessary before Canvas submission.**

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

**Appendices:** survey aggregate results; heuristic observations; reconstructed brainstorming notes; initial prototype screens; first evaluation script; first evaluation aggregate results; medium-fidelity screens; final evaluation questions; final evaluation aggregate results.

## Mandatory submission requirements
- **Deadline:** November 9, 2026, 9:00 AM.
- **Max 25 pages of body text** (references and appendices excluded).
- Compose and compile in **Overleaf with the JDF class**, submit **one PDF** to Canvas, and provide an **Overleaf edit-share link in the submission comment**. A GitHub link does not replace this.
- External videos/prototypes must be accessible to anyone with a Georgia Tech account.
- Cite sources and quotes, and use only genuine study observations. Explicit documentation gaps are described in the report and audit.

## Highest-priority remaining submission checks
1. Synchronize with Overleaf, compile there, and visually inspect figures and page count. A GitHub Actions JDF build already measured the body ending on page 24; see the latest workflow runs after edits.
2. Verify narrated video access from a Georgia Tech grader account and verify its duration.
3. Review the final PDF screenshot overlays: the first Outlook screenshot's incidental personal-name text is masked in LaTeX, but the original repository image remains unchanged.
4. The official rubric asks for an AI brainstorming transcript; Appendix C is an openly disclosed edited reconstruction, not a certified verbatim record. The rubric permits directly summarized survey data; appendices include aggregates.
5. Confirm original needfinding dates and heuristic-evaluation environment only when supported by original evidence.
6. Submit one compiled PDF and the Overleaf edit-share link via Canvas.

The report intentionally distinguishes existing counts (18 survey responses, with 15 forgotten-attachment and 10 wrong-recipient reports) from unverified or still-unperformed study results.

## Repository transition
This is the canonical repository for future project edits. The prior `Individual-Project` repository remains an archival reference. The final report draft was migrated from its main branch and references the two Recall images already present in this repository. Confirm image privacy before public submission.

## Final prototype and video (Nov 2026)
- MailFlow V4 is an interactive HTML prototype with four preset drafts, contextual missing-attachment/sensitive-visa-attachment/wrong-recipient warnings, configurable 10/30/60-second Undo Send, Send Now, and conditional Recall.
- Direct Recall is available when the recipient has not opened the message, regardless of elapsed time. Opened messages require simulated recipient approval. This is a proposed design, not an actual email-service guarantee.
- Narrated video: https://gtvault-my.sharepoint.com/:v:/g/personal/zzheng399_gatech_edu/IQCoDjijGlvxSLOoSAevYqpdAXLGodNvVcylA2DDLUJvwW8
- The report's Section 10 (Final Prototype), Section 11 (Video Prototype), Section 12 (Final Evaluation Planning), and Appendices G/H have been updated. Video access permissions and public-prototype hosting still require independent verification; final evaluation results have now been added.

## Hosting the interactive prototype
- This report repository is private; the separate `mailflow_prototype` repository exists and is public.
- Interactive site: https://zihanzheng2000.github.io/mailflow_prototype/ . A reviewer should verify its current accessibility before grading; the repository's visibility is not sufficient to prove GitHub Pages is served.
- The original private Outlook screenshots include source evidence; personal-name overlays in the LaTeX output are intended to protect the final PDF.

## Public MailFlow prototype repository
- Source: https://github.com/ZihanZheng2000/mailflow_prototype
- GitHub Pages target (requires enabling and verification): https://zihanzheng2000.github.io/mailflow_prototype/
- The repository is public and contains the interactive `index.html`. Pages is not confirmed active yet. Enable via Settings > Pages > Deploy from branch > main / (root), then check the URL without signing in.

## Final evaluation results (November 5, 2026)
- Twenty complete surveys: prototype only 8, video + prototype 7, video only 5.
- Expected-scenario comprehension: Error Detection 18/20 (90%), Undo Send 15/20 (75%), Recall 12/20 (60%).
- Positive (Agree/Strongly agree) ratings: ease of understanding 18/20, control 19/20, usefulness 19/20, warnings 18/20, Undo-vs-Recall clarity 18/20.
- Mean ratings on the 1--5 scale: 4.45, 4.30, 4.50, 4.45, and 4.30 respectively.
- Feature preference: all three equally effective 8, Recall 5, Error Detection 4, Undo Send 3.
- 15 optional feature rationales and 5 improvement comments; the report summarizes recommendations without posting identifying survey data.
- Updated `jdf-starter.tex` Section 13 and the Final Evaluation Raw Results and Statistics appendix. Do not upload the original CSV to the public repository: it contains participant names and emails.

## Source-level Final Report Audit (November 5, 2026)
The latest `jdf-starter.tex` includes a bibliography with primary Nielsen Norman Group and Microsoft Support sources. Report screenshots are grouped under `Figures/final/`, `Figures/lowfi/`, and `Figures/needfinding/`.

## Build and references verification
- `references.bib` contains six cited HCI and product-documentation references, rendered through the bundled JDF class's `biblatex` configuration.
- `.github/workflows/check-report.yml` builds `jdf-starter.tex`, uploads the PDF as an Actions artifact, and fails if the final body page exceeds 25.
- Latest analyzed PDF: 39 total pages, body end at page 24; build 42271583830.

## PDF layout refinement (November 2026)
- The latest source pairs the Final Prototype before/after screens and Outlook Recall evidence side by side with a shared caption, combines the three recovery states, and avoids forced `\\clearpage` breaks.
- Inline citations are rendered as numbered references matching the JDF bibliography; bibliography URLs remain clickable as compact text (`Online source`), and the report's external URLs use short descriptive links.
- Latest validated PDF has **40 pages total, with the body ending on page 24** (GitHub Actions run 42271583830).

## Expanded analytical content (November 2026)
The report now develops the first-round evaluation's interpretation (including the significance and limitations of its Friedman test), maps observed feedback to second-iteration design decisions, explains the removal of the prototype Recall time limit as an unvalidated design choice, and analyzes the final survey's gap between stated clarity and actual Recall-scenario comprehension. The latest verified JDF build has **39 pages overall with the body ending on page 24**, within the 25-page maximum. See audit and the compiled Actions artifact.

## Submission-clean review (November 6, 2026)
- Removed internal audit and access-verification notes from the report; the report itself no longer contains outstanding TODO markers.
- Recruitment: target email users, particularly those with prior mistaken sends; volunteer outreach via student/personal networks and course survey discussion; no unverified claim of formal screening. All 18 initial-survey respondents reported past send regret. Final evaluation used 20 email-user volunteers without proof that each had made a sending error.
- Latest clean source build (Actions run 42271583830): **39 total PDF pages**, body ends at **page 24**, JDF compilation successful. Removed a redundant appendix limitations sentence that had created an otherwise nearly empty page 40.
- Submission still requires a playable grader-accessible video link, an Overleaf editable project/share link, and Canvas PDF upload.
