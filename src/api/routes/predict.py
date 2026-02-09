from fastapi import APIRouter
from src.api.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)
from src.run_target import run_target
from datetime import datetime

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    results = run_target(
        station_id=request.station_id,
        date=request.date,
        start_hour=request.start_hour,
        end_hour=request.end_hour,
    )

    return PredictionResponse(
        station_id=request.station_id,
        date=request.date,
        generated_at=datetime.utcnow(),
        hourly_forecast=results,
    )
