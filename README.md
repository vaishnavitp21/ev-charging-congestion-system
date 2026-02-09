# EV Charging Congestion Prediction System

## Overview
This project builds a data-driven system to estimate, assess, and manage congestion at electric vehicle (EV) charging stations using historical charging behavior, temporal patterns, and external weather data.

The system progresses from **data ingestion and forecasting** to **queueing-aware waiting time estimation**, and finally to an **interpretable decision-support layer** that guides user actions under congestion.

The final system produces:
- A clean, time-aligned, model-ready dataset
- Queueing-based waiting time estimates
- A deterministic congestion risk score
- Rule-based charging recommendations

---

## Problem Statement
EV charging stations experience unpredictable congestion due to:
- Temporal demand spikes
- Station-level capacity constraints
- Stochastic arrival and service behavior
- External factors such as weather

Unmanaged congestion leads to:
- Long waiting times
- Poor user experience
- Inefficient infrastructure utilization

This system addresses these issues by moving beyond raw prediction into **operational decision support**.

---

## Project Structure

ev_charging_congestion_system/
├── analysis/                # EDA and evaluation notebooks
├── configs/                 # Configuration files
├── data/
│   ├── external/
│   │   └── weather/         # Raw & processed weather data
│   ├── interim/             # Intermediate datasets
│   └── processed/           # Final model-ready datasets
├── docs/                    # Design documents
├── experiments/             # Model experiments
├── models/                  # Saved models & checkpoints
├── reports/                 # Analysis & decision documentation
├── src/                     # Core feature, queueing, risk, decision code
│   ├── queueing/            # Arrival rate, service rate, wait-time estimation
│   ├── risk/                # Congestion risk index logic
│   └── decision/            # Rule-based recommendation logic
├── tests/                   # Unit tests
├── venv/                    # Virtual environment (ignored)
├── .gitignore
├── requirements.txt
└── README.md

---

## Environment
- Python 3.10 / 3.11
- Virtual environment: `venv`
- IDE: VS Code (only)
- OS: Windows / Linux compatible

---

## Weekly Progress

### Week 0 — Environment & Scaffolding ✅
- Project structure finalized
- Virtual environment setup
- Git repository initialized
- Tooling locked (VS Code, venv, Python)

---

### Week 1 — Problem Definition & System Design ✅
- Clear problem statement and scope definition
- End-to-end system architecture documented
- Explicit separation between data, modeling, and decision layers

---

### Week 2 — Baseline Modeling & Temporal Features ✅
- Hourly charging aggregation
- Temporal feature engineering (hour, day, seasonality)
- Baseline demand forecasting model
- Time-based validation
- Error and residual analysis

---

### Week 3 — Data Pipeline Hardening ✅
- Charging data cleaning and validation
- Station-level consistency checks
- Schema stabilization and invariants enforced

---

### Week 4 — Weather Data Integration ✅
- Downloaded hourly historical weather data
- Engineered weather features:
  - Temperature
  - Dew point
  - Humidity
  - Wind speed
  - Precipitation
  - Pressure
- Time-aligned weather data with charging demand

---

### Week 5 — Model-Ready Dataset Construction ✅
- Joined charging and weather datasets
- Enforced strict hourly alignment
- Removed non-informative features (e.g., `coco`)
- Missing value analysis and handling
- Final dataset validation

**Final output:**

- Rows: ~234k  
- Columns: 11  
- Status: Model-ready

---

### Week 6 — Queueing-Aware Waiting Time Estimation ✅
- Derived arrival rate (λ) from predicted demand
- Defined service rate (μ) from charger characteristics
- Modeled station capacity explicitly
- Estimated waiting time using queueing-theoretic assumptions
- Documented assumptions, limitations, and stability conditions

This week bridges **prediction → operational impact**.

---

### Week 7 — Congestion Risk Index & Decision Layer ✅
- Defined a deterministic Congestion Risk Index (CRI) derived from:
  - Utilization pressure
  - Waiting time stress
  - Temporal demand context
- Normalized and bounded all risk components
- Added qualitative interpretation of low / moderate / high risk
- Introduced rule-based recommendations:
  - Charge now
  - Defer charging
  - Consider alternate station (if available)
- Validated behavior using scenario-based analysis
- Locked acceptance criteria and design guardrails to prevent learning, retraining, or scope creep

This week converts estimation into **actionable decision support**.

---

## How to Run

```bash
# Activate environment
venv\Scripts\activate

# Build charging data
python data/interim/build_charging_hourly.py

# Download weather data
python data/external/weather/download_weather.py

# Build weather features
python data/external/weather/build_weather_features.py

# Build final dataset
python data/processed/build_model_dataset.py
