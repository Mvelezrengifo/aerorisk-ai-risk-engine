import math


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcula distancia entre dos puntos geográficos en km.
    """

    R = 6371  # radio de la Tierra en km

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def segment_route(start_lat, start_lon, end_lat, end_lon, segment_km=50):
    """
    Divide una ruta en segmentos geográficos.
    """

    total_distance = haversine_distance(start_lat, start_lon, end_lat, end_lon)

    num_segments = max(1, int(total_distance / segment_km))

    points = []

    for i in range(num_segments + 1):

        fraction = i / num_segments

        lat = start_lat + (end_lat - start_lat) * fraction
        lon = start_lon + (end_lon - start_lon) * fraction

        points.append((lat, lon))

    return points
if __name__ == "__main__":

    # Bogotá
    start_lat = 4.70159
    start_lon = -74.1469

    # Madrid
    end_lat = 40.4168
    end_lon = -3.7038

    points = segment_route(start_lat, start_lon, end_lat, end_lon)

    print("Total segments:", len(points))

    print("\nFirst 5 points:")
    for p in points[:5]:
        print(p)