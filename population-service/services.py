import requests
from datetime import datetime
from predict import linear_prediction


BASE_URL = "https://api.worldbank.org/v2/country"


def fetch_population(country, year):
    url = f"{BASE_URL}/{country}/indicator/SP.POP.TOTL?date={year}&format=json"
    response = requests.get(url)
    data = response.json()

    if not data or len(data) < 2 or not data[1]:
        return None

    value = data[1][0]["value"]

    return value 

def get_population(country, year):
    population = fetch_population(country, year)

    return {
        "country": country,
        "year": year,
        "population": population,
    }


def predict_population(country, future_year):
    current_year = datetime.now().year

    years = []
    values = []

    for y in range(current_year - 10, current_year + 1):
        pop = fetch_population(country, y)

        if pop is not None:
            years.append(y)
            values.append(pop)

    if len(years) < 2:
        raise Exception("Not enough data for prediction")

    prediction = linear_prediction(years, values, future_year)

    return {
        "country": country,
        "year": future_year,
        "population": prediction,
    }