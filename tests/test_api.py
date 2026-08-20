from fastapi.testclient import TestClient

import app.main as main_module


client = TestClient(main_module.app)


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Lagos Rent Prediction API is running"
    }


def test_zero_bedrooms_is_rejected():
    property_details = {
        "location": "Yaba",
        "property_type": "Flat",
        "bedrooms": 0,
        "bathrooms": 2,
    }

    response = client.post("/predict", json=property_details)

    assert response.status_code == 422


def test_valid_property_returns_prediction(monkeypatch):
    monkeypatch.setattr(
        main_module,
        "predict_rent",
        lambda *args, **kwargs: 3026000,
    )

    property_details = {
        "location": "Yaba",
        "property_type": "Flat",
        "bedrooms": 2,
        "bathrooms": 2,
    }

    response = client.post("/predict", json=property_details)

    assert response.status_code == 200
    assert response.json() == {
        "estimated_annual_rent": 3026000
    }