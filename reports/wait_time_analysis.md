# Waiting Time Estimation — Validation & Analysis (Week 6)

This document validates the queueing-aware waiting time estimation logic
introduced in Week 6 and documents expected system behavior under
different demand and capacity conditions.

---

## 1. Sanity Checks

The waiting time estimator must satisfy the following conditions:

- Waiting time should be approximately zero when arrival rate is well
  below service capacity.
- Waiting time should increase non-linearly as arrival rate approaches
  service capacity.
- Stations with higher charger counts should exhibit lower waiting time
  than lower-capacity stations under identical demand.
- Waiting time should never be negative.

Any violation of these conditions indicates a modeling or integration error.

---

## 2. Low-Demand Regime Analysis

In low-demand periods (λ ≪ μ):

- Stations operate under capacity
- Vehicles are immediately served upon arrival
- Estimated waiting time approaches zero

This behavior confirms that the model does not introduce artificial
delays when congestion is absent.

---

## 3. Peak Congestion Regime Analysis

In peak-demand periods (λ ≈ μ or λ > μ):

- Service capacity becomes a binding constraint
- Queues form and persist across time windows
- Waiting time increases rapidly as load exceeds capacity

This behavior reflects real-world congestion dynamics at charging stations.

---

## 4. Capacity Sensitivity Analysis

Holding demand constant:

- Increasing charger count reduces waiting time
- Stations with identical demand but different capacity exhibit
  materially different congestion profiles

This confirms that the model is capacity-aware rather than demand-only.

---

## 5. Model Limitations

The waiting time estimator does NOT capture:

- Within-hour arrival randomness
- Variability in charging duration
- User rerouting or abandonment behavior
- Priority access or reservation systems

These limitations are accepted trade-offs for stability,
interpretability, and alignment with available data.

---

## 6. Summary

Week 6 successfully extends demand forecasting into a
queueing-aware service model.

The system produces interpretable, capacity-sensitive
waiting time estimates suitable for congestion analysis
and downstream planning use cases.
