from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path
import requests
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
api_key = os.getenv("API_KEY")

print("API carregada:", api_key is not None)

app = Flask(__name__)
CORS(app)


def get_lat_lon(city_name, state_code, country_code, api_key):
    url = (
        f"http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city_name},{state_code},{country_code}"
        f"&limit=1&appid={api_key}"
    )
    resp = requests.get(url).json()
    if not resp:
        return None, None
    return resp[0]["lat"], resp[0]["lon"]


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
        return None
    return {
        "temperatura": resp["main"]["temp"],
        "minima": resp["main"]["temp_min"],
        "maxima": resp["main"]["temp_max"],
        "umidade": resp["main"]["humidity"],
        "descricao": resp["weather"][0]["description"],
    }


@app.route("/clima")
def clima():
    cidade = request.args.get("cidade", "São Paulo")
    estado = request.args.get("estado", "SP")
    pais = request.args.get("pais", "BR")

    lat, lon = get_lat_lon(cidade, estado, pais, api_key)
    if lat is None:
        return jsonify({"erro": "Cidade não encontrada"}), 404

    resultado = get_weather(lat, lon, api_key)
    if resultado is None:
        return jsonify({"erro": "Não foi possível buscar o clima"}), 502

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
