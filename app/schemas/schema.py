from pydantic import BaseModel

class Country(BaseModel):
    country:str


class University(BaseModel):
    name: str
    country: str
    domain: str

    class Config:
        allow_population_by_field_name = True