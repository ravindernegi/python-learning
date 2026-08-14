from fastapi import FastAPI
import uvicorn
from .models import Product
from .database import session_local, engine
from python_code import db_models

app = FastAPI()

db_models.Base.metadata.create_all(bind=engine)
products = [
    Product(id=1, name="Test", price=45.2, quantity=50),
    Product(id=2, name="Test 1", price=78.5, quantity=23),
    Product(id=3, name="Test 2", price=89, quantity=52),
    Product(id=4, name="Test 4", price=785, quantity=585),
    Product(id=5, name="Test 5", price=12054, quantity=435),
]


@app.get("/")
def home():
    return {
        "message": "OK",
    }


@app.get("/products")
def get_products():
    db = session_local()
    db.query()
    return products


@app.post("/product")
def add_products():
    return products


def main():
    uvicorn.run("python_code.app:app", reload=True)
