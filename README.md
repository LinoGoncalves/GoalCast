# GoalCast: EPL Prediction Engine 🎯⚽

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**GoalCast** is a sophisticated EPL (English Premier League) prediction engine that combines advanced statistical modeling with LLM-powered interpretation to deliver accurate match predictions and strategic insights for Superbru competitions.

## 🎯 Project Vision

Build a Python-based prediction engine that:
- **Outperforms** bookmaker odds in accuracy and calibration
- **Quantifies** overtake probabilities vs specific rivals
- **Optimizes** banker/valve/hedge strategies through Monte Carlo simulation
- **Provides** reproducible, auditable predictions with LLM-generated narratives
- **Integrates** advanced models (xG, copula, Markov chains) for competitive advantage

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    LLM Interpretation Layer                  │
│        (FastAPI + Streamlit + Markdown Playbooks)           │
└────────────────────┬────────────────────────────────────────┘
                     │ JSON/CSV Outputs
┌────────────────────▼────────────────────────────────────────┐
│                    Python Engine (Source of Truth)           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Data         │  │ Statistical  │  │ Monte Carlo  │     │
│  │ Ingestion    │─▶│ Models       │─▶│ Simulation   │     │
│  │              │  │              │  │              │     │
│  │ • Fixtures   │  │ • Poisson    │  │ • Rival      │     │
│  │ • Odds       │  │ • Dixon-Coles│  │   Analysis   │     │
│  │ • xG Data    │  │ • Bayesian   │  │ • Calibration│     │
│  │ • Injuries   │  │ • Copula     │  │ • Reports    │     │
│  │ • Live Feed  │  │ • Markov     │  │              │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Observability & Infrastructure                  │
│        (Prometheus + Grafana + Docker + CI/CD)              │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager
- Docker (for containerized deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/GoalCast.git
cd GoalCast

# Install dependencies with uv
uv sync

# Run tests
uv run pytest

# Start the API server
uv run fastapi dev src/goalcast/api/main.py

# Launch the Streamlit dashboard
uv run streamlit run src/goalcast/ui/dashboard.py
```

## 📊 Key Features

### Statistical Models
- **Poisson/Dixon-Coles**: Baseline exact score probabilities
- **Bayesian Hierarchical**: Team attack/defense strengths with uncertainty
- **xG Integration**: Shot-based expected goals to refine predictions
- **Copula Distributions**: Joint score modeling with flexible correlation
- **Markov Chains**: In-play probability updates

### Prediction Capabilities
- Match outcome probabilities (Win/Draw/Loss)
- Exact scoreline predictions
- Overtake probability vs rivals
- Banker/valve/hedge strategy optimization
- KO-15' live decision support

### Quality Metrics
- Brier score and log loss
- Calibration curves
- Accuracy vs bookmaker baseline
- xG calibration validation
- In-play Markov validation

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.13+ |
| **Package Manager** | uv |
| **Data Processing** | pandas, polars |
| **ML/Stats** | scikit-learn, PyTorch, scipy |
| **API** | FastAPI |
| **UI** | Streamlit |
| **Monitoring** | Prometheus, Grafana |
| **Testing** | pytest, hypothesis |
| **Code Quality** | ruff, mypy |
| **Security** | ASH v3 (bandit, semgrep, grype) |
| **Documentation** | Sphinx |
| **Deployment** | Docker, docker-compose |

## 📁 Project Structure

```
GoalCast/
├── src/
│   └── goalcast/
│       ├── data/              # Data ingestion & processing
│       ├── models/            # Statistical models
│       ├── simulation/        # Monte Carlo engine
│       ├── llm/               # LLM interpretation layer
│       ├── api/               # FastAPI services
│       └── ui/                # Streamlit dashboards
├── tests/                     # Test suite
├── data/                      # Data storage (gitignored)
├── docs/                      # Sphinx documentation
├── docker/                    # Container configurations
├── agentic-framework/         # AI agent personas & standards
├── pyproject.toml             # uv configuration
└── README.md
```

## 🎯 Project Epics

1. **[EPIC 1: Data Foundation & Ingestion Pipeline](../../issues/1)**
2. **[EPIC 2: Core Statistical Modeling Engine](../../issues/2)**
3. **[EPIC 3: Monte Carlo Simulation & Rival Analysis](../../issues/3)**
4. **[EPIC 4: In-Play Markov Chain Model](../../issues/4)**
5. **[EPIC 5: LLM Interpretation & Playbook Generation](../../issues/5)**
6. **[EPIC 6: Microservices Architecture & Deployment](../../issues/6)**
7. **[EPIC 7: Quality Assurance & Testing Framework](../../issues/7)**

## 📈 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Accuracy vs Bookmaker | +5% outcome accuracy | Brier score improvement |
| Exact Score Accuracy | 15%+ exact predictions | Season-long tracking |
| Calibration Quality | < 0.15 Brier score | Weekly calibration curves |
| Overtake Probability Accuracy | 80%+ correct direction | Rival swing validation |
| Valve Efficiency | +2 EV per valve used | Expected value analysis |
| Reproducibility | 100% seed-based | All simulations reproducible |
| Model Update Latency | < 2 hours pre-kickoff | Pipeline automation |
| In-play Accuracy | 85%+ vs live odds | Markov chain validation |

## 🌐 Data Sources (Free EPL Data)

### Stats & Analytics
- [SoccerSTATS.com](https://www.soccerstats.com/) – Goal timings, form, head-to-head
- [FBref](https://fbref.com/en/comps/9/Premier-League-Stats) – Advanced metrics, xG, shot maps
- [ThePuntersPage](https://www.thepunterspage.com/) – Referee stats, betting analytics

### News & Fixtures
- [PremierLeague.com](https://www.premierleague.com/) – Official fixtures, injuries, press conferences
- [BBC Sport](https://www.bbc.com/sport/football) – Previews, injury news
- [Sky Sports](https://www.skysports.com/football) – Breaking news, tactical analysis

### xG & Advanced Data
- [Understat.com](https://understat.com/) – xG data, shot maps
- [Infogol.net](https://www.infogol.net/) – xG previews, probability distributions

### Odds & Market
- [OddsPortal.com](https://www.oddsportal.com/) – Odds history, line movement
- [Betfair Exchange](https://www.betfair.com/) – Live market sentiment

## 🤝 Contributing

This project uses an **agentic framework** with AI assistants for different specialist roles. See the [agentic-framework](./agentic-framework/) directory for:

- **Master Agent**: Project orchestration
- **Sub-Agents**: Specialized AI assistants (data engineer, data scientist, ML engineer, etc.)
- **Standards**: Development guidelines and best practices

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- EPL data providers (see Data Sources section)
- Open-source Python data science community
- Superbru for the prediction platform

---

**Built with ❤️ by the GoalCast Team | Powered by Python, AI, and Statistical Rigor**
