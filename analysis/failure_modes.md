# Failure Modes — Naive Persistence Baseline

This document summarizes systematic failure patterns observed in the
naive persistence baseline for EV charging congestion prediction.

---

## Failure Mode 1: Sudden Demand Spikes

**Description:**
The persistence baseline significantly underpredicts congestion during
abrupt demand increases (e.g., sharp rises in usage).

**Evidence:**
- Large positive prediction errors in the error-over-time plot
- Heavy right tail in the error distribution

**Root Cause:**
The model assumes short-term stationarity and cannot anticipate
exogenous demand shocks.

**Impact:**
High congestion events are detected late, reducing system responsiveness.

---

## Failure Mode 2: Rapid Demand Drops

**Description:**
After congestion peaks, the baseline overpredicts congestion during
sharp declines.

**Evidence:**
- Negative error values immediately following peaks

**Root Cause:**
The model blindly propagates previous high values forward.

**Impact:**
Leads to conservative estimates that may over-allocate resources.

---

## Failure Mode 3: Trend Changes

**Description:**
The baseline performs poorly during regime shifts or gradual upward trends.

**Evidence:**
- Sustained error bias over consecutive time steps

**Root Cause:**
Lack of trend modeling or temporal context beyond t−1.

**Impact:**
Systematically biased forecasts over longer horizons.

---

## Summary

The naive persistence baseline is effective only under stable,
slowly-varying conditions. Its failure modes motivate the use of:
- Lag aggregation
- Time-of-day features
- Explicit trend modeling

These insights guide the design of more advanced baselines and models.
