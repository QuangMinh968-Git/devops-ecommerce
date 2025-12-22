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

