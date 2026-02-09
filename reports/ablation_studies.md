# Test Coverage & Evaluation Strategy

## Purpose
This document defines how test results are interpreted in Week 9.
Tests are not binary gates; they are diagnostic instruments.

---

## Test Categories

### 1. Data Tests (`tests/data_tests/`)
Focus: Input validity and assumptions.

Validated aspects:
- Schema conformity
- Required vs optional fields
- Missing, null, or malformed values
- Temporal alignment (timestamps, horizons)

Failure interpretation:
- ❌ Fail → upstream data contract violation
- ⚠️ Warning → acceptable degradation path must exist
- ✅ Pass → safe to proceed downstream

---

### 2. Model & Decision Tests (`tests/model_tests/`)
Focus: Determinism, stability, and sensitivity.

Validated aspects:
- Deterministic outputs for identical inputs
- Bounded outputs (no negatives, no explosions)
- Sensitivity to controlled perturbations
- Risk monotonicity assumptions

Failure interpretation:
- ❌ Fail → system bug
- ⚠️ Warning → model brittle but explainable
- ✅ Pass → behavior within expected envelope

---

### 3. Integration Tests (`tests/integration_tests/`)
Focus: End-to-end system behavior.

Validated aspects:
- API → feature → model → decision flow
- Failure propagation visibility
- Graceful fallback under partial outages

Failure interpretation:
- ❌ Fail → production-blocking issue
- ⚠️ Warning → acceptable but must be documented
- ✅ Pass → system resilient under stress

---

## Pass / Warn / Fail Philosophy

- A system can ship with WARNINGS
- A system cannot ship with SILENT FAILURES
- Explicit failure is preferred over confident wrong output
