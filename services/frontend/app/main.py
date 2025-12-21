from fastapi import FastAPI

app = FastAPI(title="Frontend Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/checkout")
def checkout():
    return {
        "message": "Order received",
        "status": "CREATED"
    }

