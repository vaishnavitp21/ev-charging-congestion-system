# Week 3 — Baseline Models

## Objective
Establish simple, transparent baselines to contextualize model performance
for EV charging station congestion prediction.

These baselines answer:
"What performance can be achieved without complex temporal or nonlinear models?"

---

## Mandatory Baselines (Must Beat)

### 1. Naive Persistence Baseline
**File:** models/baseline/naive_baseline.py

**Definition:**
Predict congestion at time t as the observed congestion at time t-1.

**Purpose:**
- Tests whether the system has temporal inertia
- Establishes a very strong trivial baseline for time series

**Failure Implication:**
If advanced models cannot beat this, they are not learning meaningful structure.

---

### 2. Historical Mean Baseline
**File:** models/baseline/historical_average.py

**Definition:**
Predict congestion as the global historical mean
(or mean per station if station_id is available).

**Purpose:**
- Measures signal beyond static averages
- Detects whether temporal variation matters

---

### 3. Linear Regression (Feature-based)
**File:** models/baseline/linear_regression.py

**Definition:**
Linear regression over engineered features
(time-of-day, day-of-week, lag features).

**Purpose:**
- Strong classical baseline
- Interpretable coefficients
- Acts as minimum bar before nonlinear models

---

## Optional / Stretch Baselines

### 4. Station-wise Mean
Predict per-station historical average.

Used to isolate spatial effects.

---

### 5. Lag-k Mean
Predict mean of last k observations.

Used to test smoothing vs persistence.

---

## Evaluation Protocol
All baselines:
- Use identical train/validation splits
- Are evaluated using the same metric functions
- Are compared against each other, not in isolation
