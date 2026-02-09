# Service Rate Definition (μ)

This module defines how service capacity is represented for each EV charging
station in the queueing model.

---

## 1. Definition of Service Rate

Service rate (μ) represents the maximum number of vehicles that can begin
charging service per hour at a station.

μ is expressed in units of:
- vehicles per hour
- indexed by station_id

---

## 2. Station Capacity Representation

Each charging station is modeled as a system with:
- A fixed number of identical chargers
- Parallel service capability equal to charger count

Each charger serves:
- One vehicle at a time
- For the duration of a charging session

---

## 3. Charging Duration Assumption

Charging session duration is treated as:
- A fixed average value
- Common across stations
- Not predicted by machine learning

This assumption is necessary because:
- Charging duration is not available at sufficient resolution
- The objective is congestion estimation, not energy modeling
- Fixing duration isolates queue effects from energy demand variability

---

## 4. Deriving Service Capacity

Station-level service capacity is determined by:
- Number of chargers at the station
- Assumed average charging duration

Together, these define the effective service rate μ for the station.

---

## 5. What Is Not Modeled Here

This module does NOT:
- Model variability in charging duration
- Account for charger outages or maintenance
- Consider priority access or reservations
- Adapt service rate dynamically based on demand

These effects are intentionally excluded to preserve model interpretability.
