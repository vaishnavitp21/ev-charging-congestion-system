from typing import List, Dict


def run_target(
    station_id: str,
    date: str,
    start_hour: int,
    end_hour: int,
) -> List[Dict]:
    """
    Core prediction pipeline entrypoint.
    Called by:
    - FastAPI (/predict)
    - Streamlit dashboard
    """

    results = []

    for hour in range(start_hour, end_hour):
        predicted_demand = 42.0 + (hour % 3)  # deterministic placeholder
        wait_time = 5.0 + (hour % 4)

        if wait_time < 7:
            risk = "LOW"
            recommendation = "Charge now"
        elif wait_time < 10:
            risk = "MEDIUM"
            recommendation = "Consider off-peak hours"
        else:
            risk = "HIGH"
            recommendation = "Delay charging"

        results.append(
            {
                "hour": hour,
                "predicted_demand": predicted_demand,

                # 🔑 REQUIRED BY SCHEMA
                "demand_ci": {
                    "lower": predicted_demand - 3.0,
                    "upper": predicted_demand + 3.0,
                },

                "estimated_wait_time_minutes": wait_time,
                "congestion_risk": risk,
                "recommendation": recommendation,
            }
        )

    return results
