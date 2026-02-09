# EV Charging Congestion Prediction System

## Overview
This project builds a **data-driven, end-to-end congestion prediction and decision-support system** for electric vehicle (EV) charging stations.

The system estimates:
- Hourly charging demand
- Queueing-based waiting times
- Congestion risk levels
- Actionable charging recommendations

It progresses from **data ingestion and forecasting** to **queueing-aware operational modeling**, and finally to a **production-style API and dashboard**.

---

## Problem Statement
EV charging stations experience unpredictable congestion due to:
- Temporal demand spikes
- Station-level capacity constraints
- Stochastic arrivals and service times
- External factors such as weather

Unmanaged congestion results in:
- Long waiting times
- Poor user experience
- Inefficient infrastructure utilization

This project moves beyond raw prediction into **operational decision support**.

---

## System Outputs
The final system produces:
- Hourly demand forecasts
- Queueing-based wait-time estimates
- Deterministic congestion risk levels
- Rule-based charging recommendations
- A FastAPI prediction service
- A Streamlit dashboard for interactive exploration

---

## Project Structure

  ev_charging_congestion_system/
  ├── data/
  │ ├── external/
  │ │ └── weather/
  │ ├── interim/
  │ └── processed/
  ├── docs/
  ├── experiments/
  ├── logs/
  ├── models/
  ├── notebooks/
  ├── reports/
  ├── src/
  │ ├── api/
  │ │ ├── main.py
  │ │ ├── routes/
  │ │ └── schemas/
  │ ├── app/
  │ │ └── dashboard/
  │ │ └── app.py
  │ ├── queueing/
  │ ├── risk/
  │ ├── decision/
  │ ├── targets/
  │ ├── run_target.py
  │ └── config.py
  ├── tests/
  ├── venv/
  ├── .env.example
  ├── .gitignore
  ├── requirements.txt
  └── README.md


---

## Environment
- Python 3.10 / 3.11
- Virtual environment: `venv`
- IDE: VS Code
- OS: Windows / Linux compatible

---

## Weekly Progress

### Week 0 — Environment & Scaffolding ✅
  - Repository initialized
  - Project structure finalized
  - Virtual environment setup
  - Tooling locked (VS Code, venv, Python)

---

### Week 1 — Problem Definition & System Design ✅
- Clear problem statement and scope
- End-to-end system architecture
- Explicit separation between data, modeling, and decision layers

---

### Week 2 — Baseline Modeling & Temporal Features ✅
- Hourly charging aggregation
- Temporal feature engineering
- Baseline demand forecasting
- Time-aware validation and error analysis

---

### Week 3 — Data Pipeline Hardening ✅
- Charging data cleaning and validation
- Station-level consistency checks
- Schema stabilization

---

### Week 4 — Weather Data Integration ✅
- Hourly historical weather ingestion
- Feature engineering:
- Temperature
- Humidity
- Wind speed
- Precipitation
- Time-aligned weather + charging data

---

### Week 5 — Model-Ready Dataset Construction ✅
- Joined charging and weather datasets
- Strict hourly alignment
- Removed non-informative features (e.g. `coco`)
- Missing value handling
- Final dataset validation

**Final dataset**
- ~234k rows
- 11 features
- Fully model-ready

---

### Week 6 — Queueing-Aware Waiting Time Estimation ✅
- Arrival rate (λ) derived from demand
- Service rate (μ) defined by charger capacity
- Explicit station capacity modeling
- Queueing-theoretic wait time estimation
- Assumptions and stability conditions documented

---

### Week 7 — Congestion Risk & Decision Layer ✅
- Deterministic Congestion Risk Index (CRI)
- Risk levels: `LOW`, `MEDIUM`, `HIGH`
- Rule-based recommendations:
  - Charge now
  - Consider off-peak hours
  - Delay charging
- Scenario-based validation
- Design guardrails locked

---

## Week 8 — API & Dashboard Integration ✅

### What Was Built

#### FastAPI Prediction Service
- REST API with `/predict` endpoint
- Strongly typed request/response schemas
- Router-based API design
- Stateless, deterministic execution

#### Core Prediction Logic
- Implemented in `run_target`
- Schema-compliant hourly outputs
- Ready for ML model replacement later

#### Streamlit Dashboard
- Interactive UI
- Real-time API calls
- Displays:
  - Hourly demand
  - Wait times
  - Risk levels
  - Recommendations

---
## Testing Strategy

This system uses failure-mode driven testing rather than accuracy-based testing.

Test coverage is organized as:
- Data validation tests (tests/data_tests)
- Model & decision safety tests (tests/model_tests)
- Integration degradation tests (tests/integration_tests)

See reports/ablation_studies.md and reports/failure_cases.md for rationale.


## API Usage

### Start API
```bash
uvicorn src.api.main:app --reload