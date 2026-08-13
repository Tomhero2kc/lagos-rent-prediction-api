from pathlib import Path

import joblib
import pandas as pd


project_folder = Path(__file__).resolve().parent.parent
model_file = project_folder / "model" / "rent_model.joblib"


def predict_rent(location, property_type, bedrooms, bathrooms):
    model = joblib.load(model_file)

    property_details = pd.DataFrame(
        [
            {
                "location": location,
                "property_type": property_type,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
            }
        ]
    )

    prediction = model.predict(property_details)[0]

    return round(prediction)


def main():
    print("Lagos Rent Estimator")
    print("-" * 30)

    location = input("Location: ").strip()
    property_type = input("Property type: ").strip()
    bedrooms = int(input("Number of bedrooms: "))
    bathrooms = int(input("Number of bathrooms: "))

    estimated_rent = predict_rent(
        location,
        property_type,
        bedrooms,
        bathrooms,
    )

    print(
        f"\nEstimated annual rent: "
        f"₦{estimated_rent:,.0f}"
    )


if __name__ == "__main__":
    main()