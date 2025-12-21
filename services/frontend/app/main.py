from fastapi import FastAPI
import requests

app = FastAPI(title="Frontend Service")

CHECKOUT_SERVICE_URL = "http://checkout"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
def checkout():
    response = requests.post(f"{CHECKOUT_SERVICE_URL}/checkout")
    return response.json()

