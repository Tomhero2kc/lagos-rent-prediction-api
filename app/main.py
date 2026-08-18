from fastapi import FastAPI

from app.prediction import predict_rent
from app.schemas import PropertyDetails

app = FastAPI(title="Lagos Rent Prediction API")





@app.get("/")
def home():
    return {
        "message": "Lagos Rent Prediction API is running"
    }


@app.post("/predict")
def get_prediction(property_details: PropertyDetails):
    estimated_rent = predict_rent(
        property_details.location,
        property_details.property_type,
        property_details.bedrooms,
        property_details.bathrooms,
    )

    return {
        "estimated_annual_rent": estimated_rent
    }