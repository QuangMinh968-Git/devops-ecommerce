from fastapi import FastAPI
import requests

app = FastAPI(title="Checkout Service")

PRODUCT_SERVICE_URL = "http://product"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
def checkout():
    product = requests.get(f"{PRODUCT_SERVICE_URL}/product/1").json()

    return {
        "message": "Checkout success",
        "product": product
    }

