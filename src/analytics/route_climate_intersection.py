import math


def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c


def route_distance():

    bogota = (4.7016, -74.1469)
    madrid = (40.4168, -3.7038)

    dist = haversine(
        bogota[0], bogota[1],
        madrid[0], madrid[1]
    )

    return dist


if __name__ == "__main__":

    d = route_distance()

    print("Distance Bogotá → Madrid:", round(d,2), "km")