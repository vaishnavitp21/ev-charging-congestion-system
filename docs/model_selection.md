# Model Selection Decision

## Candidate Models Evaluated
- Global Mean Baseline
- Station Mean Baseline
- Lag-1 Temporal Baseline
- Linear Regression with Temporal Features
- Decision Tree with Temporal Features

## Evaluation Setup
- Time-based split (train before 2020, validate on 2020)
- Primary metric: MAE
- Secondary metric: RMSE

## Results Summary
Linear Regression and Decision Tree both outperform baselines.
Decision Tree achieves slightly lower RMSE, while MAE is comparable.

## Selected Model
Linear Regression with temporal features.

## Rationale
- Stable and interpretable coefficients
- Comparable MAE to Decision Tree
- Lower risk of overfitting
- Easier to debug and monitor in production

## Trade-offs Accepted
- Lower ceiling than boosted trees
- Cannot model complex non-linear interactions

## Future Upgrade Path
- Gradient Boosted Trees once external features are added
- Separate weekday/weekend models
