# Lagos Rent Prediction API

I built this project as part of my practice with Python, machine learning and APIs.

The idea is simple: you provide a few details about a property in Lagos, such as the location, property type, number of bedrooms and bathrooms, and the API returns an estimated annual rent.

The dataset used here was created for practice, so the predictions should not be treated as current Lagos market prices.

## What the Project Does

- Uses a small Lagos rent dataset
- Trains a rent prediction model
- Accepts property details through an API
- Returns an estimated annual rent
- Checks for invalid inputs
- Includes basic tests to make sure the API works

## Project Structure

```text
lagos-rent-prediction-api/
├── app/
│   ├── main.py
│   ├── prediction.py
│   └── schemas.py
├── data/
│   └── lagos_rent_data.csv
├── model/
│   ├── train_model.py
│   └── rent_model.joblib
├── tests/
│   └── test_api.py
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run It

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Train the model:

```bash
python model/train_model.py
```

Start the API:

```bash
python -m uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Example Prediction

Example request:

```json
{
  "location": "Yaba",
  "property_type": "Flat",
  "bedrooms": 2,
  "bathrooms": 2
}
```

Example response from one of my tests:

```json
{
  "estimated_annual_rent": 3026000
}
```

The exact prediction can change if the model or training data changes.

## Input Checks

The API checks that the property details make sense before making a prediction.

For example, a request with `0` bedrooms is rejected instead of being passed to the model.

## Tests

I added a few basic tests for:

- The home endpoint
- A valid rent prediction request
- An invalid request with zero bedrooms

Run the tests with:

```bash
python -m pytest -q
```

My current tests return:

```text
3 passed
```

## What I Learned

While building this project, I practised:

- Preparing data for a machine learning model
- Training and saving a prediction model
- Using FastAPI
- Working with JSON requests and responses
- Checking user input
- Testing API endpoints
- Organising a Python project into separate folders

## Note

This is a learning project and the dataset is not live property-market data. The estimates are for demonstration and practice only.