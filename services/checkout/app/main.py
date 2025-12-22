from fastapi import FastAPI
import requests

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from app.otel import setup_tracing

setup_tracing("checkout")

app = FastAPI(title="Checkout Service")

FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

PRODUCT_SERVICE_URL = "http://product"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
def checkout():
    product = requests.get(f"{PRODUCT_SERVICE_URL}/product/1").json()
    return {"message": "Checkout success", "product": product}

from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Response
import time

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency",
    ["endpoint"]
)

@app.middleware("http")
async def metrics_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    REQUEST_COUNT.labels(
        request.method,
        request.url.path,
        response.status_code
    ).inc()
    REQUEST_LATENCY.labels(request.url.path).observe(duration)
    return response

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

