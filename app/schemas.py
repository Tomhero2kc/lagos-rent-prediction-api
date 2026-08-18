from pydantic import BaseModel, ConfigDict, Field


class PropertyDetails(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    location: str = Field(min_length=2, max_length=50)
    property_type: str = Field(min_length=2, max_length=30)
    bedrooms: int = Field(gt=0, le=10)
    bathrooms: int = Field(gt=0, le=10)