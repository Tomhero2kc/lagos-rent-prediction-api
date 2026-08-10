from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


project_folder = Path(__file__).resolve().parent.parent

data_file = project_folder / "data" / "lagos_rent_data.csv"
model_file = project_folder / "model" / "rent_model.joblib"


def train_model():
    rent_data = pd.read_csv(data_file)

    features = rent_data[
        ["location", "property_type", "bedrooms", "bathrooms"]
    ]

    rent_prices = rent_data["annual_rent"]

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        rent_prices,
        test_size=0.25,
        random_state=42,
    )

    text_columns = ["location", "property_type"]

    preparation = ColumnTransformer(
        [
            (
                "text",
                OneHotEncoder(handle_unknown="ignore"),
                text_columns,
            )
        ],
        remainder="passthrough",
    )

    model = Pipeline(
        [
            ("preparation", preparation),
            (
                "rent_model",
                RandomForestRegressor(
                    n_estimators=150,
                    random_state=42,
                ),
            ),
        ]
    )

    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    average_error = mean_absolute_error(y_test, predictions)

    joblib.dump(model, model_file)

    print("Rent prediction model trained successfully.")
    print(f"Listings used: {len(rent_data)}")
    print(f"Average prediction error: ₦{average_error:,.0f}")
    print(f"Model saved to: {model_file}")


if __name__ == "__main__":
    train_model()