import requests
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("API_KEY")

print("API carregada:", api_key is not None)


def get_lat_lon(city_name, state_code, country_code, api_key):
    url = (
        f"http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city_name},{state_code},{country_code}"
        f"&limit=1&appid={api_key}"
    )

    resp = requests.get(url).json()

    if not resp:
        print("Cidade não encontrada.")
        return None, None

    lat = resp[0]["lat"]
    lon = resp[0]["lon"]

    print("Latitude:", lat)
    print("Longitude:", lon)

    return lat, lon


get_lat_lon("São Paulo", "SP", "BR", api_key)


def get_weather(lat, lon, api_key):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}"
        f"&appid={api_key}"
        "&units=metric"
        "&lang=pt_br"
    )

    resp = requests.get(url).json()

    if "main" not in resp:
        print("Erro ao buscar clima:", resp)
        return None

    return {
        "temperatura": resp["main"]["temp"],
        "minima": resp["main"]["temp_min"],
        "maxima": resp["main"]["temp_max"],
        "umidade": resp["main"]["humidity"],
        "descricao": resp["weather"][0]["description"]
    }


lat, lon = get_lat_lon("São Paulo", "SP", "BR", api_key)

if lat is not None and lon is not None:
    clima = get_weather(lat, lon, api_key)
    print(clima)
