# Evaluation Strategy

## Task
Predict the number of charging sessions in the next hour per station.

## Primary Metric: MAE
Mean Absolute Error is used as the primary metric because:
- It is robust to outliers caused by rare surge events
- It directly reflects average prediction error in session counts
- It is easy to explain to non-ML stakeholders

## Secondary Metric: RMSE
RMSE is reported to penalize large errors and understand tail risk.

## Baseline
A mean predictor baseline is used with a time-based split to avoid leakage.
All models must outperform this baseline on MAE to be considered useful.
