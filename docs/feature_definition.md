# Feature Definitions & Leakage Guardrails

## Feature Groups

### 1. Temporal Features (ALLOWED)
- Hour of day (0–23)
- Day of week (0–6)
- Is weekend (boolean)
- Time slot index (based on 30-minute bins)

### 2. Historical Usage Features (ALLOWED)
- Charger utilization rate over past 15 minutes
- Charger utilization rate over past 30 minutes
- Rolling average utilization over past 1 hour
- Rolling average queue length over past 1 hour
- Number of charging sessions completed in past 1 hour

### 3. Infrastructure Features (ALLOWED)
- Number of chargers at the station
- Charger type (fast / slow)
- Maximum station capacity
- Station location type (highway / urban / residential)

### 4. External Context Features (ALLOWED)
- Weather condition (rain / clear / extreme)
- Temperature
- Nearby traffic congestion level (historical or delayed feed)
- Public holiday indicator

---

## Forbidden / Leakage Features (NOT ALLOWED)
- Current or future queue length at prediction time
- Current charger utilization at prediction time
- Number of vehicles arriving after prediction time
- Any feature computed using data after the prediction timestamp
- Target variable (`congestion_level`) or proxies derived from it

---

## Feature Time Alignment Rule
All features must be computed using data strictly available **before** the prediction timestamp.
No feature may use real-time or future information from the prediction window.
