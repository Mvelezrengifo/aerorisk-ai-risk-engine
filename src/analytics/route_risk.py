import sys
import os

# GPS: Asegura que encuentre a sus hermanos en la misma carpeta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from route_segmentation import segment_route
    from climate_lookup import find_climate_cell
except ImportError:
    from .route_segmentation import segment_route
    from .climate_lookup import find_climate_cell


def compute_route_risk(start_lat, start_lon, end_lat, end_lon, climate_cells):
    # 🔥 VALIDACIÓN FUERTE (esto es lo que te estaba matando)
    if start_lat is None or start_lon is None or end_lat is None or end_lon is None:
        return {"segments": 0, "avg_risk": 0.0, "max_risk": 0.0}

    try:
        points = segment_route(start_lat, start_lon, end_lat, end_lon)
    except:
        return {"segments": 0, "avg_risk": 0.0, "max_risk": 0.0}

    risks = []

    for lat, lon in points:

        # 🔥 validar punto
        if lat is None or lon is None:
            continue

        try:
            cell = find_climate_cell(lat, lon, climate_cells)
        except:
            continue

        # 🔥 VALIDACIÓN CLAVE (esto evita tu error)
        if not cell:
            continue

        if not isinstance(cell, dict):
            continue

        if "risk" not in cell:
            continue

        if cell["risk"] is None:
            continue

        risks.append(cell["risk"])

    if not risks:
        return {
            "segments": len(points),
            "avg_risk": 0.0,
            "max_risk": 0.0
        }

    avg_risk = sum(risks) / len(risks)
    max_risk = max(risks)

    return {
        "segments": len(points),
        "avg_risk": avg_risk,
        "max_risk": max_risk,
    }


if __name__ == "__main__":
    test_cells = [
        {"lat": 5.0, "lon": -73.0, "risk": 0.3},
        {"lat": 15.0, "lon": -40.0, "risk": 0.6},
        {"lat": 40.0, "lon": -3.0, "risk": 0.8},
    ]

    result = compute_route_risk(
        4.70159, -74.1469,  # Bogotá
        40.4168, -3.7038,  # Madrid
        test_cells
    )

    print("✅ Motor de Riesgo funcionando:")
    print(result)