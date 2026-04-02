import pandas as pd
import os

def load_airports():
    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    file_path = os.path.join(base_dir, "data", "aviation", "airports.csv")

    print(f"📂 Cargando aeropuertos desde: {file_path}")

    columns = [
        "id", "name", "city", "country",
        "iata", "icao",
        "lat", "lon",
        "altitude", "timezone", "dst",
        "tz_database", "type", "source"
    ]

    df = pd.read_csv(file_path, header=None, names=columns)

    return df