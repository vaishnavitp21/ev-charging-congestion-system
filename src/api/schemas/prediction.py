from pydantic import BaseModel
from typing import List
from datetime import datetime


class DemandConfidenceInterval(BaseModel):
    lower: float
    upper: float


class HourlyPrediction(BaseModel):
    hour: int
    predicted_demand: float
    demand_ci: DemandConfidenceInterval
    estimated_wait_time_minutes: float
    congestion_risk: str
    recommendation: str


class PredictionRequest(BaseModel):
    station_id: str
    date: str
    start_hour: int
    end_hour: int


class PredictionResponse(BaseModel):
    station_id: str
    date: str
    generated_at: datetime
    hourly_forecast: List[HourlyPrediction]
