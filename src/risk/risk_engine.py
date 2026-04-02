from pathlib import Path
import xarray as xr


def compute_risk(climate_data):
    """
    Procesa el riesgo climático.
    Soporta tanto Datasets de xarray (Cloud/GRIB) como listas de celdas (Local).
    """
    risk_map = []

    # CASO A: Si recibimos una lista (Lo que viene del main.py actual)
    if isinstance(climate_data, list):
        print("🧬 Procesando riesgo en modo Local (Lista)...")
        for cell in climate_data:
            # Aquí va tu lógica de riesgo.
            # Por ahora asignamos un riesgo base (puedes usar cell['temp'])
            risk_score = cell.get("temp", 0) * 0.01

            risk_map.append({
                "lat": cell.get("lat"),
                "lon": cell.get("lon"),
                "risk": round(min(float(risk_score), 1.0), 2)
            })

    # CASO B: Si recibimos un Dataset de xarray (Lo que tienes en el script original)
    else:
        print("☁️ Procesando riesgo en modo Cloud/GRIB (xarray)...")
        lats = climate_data.latitude.values
        lons = climate_data.longitude.values

        for lat in lats:
            for lon in lons:
                risk_map.append({
                    "lat": float(lat),
                    "lon": float(lon),
                    "risk": 0.0  # Lógica base
                })

    return risk_map


# Mantén tu función de carga por si la usas luego
def load_weather():
    BASE_DIR = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_DIR / "data" / "weather" / "era5-levels-members.grib"
    if DATA_PATH.exists():
        return xr.open_dataset(DATA_PATH, engine="cfgrib")
    return None


if __name__ == "__main__":
    # Prueba local rápida
    test_data = [{"lat": 4.7, "lon": -74.1, "temp": 20}]
    print(compute_risk(test_data))