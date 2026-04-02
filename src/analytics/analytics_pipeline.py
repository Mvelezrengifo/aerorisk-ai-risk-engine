from route_segmentation import segment_route
from climate_lookup import find_climate_cell
from route_risk import compute_route_risk


def run_route_analysis():

    # ruta de ejemplo
    start_lat = 4.7016
    start_lon = -74.1469

    end_lat = 40.4168
    end_lon = -3.7038

    # clima simulado por ahora
    climate_cells = [
        {"lat": 5.0, "lon": -73.0, "risk": 0.3},
        {"lat": 15.0, "lon": -40.0, "risk": 0.6},
        {"lat": 40.0, "lon": -3.0, "risk": 0.8},
    ]

    result = compute_route_risk(
        start_lat,
        start_lon,
        end_lat,
        end_lon,
        climate_cells
    )

    print("Route Analysis Result")
    print(result)


if __name__ == "__main__":
    run_route_analysis()