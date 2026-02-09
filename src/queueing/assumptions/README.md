# Queueing Assumptions — Week 6

This document defines the system-level assumptions used to estimate user waiting time
at EV charging stations. These assumptions explicitly separate demand forecasting
from service congestion dynamics.

---

## 1. Definition of Waiting Time

Waiting time is defined as:

The time elapsed between a vehicle’s arrival at a charging station and the moment
charging service begins.

Waiting time explicitly EXCLUDES:
- Charging duration
- Travel time to the station
- Time spent searching for or rerouting between stations
- Reservation or booking delays (if any)

This definition ensures that waiting time reflects congestion and queue buildup,
not energy consumption or trip planning behavior.

---

## 2. System Boundary

The system models an individual EV charging station observed at hourly resolution.

Each station is treated as:
- A service system with a finite number of identical chargers (servers)
- Parallel service capability equal to the charger count at the station

The model operates on:
- Aggregated hourly arrivals (station_id × hour)
- Station-level capacity attributes already present in the dataset

The model does NOT represent:
- Individual vehicle-level arrivals or departures
- Within-hour arrival ordering
- Charger failures, maintenance, or downtime
- Reservation systems or priority queues

---

## 3. Why Queueing Is Required

Waiting time cannot be inferred directly from demand alone.

Two time periods with identical arrival demand may exhibit very different waiting
times depending on available service capacity.

Waiting time is driven by the interaction between:
- Arrival rate (demand intensity)
- Service rate (charging capacity)

Therefore, a queueing-aware approach is required to translate ML-based demand
forecasts into user-relevant waiting time estimates.

This motivates a hybrid approach:
- Machine Learning for arrival rate estimation
- Classical queueing theory for congestion modeling

---

## 4. Week 6 Scope and Outputs

Week 6 produces:
- Estimated expected waiting time per station per hour
- Derived from forecasted arrival rates and station service capacity
- Using explicitly stated queueing assumptions

Week 6 does NOT:
- Predict charging duration
- Simulate individual vehicles
- Introduce new datasets or external signals
- Optimize station placement or pricing strategies

The objective is service-level interpretability, not behavioral simulation.
