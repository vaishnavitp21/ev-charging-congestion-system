# Feature Contract — EV Charging Congestion System

## Entity
Each row represents:
> One charging station × one fixed time window

---

## Time Window
- Window size: 15 minutes
- Window aligned to wall-clock time
- All features use ONLY past data within the window

---

## Input Features (X)

| Feature Name | Description | Unit | Leakage Safe |
|-------------|-------------|------|--------------|
| station_id | Unique charging station identifier | categorical | ✅ |
| time_of_day | Hour of day extracted from window start | 0–23 | ✅ |
| day_of_week | Day index (Mon=0) | 0–6 | ✅ |
| active_sessions | Number of charging sessions active | count | ✅ |
| energy_dispensed | Total kWh dispensed in window | kWh | ✅ |
| avg_session_duration | Mean duration of sessions | minutes | ✅ |
| charger_utilization | Active chargers / total chargers | ratio | ✅ |

---

## Target (y)

| Name | Definition | Unit |
|----|------------|------|
| congestion_level | Percentage utilization of station | 0–1 |

---

## Leakage Rules
- ❌ No future timestamps
- ❌ No aggregated future demand
- ❌ No labels used in features

---

## Notes
- Feature definitions are immutable once model training begins
- Any change requires version bump
