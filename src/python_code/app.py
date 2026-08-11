from fastapi import FastAPI
import numpy as np

app = FastAPI()

numbers = np.array([10, 20, 30, 40])


@app.get("/")
def home():
    return {"message": "OK", "list": numbers.tolist()}
