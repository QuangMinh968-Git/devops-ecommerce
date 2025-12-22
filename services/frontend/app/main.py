from fastapi import FastAPI
import requests

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from app.otel import setup_tracing

setup_tracing("frontend")

app = FastAPI(title="Frontend Service")

FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
def checkout():
    r = requests.post("http://checkout/checkout")
    return r.json()

