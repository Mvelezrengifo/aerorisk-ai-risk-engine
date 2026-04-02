import pandas as pd
from api import route_risk


def run_global_route_study(routes_df, airports_df, climate_cells):

    results = []

    # ================================
    # 1. LIMPIAR Y CREAR AEROPUERTOS
    # ================================
    airport_dict = {}

    for _, row in airports_df.iterrows():
        try:
            iata = str(row["iata"]).strip().upper()

            # 🚫 invalid IATA
            if iata in ["", "\\N", "NAN"]:
                continue

            lat = row["lat"]
            lon = row["lon"]

            # 🚫 CLAVE: filtrar None / NaN reales
            if pd.isna(lat) or pd.isna(lon):
                continue

            lat = row["lat"]
            lon = row["lon"]

            if pd.isna(lat) or pd.isna(lon):
                continue

            lat = row["lat"]
            lon = row["lon"]

            if pd.isna(lat) or pd.isna(lon):
                continue

            lat = float(lat)
            lon = float(lon)

            airport_dict[iata] = (lat, lon)

        except:
            continue

    print(f"✈️ Aeropuertos válidos: {len(airport_dict)}")

    # ================================
    # 2. LIMPIAR RUTAS
    # ================================
    routes_df["source_airport"] = routes_df["source_airport"].astype(str).str.strip().str.upper()
    routes_df["destination_airport"] = routes_df["destination_airport"].astype(str).str.strip().str.upper()

    # 🚫 eliminar basura
    routes_df = routes_df[
        (routes_df["source_airport"] != "\\N") &
        (routes_df["destination_airport"] != "\\N")
    ]

    # ================================
    # 3. FILTRAR SOLO RUTAS VÁLIDAS
    # ================================
    routes_df = routes_df[
        routes_df["source_airport"].isin(airport_dict.keys()) &
        routes_df["destination_airport"].isin(airport_dict.keys())
    ]

    print(f"🌍 Rutas válidas encontradas: {len(routes_df)}")

    # 🔥 IMPORTANTE: si esto da 0, aquí estaba tu problema
    if len(routes_df) == 0:
        print("❌ No hay rutas válidas después del filtro")
        return []

    # ================================
    # 4. PROCESAR RUTAS (PRUEBA)
    # ================================
    for _, row in routes_df.head(300).iterrows():

        try:
            origin_code = row["source_airport"]
            dest_code = row["destination_airport"]

            slat, slon = airport_dict[origin_code]
            elat, elon = airport_dict[dest_code]

            risk = route_risk.compute_route_risk(
                slat, slon, elat, elon, climate_cells
            )

            results.append({
                "origin": origin_code,
                "destination": dest_code,
                "avg_risk": risk["avg_risk"],
                "max_risk": risk["max_risk"],
                "segments": risk["segments"]
            })


        except Exception as e:

            print(f"❌ ERROR en ruta {origin_code} -> {dest_code}: {e}")

            continue

    print(f"🌍 Rutas procesadas: {len(results)}")

    return results