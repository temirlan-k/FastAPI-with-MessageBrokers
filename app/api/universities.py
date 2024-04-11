import json
import httpx
from app.schemas.schema import University  

def get_all_universities_for_country(country: str) -> dict:
    url = 'http://universities.hipolabs.com/search'
    params = {'country': country}
    client = httpx.Client()
    response = client.get(url, params=params)
    response_json = response.json()
    universities = []
    for university_data in response_json:
        university_obj = University(**university_data)
        universities.append(university_obj)
    return {country: universities}
