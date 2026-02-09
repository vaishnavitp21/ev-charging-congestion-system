import streamlit as st
import requests
from datetime import date

# ---------------------------------------------------
# Page config
# ---------------------------------------------------
st.set_page_config(
    page_title="EV Charging Congestion Dashboard",
    layout="wide",
)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("EV Charging Congestion Prediction System")

st.markdown(
    """
This dashboard visualizes **real-time outputs** from the EV charging
congestion prediction system.

- Hourly demand forecasts  
- Estimated waiting times  
- Congestion risk levels  
- Actionable recommendations  
"""
)

# ---------------------------------------------------
# Input controls
# ---------------------------------------------------
st.subheader("Select Query Parameters")

col1, col2, col3, col4 = st.columns(4)

with col1:
    station_id = st.text_input(
        "Station ID",
        value="STATION_001",
    )

with col2:
    selected_date = st.date_input(
        "Date",
        value=date.today(),
    )

with col3:
    start_hour = st.selectbox(
        "Start Hour",
        options=list(range(0, 24)),
        index=8,
    )

with col4:
    end_hour = st.selectbox(
        "End Hour",
        options=list(range(1, 25)),
        index=12,
    )

st.divider()

# ---------------------------------------------------
# Prediction trigger
# ---------------------------------------------------
prediction_data = None

if st.button("Run Prediction"):
    payload = {
        "station_id": station_id,
        "date": selected_date.strftime("%Y-%m-%d"),
        "start_hour": start_hour,
        "end_hour": end_hour,
    }

    with st.spinner("Fetching predictions..."):
        response = requests.post(
            "http://localhost:8000/predict",
            json=payload,
            timeout=10,
        )

    if response.status_code != 200:
        st.error("Failed to fetch predictions from API")
    else:
        prediction_data = response.json()
        st.success("Prediction fetched successfully")

# ---------------------------------------------------
# Render results (ONLY if prediction exists)
# ---------------------------------------------------
if prediction_data:
    hourly_data = prediction_data["hourly_forecast"]

    st.subheader("Hourly Forecast Results")

    for row in hourly_data:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)

            col1.metric("Hour", row["hour"])
            col2.metric(
                "Demand",
                f'{row["predicted_demand"]:.2f}',
            )
            col3.metric(
                "Wait (min)",
                f'{row["estimated_wait_time_minutes"]:.1f}',
            )

            risk = row["congestion_risk"]

            if risk == "LOW":
                col4.markdown("🟢 **LOW**")
            elif risk == "MEDIUM":
                col4.markdown("🟡 **MEDIUM**")
            else:
                col4.markdown("🔴 **HIGH**")

            col5.write(row["recommendation"])

        st.divider()
