from fastapi import FastAPI
from src.api.routes import predict_router
from src.api.middleware.logging import request_logger

app = FastAPI(
    title="EV Charging Congestion Prediction API",
    version="1.0.0",
)

app.middleware("http")(request_logger)

app.include_router(predict_router)
