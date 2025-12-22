from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from app.otel import setup_tracing

setup_tracing("product")

app = FastAPI(title="Product Service")
FastAPIInstrumentor.instrument_app(app)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/product/{product_id}")
def get_product(product_id: int):
    return {"id": product_id, "name": "Demo Product", "price": 100}

