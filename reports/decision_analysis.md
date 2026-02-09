# Week 7 — Decision & Recommendation Layer

## 1. Purpose of the Decision Layer

## 2. Definition of Congestion Risk Index (CRI)
The Congestion Risk Index (CRI) is a deterministic, derived metric that quantifies the operational stress of an EV charging station at a given time.

CRI is designed to answer the question:
“How likely is a user to experience unacceptable congestion if they attempt to charge now?”

The index is computed as a normalized combination of three interpretable system signals:

1. Utilization Pressure  
   Defined as the ratio of arrival rate to service capacity:
   
   ρ = λ / (c · μ)

   where:
   λ = predicted arrival rate  
   μ = service rate per charger  
   c = number of chargers  

   Values of ρ approaching or exceeding 1 indicate system instability.

2. Waiting Time Stress  
   Defined as the ratio of estimated waiting time to a user-tolerable threshold:

   Wₙ = min(W_est / W_max, 1)

   where:
   W_est = estimated waiting time from Week 6  
   W_max = maximum acceptable waiting time (policy-defined)

3. Temporal Demand Pressure  
   A binary or bounded scalar capturing peak vs off-peak behavior:

   T ∈ [0, 1]

   where higher values correspond to historically high-demand periods.

The final Congestion Risk Index is defined as:

CRI = w₁ · ρₙ + w₂ · Wₙ + w₃ · T

subject to:
w₁ + w₂ + w₃ = 1
wᵢ ≥ 0

All components are normalized to [0, 1], ensuring CRI ∈ [0, 1].

## 3. Inputs Used for Risk Computation
The Congestion Risk Index (CRI) depends exclusively on signals already produced by upstream system components.

The allowed inputs are:

1. Predicted Arrival Rate (λ)  
   Output of the demand forecasting module (Weeks 3–4).

2. Service Rate (μ)  
   Station-specific service capability derived from charger characteristics (Week 6).

3. Station Capacity (c)  
   Fixed number of available chargers at the station.

4. Estimated Waiting Time (W_est)  
   Computed using queueing-theoretic assumptions (Week 6).

5. Time Context  
   Hour-of-day or peak/off-peak indicator derived from timestamp metadata.

Optional inputs (only if available, not required):

6. Neighbor Station Congestion Signals  
   Aggregated risk or utilization indicators from nearby stations (Week 5).

The CRI does not depend on:
- User identity or preferences  
- Historical outcomes after recommendation  
- Learned policies or reinforcement signals  
- Any retraining or adaptive feedback loops

## 4. Normalization and Weighting Strategy
Each component of the Congestion Risk Index (CRI) is normalized to ensure interpretability and boundedness.

Utilization Pressure Normalization  
The utilization ratio ρ is clipped to the interval [0, 1]:

ρₙ = min(ρ, 1)

This prevents extreme overload conditions from dominating the score while preserving instability signals.

Waiting Time Stress Normalization  
Waiting time stress is normalized relative to a policy-defined maximum acceptable wait:

Wₙ = min(W_est / W_max, 1)

This aligns the metric with user experience thresholds without learning from outcomes.

Temporal Demand Normalization  
Temporal pressure T is defined on a bounded scale [0, 1] using static business rules
(e.g., peak vs off-peak classification).

Weighting Strategy  
Weights are chosen to balance operational load and user experience:

w₁ ≥ w₂ ≥ w₃

subject to:
w₁ + w₂ + w₃ = 1

This ordering prioritizes system stability over delay perception, while still accounting for temporal demand patterns.

Weights are fixed, policy-defined constants and do not adapt over time.

## 5. Interpretation of Congestion Risk Levels
The Congestion Risk Index (CRI) provides a continuous measure of congestion risk on a normalized scale.

Low Risk (CRI ≈ 0)  
Indicates underutilized or well-balanced system conditions.
Users are unlikely to experience waiting delays or capacity contention.

Moderate Risk (CRI ≈ 0.5)  
Represents transitional conditions where demand approaches service capacity.
Some waiting may occur, and user experience is sensitive to short-term fluctuations.

High Risk (CRI ≈ 1)  
Signals sustained overload or near-instability conditions.
Users are highly likely to experience significant waiting times or denied service.

These interpretations are qualitative and descriptive.
They do not imply hard thresholds or automatic decisions.

## 6. Decision Rules and Recommendation Logic
The decision layer consumes the Congestion Risk Index (CRI) and system context
to generate user-facing recommendations.

All decisions are rule-based, deterministic, and interpretable.

### 6.1 Best Time to Charge

IF:
- CRI is low
- AND estimated waiting time is minimal
- AND station capacity is not saturated

THEN:
- Recommend charging immediately
- Indicate low congestion risk to the user

### 6.2 Avoid or Defer Charging

IF:
- CRI is high
- OR utilization pressure indicates near-instability
- OR estimated waiting time exceeds acceptable limits

THEN:
- Recommend deferring charging
- Suggest checking later off-peak periods

### 6.3 Consider Alternate Station (Optional)

IF:
- CRI is moderate to high
- AND neighbor station signals indicate lower congestion elsewhere

THEN:
- Recommend an alternate nearby station
- Provide comparative congestion context

Decision rules are intentionally conservative.
They prioritize system stability and user experience over short-term throughput.

## 7. Validation and Scenario-Based Analysis
The decision layer is validated using scenario-based analysis rather than predictive accuracy metrics.

Key evaluation scenarios include:

Peak Demand Scenario  
High arrival rates during peak hours with limited station capacity.
Expected behavior:
- CRI increases toward high risk
- System recommends deferring charging or alternate stations

Off-Peak Scenario  
Low arrival rates with ample service capacity.
Expected behavior:
- CRI remains low
- System recommends charging immediately

Capacity-Constrained Scenario  
Normal demand with reduced service capacity (e.g., charger outages).
Expected behavior:
- Utilization pressure dominates CRI
- System shifts recommendations toward avoidance or deferral

Sensitivity Analysis  
CRI sensitivity is assessed by perturbing individual inputs (λ, μ, W_est)
while holding others constant.
This ensures:
- Monotonic response to worsening conditions
- No abrupt decision flips due to minor input noise

The decision layer supports qualitative validation of system behavior,
not quantitative performance guarantees.

## 8. Acceptance Criteria and Design Guardrails
Week 7 is considered complete when the following conditions are met:

Acceptance Criteria
- A deterministic Congestion Risk Index (CRI) is defined using existing system outputs
- Risk computation is explicit, interpretable, and bounded
- Decision logic is rule-based and explainable
- Recommendations depend only on CRI and allowed system context
- No models are retrained and no new datasets are introduced
- Validation is scenario-driven and qualitative

Design Guardrails (FAANG-Level Red Flags Avoided)
- No learned policies or end-to-end optimization
- No feedback loops from recommendations into model training
- No hard-coded thresholds masquerading as learned behavior
- No silent expansion of inputs beyond declared scope
- No coupling between decision rules and model internals
- No claims of optimality or guaranteed outcomes

The decision layer is designed to support user guidance and system stability,
not to automate irreversible actions or enforce mandatory behavior.
