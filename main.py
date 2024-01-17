# Imports
from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
import sqlite3
import yaml
import pickle

# Import du fichier YAML : config du projet
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# ----------------
app = FastAPI()

with open('models/model_dtr.pkl', "rb") as model_file:
    model = pickle.load(model_file)

with open('models/model_rfr.pkl', "rb") as model_rfr_file:
    model_rfr = pickle.load(model_rfr_file)

@app.on_event("startup")
def load_models():
    global model, model_rfr
    

# Root
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict")
async def predict(longitude: float, latitude: float):
    try:
        # Create a NumPy array from the input data
        input_array = np.array([[longitude, latitude]])

        # Use the loaded model to make predictions
        prediction = model.predict(input_array)

        # Return the prediction as JSON
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {str(e)}")
    

@app.get("/predict_rfr")
async def predict_rfr(longitude: float, latitude: float, type_Appartement: bool, type_Maison: bool, vefa: bool, n_pieces: int, surface_habitable: int):
    try:
        # Create a NumPy array from the input data
        input_array = np.array([[longitude, latitude, type_Appartement, type_Maison, vefa, n_pieces, surface_habitable]])

        # Use the loaded model to make predictions
        prediction = model_rfr.predict(input_array)

        # Return the prediction as JSON
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making prediction: {str(e)}")