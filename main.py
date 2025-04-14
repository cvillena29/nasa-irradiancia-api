from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/irradiancia")
def get_irradiancia(lat: float, lon: float, fecha: str):
    try:
        param = "ALLSKY_SFC_SW_DWN"
        url = (
            f"https://power.larc.nasa.gov/api/temporal/daily/point?"
            f"parameters={param}&community=RE&longitude={lon}&latitude={lat}"
            f"&start={fecha}&end={fecha}&format=JSON"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        valor = data["properties"]["parameter"][param][fecha]
        return {
            "fecha": fecha,
            "lat": lat,
            "lon": lon,
            "valor_kWh_m2": valor
        }
    except Exception as e:
        return {"error": str(e)}
