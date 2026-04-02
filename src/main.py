import sys
import os
from google.cloud import bigquery
import pandas as pd

# Manejo de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Imports
try:
    # ... (tus otros imports se mantienen igual)
    from api.risk_service import get_risk_by_iata
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    sys.exit(1)


def main():
    print("\n" + "=" * 40)
    print("   AERORISK PIPELINE - CLOUD READY")
    print("=" * 40 + "\n")

    # 0️⃣ INICIALIZACIÓN DE BIGQUERY
    try:
        client = bigquery.Client(project="aerorisk-platform")
        print("✅ Conexión exitosa a BigQuery\n")
    except Exception as e:
        print(f"❌ Error conectando a Google Cloud: {e}")
        return

    # --- CONSULTAS INDIVIDUALES (BOG Y CNP) ---
    print("🔍 Consultando riesgo específico por IATA...")

    # Prueba 1: BOG
    res_bog = get_risk_by_iata("BOG")
    print(f"   -> Resultado para BOG: {res_bog}")

    # Prueba 2: CNP (Neoclí / Nuevo)
    res_cnp = get_risk_by_iata("CNP")
    print(f"   -> Resultado para CNP: {res_cnp}\n")

    # 1️⃣ WEATHER ENGINE (Agregamos un try/except para que el error de cfgrib no mate el proceso)
    print("🛰️  Fase 1: Cargando datos meteorológicos...")
    try:
        from climate.weather_loader import load_weather_dataset
        weather_data = load_weather_dataset()
    except Exception as e:
        print(f"   ⚠️ Error en Fase 1 (Meteorología): {e}")
        print("   💡 Tip: Revisa la instalación de 'cfgrib' y 'eccodes' en tu entorno conda.")
        # Si prefieres que el programa se detenga aquí, deja el sys.exit(1)
        # sys.exit(1)

    # ... Resto del pipeline (Fase 2 a 7)
    print("\n✅ PROCESO DE CONSULTA FINALIZADO\n")


if __name__ == "__main__":
    main()