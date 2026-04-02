import math


def distance(lat1, lon1, lat2, lon2):
    """
    Distancia simple entre dos puntos geográficos.
    """

    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)


def find_climate_cell(lat, lon, climate_cells):
    """
    Encuentra la celda climática más cercana a un punto.
    """

    closest_cell = None
    min_distance = float("inf")

    for cell in climate_cells:

        cell_lat = cell["lat"]
        cell_lon = cell["lon"]

        d = distance(lat, lon, cell_lat, cell_lon)

        if d < min_distance:
            min_distance = d
            closest_cell = cell

    return closest_cell

if __name__ == "__main__":

    climate_cells = [
        {"lat": 5.0, "lon": -73.0, "risk": 0.3},
        {"lat": 10.0, "lon": -60.0, "risk": 0.5},
        {"lat": 40.0, "lon": -3.0, "risk": 0.7},
    ]

    lat = 5.2
    lon = -72.8

    cell = find_climate_cell(lat, lon, climate_cells)

    print("Closest climate cell:")
    print(cell)