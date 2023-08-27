from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)