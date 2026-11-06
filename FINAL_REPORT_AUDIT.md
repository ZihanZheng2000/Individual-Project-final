# Final Report Audit — 2026-11-05

Scope: current `main/jdf-starter.tex`, 13 graded sections as mapped by the repository README, supporting source files, and independently recomputed final-evaluation data from the uploaded 20-response Microsoft Forms CSV. This is a **source-level audit**, not a successful PDF compilation or an independent review of the official Canvas rubric.

## Section-by-section audit

| No. | Section | Evidence present | Remaining issue / assessment |
|---:|---|---|---|
| 1 | Introduction | Clear Outlook email mistake/recovery task and three-stage scope | **Updated:** qualified cross-provider recall experience and cited Microsoft limitations. |
| 2 | Needfinding Plan | 18-person survey and 4-task, 3-heuristic inspection | **Open:** exact survey dates/channels; heuristic test date, OS, account mapping and settings not fully documented. |
| 3 | Needfinding Results | Counts by type, recovery distributions, heuristic observations, 3 evidence-based insights | **Updated:** Nielsen/Microsoft citations and provisional T4 severity. Source records for initial study not rechecked in this audit. |
| 4 | Initial Brainstorming Plan | Divergent/convergent activity, AI role and bias mitigation | No major structural gap; planning versus retrospective tense can be editorially tightened. |
| 5 | Brainstorming Results | Multiple candidates, rationale, 3 textual designs | **Open:** Appendix C is an explicitly paraphrased reconstruction, not a verbatim original transcript; ensure rubric permits this. |
| 6 | Initial Prototyping | A/B/C mockups, explanations, figures and supplementary PDF screens | **Open:** visually confirm page-numbered PDF assets and captions in compiled output. |
| 7 | Evaluation Planning | First-round recruitment, scenario questions, Likert measures, Friedman plan | Present and appropriately framed. |
| 8 | Evaluation Results | 7 participants, scenario answers, ratings, Friedman test, limited comments | Internal narrative and appendix agree; raw original survey export unavailable here for independent recalculation. |
| 9 | Second Iteration Planning | Evidence-driven integration of A/B/C, explicit removal of old 5-minute recall rule | Present; limitations of changing recall rule already acknowledged. |
| 10 | Final Prototype | Interactive HTML, screenshots, implementation logic, limitations | **Open:** external public GitHub Pages accessibility and screenshot privacy not independently confirmed. |
| 11 | Video Prototype | Narrated-demo description and SharePoint link | **Open / critical:** demonstrate viewer permissions and duration; link has not been independently playable through this audit. |
| 12 | Final Evaluation Planning | Separate final survey, methods and analysis plan | Present; procedure allows video-only participants; results report this exposure difference. |
| 13 | Final Evaluation Results | All 20 survey records; counts, means, medians, preferences and qualitative feedback | **Verified:** figures recomputed against source CSV. The data measure responses/perceptions, not observed task success. |

## Cross-cutting findings, highest priority first

### Critical before submission
1. **PDF compilation and page cap:** Compile in Overleaf with the bundled JDF class, inspect figure pages, and verify body text is at most 25 pages excluding references and appendices. Not established by a source-only inspection.
2. **Video access:** Test the OneDrive/SharePoint URL from a permitted Georgia Tech account other than the owner's, verify playback, narrated content, and approximate five-minute duration.
3. **Heuristic screenshot privacy:** Inspect both Outlook recall screenshots for real names, addresses, and other identifiers. Blur/redact as needed; textual descriptions are not proof that embedded image pixels are safe.
4. **Rubric and transcript:** If the official assignment requires a full AI conversation transcript rather than an explicit paraphrase, replace Appendix C with a genuine transcript or faithful translation, not an invented conversation.

### Important evidence/documentation gaps
5. The initial needfinding and heuristic inspection have incomplete dates and environment metadata. Do not invent them.
6. The original round-one evaluation is internally consistent but its original row-level export was not available during this audit. Existing appendices provide aggregates rather than respondent-level raw records; check the official raw-data requirement.
7. The 20-person final evaluation similarly provides de-identified aggregate tables, not public respondent-level raw data; retain original identifiable CSV privately. If raw responses are specifically required, prepare a privacy-safe export without identities, timestamp or sensitive free text.
8. Confirm prototype hosting access and check all large illustrations at actual PDF scale. Source filenames referenced by LaTeX exist in GitHub, but graphics rendering was not compiled or visually inspected.
9. Verify linked course readings and any genuinely borrowed graphics/assets are credited. Nielsen and Microsoft sources have now been cited; no additional source was added without direct evidence of use.

### Resolved in GitHub during this audit
- Replaced empty References placeholder with Nielsen Norman Group and Microsoft Support bibliography entries plus in-text citations.
- Changed overly certain statements about external Gmail Recall, account roles, and severity-4 inspection into evidence-bounded descriptions.
- Removed the opening 'working draft' disclaimer and duplicate bibliography section heading.
- Replaced generic TODO notices with explicit documentation gaps and a submission-time checklist.
- Renamed the final survey appendix from 'Raw Results' to 'Aggregate Results' to avoid implying individual responses are included.
- Checked LaTeX environment begin/end counts and reference/citation keys at source level; no unmatched labels or undefined citations found.
- Verified the final survey: 20 participants (8 prototype only, 7 both, 5 video only); comprehension 18/20, 15/20, 12/20; means 4.45/4.30/4.50/4.45/4.30; positive ratings 18/19/19/18/18; choices 8/5/4/3; open responses 15 rationales and 5 improvements.

