# Model Analysis & Insights

## Best Performing Model
Decision Tree with temporal features achieved the lowest RMSE while matching linear regression on MAE.

## Key Error Patterns

### Time of Day
Errors peak during early morning and late night hours, likely due to sparse and bursty charging behavior.

### Station-Level Variance
A small subset of stations contributes disproportionately to total error, indicating heterogeneous usage patterns.

### Weekend Effect
Weekend demand is significantly harder to predict, suggesting different behavioral regimes.

## Limitations
- No external context (weather, events)
- No station embeddings
- Single global model for all stations

## Next Improvements (Production Roadmap)
1. Add weather and calendar event features
2. Train separate weekday/weekend models
3. Introduce station embeddings or per-station normalization
4. Upgrade to gradient-boosted trees
