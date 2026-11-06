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
