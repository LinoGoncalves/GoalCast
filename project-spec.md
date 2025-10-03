# Comprehensive Specification: EPL Prediction Engine with LLM Interpretation

## 🎯 Objectives

* **Python engine** is the canonical source of truth for all statistical modelling, probabilities, simulations, and metrics.
* **LLM layer** consumes structured outputs (JSON/CSV) from Python and generates human‑readable playbooks, rival swing maps, and strategic narratives.
* **Reproducibility and auditability** are guaranteed by keeping all computation in Python, with the LLM acting only as an interpreter.
* **Advanced extensions** : integrate xG, in‑play Markov models, copula score distributions, and optional automated feeds.
* **Data sources** : leverage free EPL stats/news/xG/odds feeds to improve accuracy.

## 🐍 Python Engine (Canonical Source)

### Core Functions

1. **Data ingestion**
   * Fixtures, bookmaker odds, historical results, rival pick history, injuries/rotations.
   * Optional: xG shot‑level data, live in‑play event feeds.
   * Formats: CSV/JSON.
2. **Probability modelling**
   * **Poisson / Dixon–Coles** : Baseline exact score probabilities.
   * **Bayesian hierarchical updating** : Team attack/defence strengths with uncertainty.
   * **xG integration** : Use shot‑based expected goals to refine team strengths and adjust Poisson λ parameters.
   * **Copula scores** : Model joint distribution of home/away goals with flexible correlation structures, improving realism over independent Poisson.
3. **Simulation**
   * Monte Carlo (10,000+ runs) of round outcomes.
   * Leaderboard swing simulations incorporating rival picks and Superbru scoring rules.
   * Overtake probability estimates.
   * **In‑play Markov chain model** : Transition matrix between score states (0–0, 1–0, 1–1, etc.) to update live win probabilities and dynamically adjust valve recommendations.
4. **Metrics & reporting**
   * Accuracy: outcome %, exact %, close %.
   * Probabilistic: Brier score, log loss, calibration curves.
   * Rival‑aware: swing maps, overtake probabilities, rank distributions.
   * Baselines: compare vs bookmaker implied and classical Poisson.
   * **xG calibration:** Compare predicted vs actual xG to refine model fit.
   * **In‑play validation:** Backtest Markov chain predictions against live odds.
5. **Outputs**
   * Structured JSON/CSV files (see API contract).
   * Persist all snapshots for audit, even when using automated feeds.

## 📂 Data Schemas

### Input Files

* **fixtures.csv** : fixture_id, season, round, kickoff_iso, home_team, away_team
* **odds.csv** : fixture_id, odds_home, odds_draw, odds_away, overround
* **results.csv** : fixture_id, home_goals, away_goals, status
* **rival_picks.csv** : round, rival_name, fixture_id, pick_exact, pick_outcome
* **injuries.json** : team, player, status, expected_return
* **xg_events.csv** (optional): fixture_id, team, player, minute, xG_value, shot_outcome
* **inplay_feed.json** (optional): fixture_id, timestamp, score_state, possession, shots, cards

### Output Files (Python → LLM)

* **probs_model.json** : Win/draw/loss + scoreline probabilities (Poisson/DC + xG + copula).
* **sim_leaderboard.json** : Monte Carlo results, overtake probabilities.
* **calibration_report.json** : Accuracy, Brier/log loss, calibration curves.
* **inplay_probs.json** : Live win/draw/loss probabilities by minute, valve update triggers.
* **xg_report.json** : Team attack/defence strengths adjusted by xG.

## 🧠 LLM Layer (Consumer Only)

### Responsibilities

* Interpret outputs (JSON/CSV).
* Generate playbooks (`RXX.md`) with picks, intent labels, KO−15’ rules.
* Translate sim_leaderboard into rival‑aware swing maps.
* Narrate strategy: banker/valve/hedge logic, highlight risks, KO−15’ triggers.
* Guardrails: Never invent probabilities; always anchor to Python outputs.

## 🔗 API Contract (Python → LLM)

* **Mandatory outputs per round:**
  * `probs_model.json`
  * `sim_leaderboard.json`
  * `calibration_report.json`
* **Optional outputs:**
  * `xg_report.json`
  * `inplay_probs.json`
  * `rival_summary.json`
* **Format:** JSON/CSV only, with timestamps and seeds for reproducibility.

## 📊 Reporting

* **Python reports:**
  * Accuracy vs baselines.
  * Calibration plots.
  * Rival swing distributions.
  * xG vs goals calibration.
  * In‑play Markov validation.
* **LLM reports:**
  * Narrative summaries.
  * Markdown playbooks.
  * Rival swing maps.
* **KPIs:**
  * Hold‑lead probability.
  * Valve efficiency (EV gain per valve).
  * Hedge utility (downside risk reduction).
  * Calibration improvement vs bookmaker baseline.
  * xG predictive lift vs raw goals.
  * In‑play accuracy vs live odds.

## 🌐 Free EPL Data Sources

### Stats & Analytics

* SoccerSTATS.com – goal timings, form, head‑to‑head.
* FBref EPL Stats – advanced metrics, xG, shot maps.
* ThePuntersPage EPL Stats – referee stats, betting‑oriented analytics.

### News & Fixtures

* PremierLeague.com – official fixtures, injuries, pressers.
* BBC Sport Football – previews, injury news.
* Sky Sports Football – breaking news, tactical write‑ups.

### xG & Advanced Data

* Understat.com – xG data, shot maps.
* Infogol.net – xG previews, probability distributions.

### Odds & Market

* OddsPortal.com – odds history, line movement.
* Betfair Exchange (free view) – live market sentiment.

### Rivals & Crowd Bias

* **Superbru pool stats** (if available) – pick distributions.
* **Fantasy Premier League (FPL)** – player ownership % as proxy for crowd bias.

## 🏁 Governance

* **Python = canonical truth.**
* **LLM = interpretation only.**
* **Versioning:** All outputs timestamped and committed.
* **Reproducibility:** Simulations seeded; results reproducible.
* **Auditability:** No LLM‑generated numbers; all stats traceable to Python outputs.
* **Automated feeds:** Optional API connectors (odds, xG, in‑play events) with permission; all snapshots persisted to CSV/JSON for audit.

✅ This spec is now  **end‑to‑end complete** : Python engine, LLM interpretation, advanced modelling (xG, Markov, copula), automated feeds, and free EPL data sources.
