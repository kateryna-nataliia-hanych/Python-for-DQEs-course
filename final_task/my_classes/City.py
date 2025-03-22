import math
class City:
    def __init__(self, name, lon = None, lat = None):
        self.name = name
        self.lon = lon
        self.lat = lat

    def __repr__(self):
        print(f"City(name={self.name}, lon={self.lon}, lat={self.lat})")

    def distance_to_other_city(self, other_city):
        lat1, lon1 = self.lat, self.lon
        lat2, lon2 = other_city.lat, other_city.lon

        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = math.sin(delta_lat/2)**2 + math.cos(lat1) * math.cos(lat2) + math.sin(delta_lon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Radius of the Earth in kilometers
        radius_of_earth_km = 6371.0

        distance = radius_of_earth_km * c
        return distance

