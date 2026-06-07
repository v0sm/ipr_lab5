from datetime import datetime, timezone
import os
import platform
import socket

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="lab5-fastapi-backend", version="1.0.0")

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_endpoint() -> dict[str, str]:
    return {
        "status": "healthy",
        "service_name": "backend-core",
        "current_time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/info")
@app.get("/api/info")
def info_endpoint() -> dict[str, str | bool]:
    try:
        host_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        host_ip = "unknown"

    return {
        "service": "серверная часть",
        "framework": "FastAPI",
        "message": "Компоненты лабораторной работы №5 успешно запущены",
        "environment": os.getenv("APP_ENV", "разработка"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "pod_name": os.getenv("HOSTNAME", socket.gethostname()),
        "pod_ip": host_ip,
        "os_platform": platform.system(),
        "secret_loaded": bool(os.getenv("DEMO_API_KEY")),
        "time": datetime.now(timezone.utc).isoformat(),
    }
