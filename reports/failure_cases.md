# Failure Cases & System Boundaries

## Purpose
This document enumerates known, expected, and unacceptable failure modes
of the EV Charging Congestion Prediction System.

The goal is not to eliminate all failures, but to:
- Make failures explicit
- Separate acceptable degradation from system bugs
- Prevent silent or misleading outputs in production

---

## Definitions

### Acceptable Failure
A condition where:
- The system produces a degraded, conservative, or partial output
- The behavior is explainable and deterministic
- No incorrect confidence is presented to the user

Examples:
- Falling back to historical averages when weather data is missing
- Increasing uncertainty under sparse station activity
- Returning "low confidence" instead of a numeric prediction

---

### System Bug (Unacceptable)
A condition where:
- Outputs are incorrect, unstable, or misleading
- The system fails silently
- Internal assumptions are violated without detection

Examples:
- Negative congestion probabilities
- Non-deterministic outputs for identical inputs
- Risk scores increasing when demand decreases
- API returns success with corrupted inputs

---

## What Is Explicitly Tested in Week 9

### Data Layer
- Schema integrity
- Missing or partial inputs
- Boundary values (zero demand, peak demand)
- Time alignment assumptions

### Decision & Risk Logic
- Deterministic behavior
- Sensitivity to input perturbations
- Graceful degradation paths

### System Integration
- API → model → decision flow
- Failure propagation visibility
- End-to-end stability under stress

---

## What Is Explicitly NOT Tested

- Model retraining performance
- UI responsiveness or aesthetics
- New feature behavior
- Dataset correctness beyond structural validation

These are out of scope by design.

---

## Data-Layer Failure Modes (Week 9 Scope)

The following failure modes are explicitly tested in `tests/data_tests/`.

### 1. Missing Required Fields
Description:
- One or more mandatory inputs (timestamp, station_id, demand signal) absent.

Expected behavior:
- Hard fail OR explicit fallback path.
- Never silently impute critical identifiers.

Classification:
- ❌ System bug if silent
- ⚠️ Acceptable if explicit fallback is documented

---

### 2. Null or NaN Values
Description:
- Required numeric fields present but null / NaN.

Expected behavior:
- Conservative handling (drop row, fallback, or low-confidence output).

Classification:
- ⚠️ Acceptable failure if handled deterministically
- ❌ Bug if propagated downstream

---

### 3. Temporal Misalignment
Description:
- Feature timestamps outside prediction horizon
- Weather lagging or leading demand window

Expected behavior:
- Detection and rejection OR explicit realignment logic.

Classification:
- ❌ Bug if undetected
- ⚠️ Acceptable if corrected and logged

---

### 4. Zero-Activity Edge Case
Description:
- Stations with zero demand history in the evaluation window.

Expected behavior:
- Low-confidence or baseline output
- No division-by-zero or instability

Classification:
- ⚠️ Acceptable degradation
- ❌ Bug if unstable output

---

### 5. Extreme Out-of-Range Values
Description:
- Unrealistic spikes (e.g., demand >> historical max)

Expected behavior:
- Clipping, bounding, or risk inflation
- No numeric explosion

Classification:
- ❌ Bug if output unbounded
- ⚠️ Acceptable if risk-aware response

---

## Model & Decision-Layer Failure Modes (Week 9 Scope)

The following failure modes are explicitly tested in `tests/model_tests/`.

### 1. Non-Deterministic Outputs
Description:
- Identical inputs produce different outputs across runs.

Expected behavior:
- Outputs must be deterministic given fixed inputs and model state.

Classification:
- ❌ System bug (always)

---

### 2. Unbounded or Invalid Outputs
Description:
- Negative congestion values
- Probabilities outside [0, 1]
- Risk scores exceeding defined limits

Expected behavior:
- Outputs must be bounded and validated before exposure.

Classification:
- ❌ System bug

---

### 3. Sensitivity Explosion
Description:
- Small perturbations in input produce disproportionately large output changes.

Expected behavior:
- Smooth, explainable response curves.
- Risk inflation instead of output instability.

Classification:
- ⚠️ Acceptable only if explainable and bounded
- ❌ Bug if unstable or chaotic

---

### 4. Monotonicity Violations
Description:
- Increased demand leads to lower congestion or risk score.

Expected behavior:
- Monotonic assumptions must hold within defined envelopes.

Classification:
- ❌ System bug unless explicitly justified

---

### 5. Overconfident Predictions
Description:
- High-confidence output under sparse or unreliable input conditions.

Expected behavior:
- Confidence must degrade with data quality.

Classification:
- ⚠️ Acceptable only if confidence is surfaced
- ❌ Bug if silent

---

## Integration Failure Modes (Week 9 Scope)

The following failure modes are explicitly tested in `tests/integration_tests/`.

### 1. Partial Dependency Failure
Description:
- One upstream component fails (e.g., weather unavailable) while others succeed.

Expected behavior:
- System continues with degraded but safe output.
- Explicit signal that partial data was used.

Classification:
- ⚠️ Acceptable degradation if explicit
- ❌ Bug if silent or misleading

---

### 2. API Contract Drift
Description:
- API receives structurally valid but semantically incorrect payloads.

Expected behavior:
- Validation failure or rejection.
- Never pass malformed semantics downstream.

Classification:
- ❌ System bug if accepted silently

---

### 3. Timeout or Latency Spikes
Description:
- One component responds slowly or times out under load.

Expected behavior:
- Bounded waiting, fallback, or fast failure.
- No cascading stalls.

Classification:
- ⚠️ Acceptable if bounded and visible
- ❌ Bug if cascading failure occurs

---

### 4. Inconsistent Feature Availability
Description:
- Some features computed, others missing due to partial pipeline failure.

Expected behavior:
- Conservative decision or explicit rejection.
- No mixed-confidence outputs.

Classification:
- ❌ Bug if confidence not degraded

---

### 5. End-to-End Stress Conditions
Description:
- High request volume or repeated edge cases.

Expected behavior:
- Stable outputs, increased latency acceptable.
- No memory leaks or state corruption.

Classification:
- ⚠️ Acceptable degradation
- ❌ Bug if correctness compromised
