import pandas as pd
import os

def load_routes():
    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    file_path = os.path.join(base_dir, "data", "aviation", "routes.csv")

    print(f"📂 Cargando rutas desde: {file_path}")

    columns = [
        "airline", "airline_id",
        "source_airport", "source_id",
        "destination_airport", "destination_id",
        "codeshare", "stops", "equipment"
    ]

    df = pd.read_csv(file_path, header=None, names=columns)

    return df