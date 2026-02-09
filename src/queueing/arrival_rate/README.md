# Arrival Rate Estimation (λ)

This module defines how arrival rates are derived from machine learning
demand forecasts produced in Week 5.

---

## 1. Definition of Arrival Rate

Arrival rate (λ) is defined as the expected number of EV charging arrivals
to a given station within a one-hour time window.

λ is expressed in units of:
- vehicles per hour
- indexed by (station_id, hour)

---

## 2. Source of Arrival Rate

Arrival rates are obtained directly from the existing ML demand forecasting
pipeline.

Specifically:
- The ML model predicts hourly charging arrivals per station
- These predictions are interpreted as the expected arrival rate λ
  for the corresponding station and hour

No additional transformation or smoothing is applied at this stage.

---

## 3. Justification

Using ML-predicted demand as arrival rate is justified because:
- The temporal granularity of the dataset is hourly
- Queueing models operate on expected arrival intensity
- The forecast represents the mean arrival behavior over the hour

This preserves consistency between forecasting and queueing layers.

---

## 4. What Is Not Modeled Here

This module does NOT:
- Assume a specific arrival distribution (e.g., Poisson)
- Model within-hour arrival timing
- Introduce stochastic sampling of arrivals
- Modify or retrain ML models

Arrival uncertainty is addressed later at the queueing level if required.