## Required final handoff

Synchronize `jdf-starter.tex` and any changed assets with Overleaf; compile; independently review body-page count, visual figures, bibliography, video and prototype access; then submit the compiled PDF and Overleaf edit-share URL as the course instructions require. Do not treat this audit as proof the PDF is submission-ready.

## 2026-11-05 second pass: exact assignment rubric and length audit

The original CS 6750 Individual Project assignment text supplied in the user's earlier materials was retrieved and checked against every graded question, rather than relying only on the repository README. It specifies 13 graded sections totaling 100 points, a **25-page maximum for the body** (references/appendices excluded), Overleaf JDF composition, one PDF and an Overleaf **edit-share** link. The suggested lengths below are recommendations, not enforced section caps.

| # | Rubric item | Pts | Suggested pages | Current body words* | Requirement-by-requirement judgment |
|---:|---|---:|---:|---:|---|
| 1 | Introduction | 5 | ~1 | 253 | Task, user goals and motivating vignette provided; expanded scenario and task scope. |
| 2 | Needfinding Plan | 5 | ~1 | 413 | Two activities (18-person survey and single-evaluator inspection) and 3 explicitly named heuristics; exact historical collection dates and conditions not established. |
| 3 | Needfinding Results | 5 | ~2 | 839 | Survey counts, heuristic behavior for T1–T4, three justified insights; Appendix A summary and Appendix B notes. |
| 4 | Initial Brainstorming Plan | 5 | ~0.5 | 214 | Individual AI-assisted divergent/convergent plan, rationale, anchoring mitigation; Appendix C contains a clearly labelled edited reconstruction, not certified verbatim chat. |
| 5 | Brainstorming Results | 5 | ~1.5 | 506 | Alternatives, selection rationale for A/B/C, three textual prototypes; Appendix C process notes. |
| 6 | Initial Prototyping | 10 | ~3 | 458 | Three low-fidelity visual prototypes and design rationale, with full screens in Appendix D; PDF display must still be compiled/verified. |
| 7 | Evaluation Planning | 5 | ~1 | 415 | Participant procedure, quantitative + qualitative measures, Friedman test and thematic analysis plan; survey in Appendix E. |
| 8 | Evaluation Results | 10 | ~2 | 435 | N=7, scenario correctness, full Likert distributions, Friedman p=0.472 and interpretive comments; Appendix F. Original participant-level export not independently rechecked in second pass. |
| 9 | Second Iteration Planning | 5 | ~2 | 483 | Evaluation-based new needs, explicit integration and design refinement; no dedicated new needfinding claimed. |
| 10 | Final Prototype | 15 | ~3 | 663 | Medium-fidelity interactive MailFlow simulation, multiple figures, design rationale and scenario mechanics; Appendix G. |
| 11 | Video Prototype | 15 | ~0.5 | 141 | Narrated-demo description, link and access instructions. **Must verify playable link, permissions, voice walkthrough and about-five-minute duration.** |
| 12 | Final Evaluation Planning | 5 | ~1 | 306 | N≈20 target, exposure procedure, 3 scenario checks, 5 Likert items, preference and optional open responses, analysis plan. Appendix H. |
| 13 | Final Evaluation Results | 10 | ~1.5 | 574 | N=20, exposure, answer counts, Likert means/medians, preferences, qualitative themes, limitations; Appendix I. All numerical response counts rechecked against the uploaded CSV. |

*Words are approximate source-text counts, with basic LaTeX markup stripped. They are **not** actual PDF page counts. Current body totals **about 5,700 words**, contains **6 figure environments** (including 3 low-fidelity PDF figures), **3 external TeX graphics inputs**, and **4 explicit page breaks**. Reference and appendix text is excluded. With diagrams and JDF layout, a page estimate is unreliable: **the ≤25-page requirement is not yet verified**. Compile in Overleaf and inspect page number immediately before the automatically generated bibliography; avoid removing substantive evidence merely to approach a page target.

### Specific upgrades performed in second pass
- Added a concrete, task-focused email mistake vignette to the short Introduction.
- Added **four additional independently checked HCI references**: Moran & Gordon (2023) on heuristic inspection; Norman (2013) on discoverability and feedback; ISO 9241-210:2019 on iterative human-centred design; Nielsen (1993) on response-time feedback. Total is now six bibliography entries, all cited in the body; no unused keys.
- Integrated these references at points where they support actual methodological choices or prototype design rather than appending unrelated literature.
- Rechecked the uploaded 20-row final survey (Windows-1252 CSV): exposure 8/7/5; expected scenario choices 18/15/12; five Likert positive counts 18/19/19/18/18; feature choices 8/5/4/3; 15 preference explanations and 5 improvement responses. Identifiers remain private.
- Source checks after changes: all 13 body sections present; **zero literal TODO markers**, **zero undefined citation references**, **zero undefined cross-references**. A clean Overleaf compilation, final pagination and screenshot pixel-level review still remain.

### Source integrity note on AI brainstorming
The rubric explicitly asks for the transcript when AI-assisted brainstorming is used. Appendix C presently contains an **edited, reconstructed exchange clearly disclosed as such**. It can document substantive decision-making but is not a verbatim original; describing it as one would be inaccurate. If graders require the complete original interaction, attach the authentic transcript or faithful translation. This is the main content-completeness risk that cannot be truthfully resolved by editing existing reconstructed text.
