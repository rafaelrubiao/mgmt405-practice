# MGMT 405 — Practice Problems

Interactive practice questions for MGMT 405 (Managerial Economics). Each module
has its own page with numeric and multiple-choice questions. Every question
comes with three escalating hints (one more is revealed after each wrong
attempt) and a full step-by-step solution. Progress is saved in the student's
browser; nothing is collected or sent anywhere.

Live site: https://rafaelrubiao.github.io/mgmt405-practice/

## Links for the course calendar

Each module has a stable URL, so the calendar can link week by week:

| Module | Page |
|---|---|
| Overview (all modules) | https://rafaelrubiao.github.io/mgmt405-practice/ |
| Module 1 — Basic Concepts and Economic Principles | https://rafaelrubiao.github.io/mgmt405-practice/module-1.html |
| Module 2 — Demand Analysis | https://rafaelrubiao.github.io/mgmt405-practice/module-2.html |
| Module 3 — Production & Costs | https://rafaelrubiao.github.io/mgmt405-practice/module-3.html |
| Module 4 (Part I) — Competitive Markets and Market Interventions | https://rafaelrubiao.github.io/mgmt405-practice/module-4-part-1.html |
| Module 4 (Part II) — Market Distortions / Externalities | https://rafaelrubiao.github.io/mgmt405-practice/module-4-part-2.html |
| Module 5 — Monopoly and Monopolistic Competition | https://rafaelrubiao.github.io/mgmt405-practice/module-5.html |
| Module 6 — Complex Pricing and Advanced Pricing Strategies | https://rafaelrubiao.github.io/mgmt405-practice/module-6.html |
| Module 7 (Part I) — Oligopoly with Homogenous Goods | https://rafaelrubiao.github.io/mgmt405-practice/module-7-part-1.html |
| Module 7 (Part II) — Oligopoly with Diff. Goods; Game Theory | https://rafaelrubiao.github.io/mgmt405-practice/module-7-part-2.html |
| Module 8 — Auctions | https://rafaelrubiao.github.io/mgmt405-practice/module-8.html |

## How to change the questions

1. Edit `src/practice_questions.py` (open questions and some multiple choice)
   or `src/practice_mcqs.py` (the rest of the multiple choice). The schema is
   documented at the top of `practice_questions.py`.
2. Rebuild the pages:

   ```
   python build_site.py
   ```

   The script validates every question (3 hints, 5 choices, valid answer,
   unique ids) and refuses to build if something is off.
3. Commit and push. GitHub Pages updates the site within a minute or two.

## Layout

- `src/` — the question bank (Python files; this is what you edit)
- `build_site.py` — turns the question bank into the web pages
- `docs/` — the generated site, served by GitHub Pages. Do not edit these
  files by hand; they are overwritten on every build.

## If this repository is transferred to another account

GitHub Pages URLs are tied to the account name, so after a transfer the site
moves to `https://<new-account>.github.io/mgmt405-practice/` and the old links
stop working. Pages may also need to be switched on once in the new account
(Settings → Pages → deploy from branch `main`, folder `/docs`). Update the
calendar links after any transfer.
