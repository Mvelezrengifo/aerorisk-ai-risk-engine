from google.cloud import bigquery
import random

# Cliente global (ya autenticado con gcloud)
client = bigquery.Client(project="aerorisk-platform")

# --- FUNCIÓN 1: Consulta Individual (Aeropuerto Específico) ---
def get_risk_by_iata(iata_code: str):
    """
    Obtiene información básica de ubicación de un solo aeropuerto.
    """
    query = f"""
    SELECT
        string_field_1 AS airport_name,
        string_field_2 AS city,
        string_field_3 AS country,
        string_field_4 AS iata,
        double_field_6 AS latitude,
        double_field_7 AS longitude
    FROM aerorisk_data.airport_risk
    WHERE string_field_4 = '{iata_code.upper()}'
    LIMIT 1
    """
    try:
        results = client.query(query).result()
        for row in results:
            return {
                "airport": row.airport_name,
                "city": row.city,
                "country": row.country,
                "iata": row.iata,
                "latitude": row.latitude,
                "longitude": row.longitude
            }
        return {"error": f"No se encontró el aeropuerto: {iata_code}"}
    except Exception as e:
        return {"error": str(e)}


# --- FUNCIÓN 2: Consulta de Ruta (Inteligencia de Negocio) ---
def get_route_risk(origin: str, destination: str):
    """
    Calcula el riesgo y obtiene detalles de la ruta entre dos puntos.
    """
    query = f"""
    SELECT
        codigo_origen,
        codigo_destino,
        nombre_aeropuerto_origen,
        ciudad_origen,
        pais_origen,
        nombre_aeropuerto_destino,
        ciudad_destino,
        pais_destino
    FROM aerorisk_data.v_rutas_detalladas
    WHERE codigo_origen = '{origin.upper()}'
    AND codigo_destino = '{destination.upper()}'
    LIMIT 1
    """

    try:
        results = client.query(query).result()

        for row in results:
            # --- LÓGICA DE RIESGO (Simulación NOAA para el MVP) ---
            score = round(random.uniform(10, 95), 2)

            if score > 80:
                level = "CRÍTICO"
                recommendation = "Desvío recomendado por tormentas severas."
            elif score > 50:
                level = "MEDIO"
                recommendation = "Precaución: Turbulencia moderada en ruta."
            else:
                level = "BAJO"
                recommendation = "Ruta despejada. Condiciones óptimas."

            return {
                "route": f"{row.codigo_origen} → {row.codigo_destino}",
                "risk_score": score,
                "risk_level": level,
                "ai_recommendation": recommendation,
                "details": {
                    "origin": f"{row.nombre_aeropuerto_origen} ({row.ciudad_origen})",
                    "destination": f"{row.nombre_aeropuerto_destino} ({row.ciudad_destino})"
                }
            }

        return {"error": f"Ruta no encontrada entre {origin} y {destination}"}
    except Exception as e:
        return {"error": str(e)}