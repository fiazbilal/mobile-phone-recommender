# app/main.py
from fastapi import FastAPI
from app.routes import health

app = FastAPI(
    title="Health Check API",
    description="Simple backend service with health check endpoint",
    version="0.1.0"
)

# Include router from routes
app.include_router(health.router)
