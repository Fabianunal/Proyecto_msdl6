from fastapi import FastAPI # importamos el API
from pydantic import BaseModel
from typing import List
import joblib # importamos la librería para cargar el modelo

class ApiInput(BaseModel):
    texts: List[str]

class ApiOutput(BaseModel):
    is_hate: List[int]

app = FastAPI() # creamos el api
rf_classifier = joblib.load("rf_classifier.joblib") # cargamos el modelo.

@app.post("/IED") # creamos api que permita requests de tipo post.
async def create_user(data: ApiInput) -> ApiOutput:
    predictions = rf_classifier.predict(X_test) # generamos la predicción
    preds = ApiOutput(is_IED=predictions) # estructuramos la salida del API.
    return preds # retornamos los resultados
