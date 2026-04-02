import csv
import sys
import os

# Esto asegura que encuentre a su vecino 'global_route_study'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import global_route_study


class RiskStatistics:
    def __init__(self, dataset="route_risk_results.csv"):
        self.dataset = dataset

    def compute_statistics(self, data):
        if not data:
            return {"status": "No hay datos"}

        avg_risks = [d["avg_risk"] for d in data]
        return {
            "average_risk": sum(avg_risks) / len(avg_risks),
            "max_risk": max([d["max_risk"] for d in data]),
            "total_routes": len(data)
        }


def main():
    print("🚀 Iniciando AeroClimate Analytics...")

    # Obtenemos los datos del otro script
    results = global_route_study.run_global_route_study()

    # Calculamos estadísticas
    stats_calc = RiskStatistics()
    res = stats_calc.compute_statistics(results)

    print("\n--- ESTADÍSTICAS DE RIESGO ---")
    print(res)
    print("\n✅ Proceso completado con éxito.")


if __name__ == "__main__":
    main()