from fastapi import FastAPI
import asyncio
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI ()
@app.get ("/")
def read_root () :
    return FileResponse(FRONTEND_DIR / "house_form.html")

@app.get ( "/hello/{name}") # path parameter
def hello (name: str) :
    return {"greeting" : f"Hello {name}"}

@app.get ("/add") # query params : /add?a=2&b=3
async def add(a: int, b: int) :
    await asyncio.sleep(3)  # Simulate a delay
    return {"a": a, "b": b, "sum": a + b}

def predict_price(area: float, bedrooms: int, location: str) -> float:
    base_price = 500_000_000
    price_per_area = 15_000_000 * area
    price_per_bedroom = 50_000_000 * bedrooms

    total_price = base_price + price_per_area + price_per_bedroom

    if location.lower() == "hanoi":
        total_price *= 1.3
    elif location.lower() == "hcmc":
        total_price *= 1.25

    return round(total_price / 1_000_000) * 1_000_000

@app.get("/predict")
def predict(area: float, bedrooms: int, location: str):
    price = predict_price(area, bedrooms, location)
    return {"predicted_price": f"{price:,} VND"}

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
