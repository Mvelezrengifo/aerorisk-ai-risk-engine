import csv
import os


class GlobalRiskMap:
    def __init__(self, dataset):
        self.dataset = dataset

    def load_data(self):
        rows = []
        if not os.path.exists(self.dataset):
            print(f"⚠️ Archivo {self.dataset} no encontrado.")
            return []

        with open(self.dataset, "r") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append({
                    "origin": r["origin"],
                    "destination": r["destination"],
                    "avg_risk": float(r["avg_risk"]),
                    "max_risk": float(r["max_risk"])
                })
        return rows


# ESTA ES LA FUNCIÓN QUE EL MAIN BUSCA
def generate_global_risk_map(dataset="route_risk_results.csv"):
    print(f"🗺️  Generando mapa global desde: {dataset}")

    # Usamos tu clase interna para cargar los datos
    map_engine = GlobalRiskMap(dataset)
    data = map_engine.load_data()

    if data:
        print(f"✅ Se cargaron {len(data)} rutas para el mapa.")
    else:
        print("⚠️ No hay datos suficientes para visualizar el mapa.")


if __name__ == "__main__":
    # Prueba local
    generate_global_risk_map("route_risk_results.csv")