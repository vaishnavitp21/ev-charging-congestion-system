# Error Analysis — TFT EV Charging Congestion

## 1. Where the model performs well
- Regular weekdays
- Office-area stations
- Stable pricing regimes
- Midday and evening peaks

## 2. Failure cases
### a) Holidays
- Demand patterns deviate from learned weekday cycles
- Underprediction during unexpected surges

### b) Sparse stations
- New or low-traffic stations lack sufficient history
- TFT defaults to population-level patterns

### c) Weather extremes
- Heavy rainfall / heatwaves not fully captured
- Lagged weather effects observed

## 3. Bias & variance tradeoff
- Low variance across normal days
- Higher bias on rare events

## 4. Mitigations (future work)
- Add holiday embeddings
- Cluster stations by usage profile
- Incorporate weather forecasts (known future covariates)
- Increase encoder length during seasonal retraining
