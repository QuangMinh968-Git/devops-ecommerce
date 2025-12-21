from fastapi import FastAPI

app = FastAPI(title="Product Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/product/{product_id}")
def get_product(product_id: int):
    return {
        "id": product_id,
        "name": "Demo Product",
        "price": 100
    }

