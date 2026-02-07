# Feature ↔ Target Relationship Sanity Check

## Temporal Features → Target
EV charging demand follows strong daily and weekly patterns. Peak congestion is
more likely during office hours, evenings, and weekends. Temporal features such as
hour of day, day of week, and weekend indicators help the model learn recurring
usage cycles that directly influence congestion levels.

## Historical Usage Features → Target
Recent past utilization and queue behavior are strong predictors of near-future
congestion. Rolling averages of charger utilization and queue length capture demand
momentum and short-term trends, allowing the model to anticipate whether congestion
is likely to increase or decrease in the next 30 minutes.

## Infrastructure Features → Target
Station capacity and charger characteristics constrain how demand translates into
congestion. Stations with fewer chargers or slower charger types are more prone to
high congestion under similar demand conditions. Infrastructure features provide
context that explains why identical demand levels may result in different congestion
outcomes across stations.

## External Context Features → Target
External factors such as weather, traffic congestion, and public holidays influence
EV usage behavior. For example, bad weather or heavy traffic can increase charging
demand at certain locations, while holidays may shift usage patterns. These features
add situational awareness beyond station-level data.

---

## Features Considered but Rejected
- Real-time queue length at prediction time (leaks target information)
- Current charger utilization at prediction time (direct proxy for target)
- Number of vehicles arriving in the next 30 minutes (future information unavailable
  at prediction time)

---

## Risk Assessment
The model may underperform during rare or anomalous events such as major outages,
special events, or sudden policy changes that are not reflected in historical data.
Bias may also occur if certain stations have limited historical data or if external
data sources (e.g., traffic or weather) are noisy or delayed.
