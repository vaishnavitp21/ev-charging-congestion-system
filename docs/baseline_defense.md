# Baseline Strategy — Interview Defense

## Why Baselines Matter
Baselines establish a minimum acceptable performance and prevent over-engineering.
They help validate that the problem is learnable from available data.

## Baselines Used
- Global mean predictor
- Station-level mean predictor
- Lag-1 temporal baseline

## What They Tell Us
- Station mean captures static demand differences
- Lag-1 baseline captures short-term temporal dependence
- Any learned model must outperform these to be useful

## Interview Soundbite (30 seconds)
“I always start with strong baselines to verify signal, quantify gains,
and avoid unnecessary complexity. In this project, even simple temporal baselines
were competitive, which informed my decision to prefer interpretable models.”
