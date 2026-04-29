# CLAUDE.md — Project Guide for exam-quizzer

## Project Overview
A zero-dependency, mobile-friendly multi-select quiz web app for ML4T (Machine Learning for Trading) exam preparation. Vanilla HTML + CSS + JavaScript — no framework, no build step.

## File Structure
```
index.html              # Single-page app (3 screens: home, quiz, results)
css/style.css           # Mobile-first responsive styles
js/app.js               # Quiz engine, UI rendering, scoring
js/exam1.json           # Exam 1 bank (141 questions, 12 topics — intro ML4T)
js/exam2.json           # Exam 2 bank (154 questions, 17 topics — advanced ML4T)
resources/              # Source materials (gitignored, not deployed)
```

## Running Locally
```bash
python -m http.server 8080
# Open http://localhost:8080
```
Any static file server works (VS Code Live Server, `npx serve`, etc.). The app uses `fetch()` to load the selected exam's JSON, so opening index.html directly via `file://` will fail due to CORS.

## Exam Selection
The home screen has an "Exam" radio group (`exam1` / `exam2`). Changing the selection re-fetches `js/${examId}.json` and rebuilds the topic checkboxes and question counts. See [js/app.js:33](js/app.js#L33) for the fetch logic and [js/app.js:64-66](js/app.js#L64-L66) for the listener.

## Question Bank Rules
- Every question has exactly **5 options** (a–e)
- Each question has **1–4 correct answers** (never 0, never 5)
- Schema per question:
  ```json
  { "id": 1, "topic": "...", "difficulty": "easy|medium|hard",
    "question": "...", "options": [{"id": "a", "text": "..."}, ...],
    "correctAnswers": ["a", "c"], "explanation": "..." }
  ```
- Optional `scenario` field (Exam 1 scenario-type questions) and `type: "scenario"` flag trigger a different hint text in the UI.

## Valid Topics

**Exam 1** (`js/exam1.json`): stock-data, portfolio-stats, market-mechanics, hedge-funds, valuation, technical-analysis, regression, decision-trees, ensemble-methods, overfitting, ml-finance, projects

**Exam 2** (`js/exam2.json`): reinforcement-learning, q-learning, dyna-q, rl-trading, emh, fundamental-law, portfolio-optimization, market-simulator, time-series-ta, data-handling, deep-learning, generative-ai, algorithmic-bias, options, quant-practice, ml-execution, ai-infrastructure

Each exam's `metadata.topics` array holds the canonical id → display-name mapping — [js/app.js:38-40](js/app.js#L38-L40) populates `topicMeta` from it.

## Scoring
Two scores are computed and displayed:
- **Option Accuracy (primary)** — 1 point per option that the user's mark matches correctness (selected & correct, OR unselected & incorrect), out of 5 per question. This is the headline metric on the results screen.
- **Full-question correct (secondary)** — 1 point only when the selected set exactly equals the correct set (strict grading).

Both metrics are shown at the overall level and per-topic. Per-topic rows are sorted by option accuracy ascending so weak topics surface first. See [js/app.js:302-320](js/app.js#L302-L320) for grading and [js/app.js:346-357](js/app.js#L346-L357) for the overall-score rendering.

Per-option feedback colors are always shown after submission (green = correct & selected, red = incorrect & selected, amber = correct & missed).

## Coding Conventions
- No external dependencies — everything is vanilla JS/CSS/HTML
- Mobile-first CSS with media queries at 768px and 1024px
- CSS custom properties for theming (defined in `:root` of style.css)
- State managed via a plain `state` object in app.js
- All DOM rendering done through template literals and innerHTML