from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel
import numpy as np
from .ml.model import get_model, Model

class PredictRequest(BaseModel):
    data: List[List[float]]

class PredictResponse(BaseModel):
    data: List[float]

app = FastAPI()

@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest, model: Model = Depends(get_model)):
    X = np.array(input.data)
    y_pred = model.predict(X)
    result = PredictResponse(data=y_pred.tolist())
    return result
