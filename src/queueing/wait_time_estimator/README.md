# Waiting Time Estimation Logic

This module defines the logic used to estimate expected waiting time
from arrival rate and service capacity.

The objective is to provide a queue-aware, deterministic estimate
that reflects congestion effects without requiring full stochastic simulation.

---

## 1. Inputs

The waiting time estimator operates on:
- Arrival rate λ (vehicles per hour)
- Service capacity μ (vehicles per hour)
- Number of parallel servers (chargers)

All inputs are indexed at station_id × hour.

---

## 2. Congestion Load Factor

Congestion is characterized using a load factor:

ρ = λ / μ

This represents how heavily loaded a station is during a given hour.

Interpretation:
- ρ < 1 → system can absorb arrivals
- ρ ≈ 1 → system at capacity
- ρ > 1 → queue growth and delays

---

## 3. Waiting Time Estimation Strategy

Waiting time is estimated using a piecewise logic:

- If ρ is sufficiently below capacity:
  Waiting time is approximately zero

- If ρ approaches capacity:
  Waiting time increases non-linearly

- If ρ exceeds capacity:
  Waiting time grows rapidly due to queue accumulation

This logic captures congestion effects without requiring
explicit modeling of arrival or service time distributions.

---

## 4. Justification

This approach is chosen because:
- Hourly aggregation limits stochastic fidelity
- Station capacity is the dominant driver of delay
- Deterministic estimates are easier to validate and explain
- The goal is service-level insight, not exact queue simulation

---

## 5. What This Model Captures

- Impact of demand relative to capacity
- Differences between low-load and peak-load periods
- Station-to-station capacity heterogeneity

---

## 6. What This Model Ignores

- Within-hour arrival variability
- Random service time fluctuations
- Short-term burstiness
- User behavior under congestion

These limitations are accepted trade-offs for robustness and interpretability.
