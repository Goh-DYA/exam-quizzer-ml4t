# ML4T Exam Prep Quizzer

Multi-select quizzes for GaTech CS7646 ML4T (Machine Learning for Trading) exam preparation.

## Features

- **Two exam banks** — Exam 1 (141 questions, 12 topics) and Exam 2 (154 questions, 17 topics) — swappable from the home screen
- **295 total questions** covering the full ML4T syllabus from intro stock mechanics through reinforcement learning, deep learning, generative AI, and algorithmic bias
- **Quiz modes** — All Questions, Random 20, Random 40, or filter By Topic
- **Per-option scoring** — 1 point per correctly-marked option (primary metric) plus strict full-question score (secondary)
- **Instant feedback** — per-option color coding (correct / incorrect / missed) with explanations
- **Results dashboard** — overall option-accuracy + per-topic breakdown with review mode
- **Mobile-friendly** — responsive design with touch-sized targets

All questions & responses were generated with Claude Sonnet 4.6, taking reference from course notes & textbook material.

## Getting Started

Serve the project with any static file server:

```bash
# Python (built-in)
python -m http.server 8080

# Alternatively, use Node.js (npx)
npx serve .

# Alternatively, with VS Code
# Install "Live Server" extension → right-click index.html → Open with Live Server
```

Then open [http://localhost:8080](http://localhost:8080) in your browser.

> **Note:** Opening `index.html` directly via `file://` won't work because the app uses `fetch()` to load the question banks.

## Exam 1 — Intro ML4T (141 questions)

| Topic | Count |
|-------|------:|
| Stock Data & Pandas | 10 |
| Portfolio Statistics & Sharpe Ratio | 11 |
| Market Mechanics & Order Types | 12 |
| Hedge Funds & Fund Types | 12 |
| Company Valuation & CAPM | 14 |
| Technical Analysis & Indicators | 12 |
| Regression (Linear, KNN) | 12 |
| Decision Trees & Construction | 14 |
| Ensemble Methods (Bagging, Boosting, RF) | 12 |
| Overfitting & Bias-Variance | 10 |
| ML in Finance | 10 |
| Projects (Martingale, Learners) | 12 |

## Exam 2 — Advanced ML4T (154 questions)

| Topic | Count |
|-------|------:|
| RL Fundamentals (MDPs, Policy, Value) | 10 |
| Q-Learning | 10 |
| Dyna-Q (Model-Based Planning) | 6 |
| RL Applied to Trading | 9 |
| Efficient Markets Hypothesis | 8 |
| Grinold's Fundamental Law | 7 |
| MVO & Efficient Frontier | 8 |
| Market Simulator & Backtesting | 9 |
| Time Series & TA Indicators | 8 |
| Data Handling (Splits, Dividends, Survivor Bias) | 9 |
| Deep Learning (NNs, CNNs, RNNs) | 10 |
| Generative AI & Transformers | 12 |
| Algorithmic Bias & Fairness | 12 |
| Options & Derivatives | 12 |
| Quantitative Practice (Kamel Interview) | 10 |
| ML for Execution (Microstructure) | 5 |
| AI Infrastructure in Investments | 9 |


## Scoring

Each question has exactly 5 options (a–e) and 1–4 correct answers. Two scores are computed:

- **Option Accuracy** (primary) — 1 point per option that the user correctly marked or correctly left unmarked, out of 5 per question
- **Full-question correct** (secondary) — 1 point only when the user selects exactly the correct set

The results screen shows both scores at the overall and per-topic level.

## CSV Export

A standalone Python script exports all questions from both exam banks into a single CSV file for offline review:

```bash
python export_qns.py
```

This produces `questions_export.csv` in the project root with columns: Exam, Topic, Difficulty, Question, Options, Correct Answers, Explanation, Source. 

## Tech Stack

Vanilla HTML + CSS + JavaScript — zero dependencies, no build step.