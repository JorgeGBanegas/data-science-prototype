from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from prophet import Prophet
import json
import matplotlib.pyplot as plt
import statsmodels.api as sm
from fastapi.responses import JSONResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carga el modelo de Random Forest
rf_model = joblib.load('modelo_random_forest.pkl')

class PropertyFeatures(BaseModel):
    BedroomAbvGr: int
    FullBath: int
    LotArea: float
    GrLivArea: float

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict_property_price(features: PropertyFeatures):
    try:
        input_data = [[features.BedroomAbvGr, features.FullBath, features.LotArea, features.GrLivArea]]
        prediction = rf_model.predict(input_data)
        predicted_price = prediction[0]
        return {"predicted_price": predicted_price}
    
    except Exception as e:
        print(e)
        return {"error": e}




df = pd.read_csv("train.csv")


@app.get("/analisis-tendencias")
def analisis_tendencias():
    # Analiza el dataset para identificar tendencias
    años_unicos = df['YrSold'].unique()
    años_unicos.sort()

    años = np.array(años_unicos).reshape(-1, 1)
    precios_promedio = np.array([df[df['YrSold'] == año]['SalePrice'].mean() for año in años_unicos])
    print(años)
    # Entrenar el modelo de regresión lineal
    modelo = LinearRegression()
    modelo.fit(años, precios_promedio)
    tendencia = modelo.predict(años)
    # Crear el gráfico
    # Crear el gráfico de barras
    '''plt.figure(figsize=(10, 6))
    plt.bar(años_unicos, precios_promedio, color='blue', label='Precios Promedio')
    plt.plot(años_unicos, tendencia, color='red', label='Tendencia')
    plt.xlabel('Años')
    plt.ylabel('Precio Promedio de Venta')
    plt.title('Tendencias del Mercado Inmobiliario')
    plt.legend()
    plt.grid(True)
    plt.show()'''
    
    return {
        "anyos": años_unicos.tolist(),
        "precios_promedio": precios_promedio.tolist(),
        "tendencia": tendencia.tolist()
    }




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)