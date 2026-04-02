import math
import random

from routes.route_graph import RouteGraph
from risk.risk_engine import RiskEngine


class RouteOptimizer:
    """
    Finds safer routes between origin and destination
    based on risk evaluation
    """

    def __init__(self):
        self.graph = RouteGraph(step_degrees=1)
        self.graph.generate_nodes()

        self.risk_engine = RiskEngine()

    def distance(self, a, b):
        """
        Simple geographic distance
        """
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def generate_candidate_routes(self, origin, destination, n=10):
        """
        Generate random candidate routes between origin and destination
        """
        routes = []

        for _ in range(n):

            route = [origin]

            # intermediate waypoints
            for _ in range(5):
                node = random.choice(self.graph.nodes)
                route.append(node)

            route.append(destination)

            routes.append(route)

        return routes

    def simulate_weather(self):
        """
        Placeholder weather simulation
        (later replaced with real NOAA data)
        """
        return {
            "wind_speed": random.uniform(0, 40),
            "precipitation": random.uniform(0, 50),
            "visibility": random.uniform(1000, 10000),
            "temperature": random.uniform(-30, 45)
        }

    def route_risk(self, route):
        """
        Compute average risk of a route
        """
        risks = []

        for _ in route:
            weather = self.simulate_weather()
            risk = self.risk_engine.compute_risk(weather)
            risks.append(risk)

        return sum(risks) / len(risks)

    def find_best_route(self, origin, destination):

        candidates = self.generate_candidate_routes(origin, destination)

        best_route = None
        best_score = float("inf")

        for route in candidates:

            score = self.route_risk(route)

            if score < best_score:
                best_score = score
                best_route = route

        return best_route, best_score


if __name__ == "__main__":

    optimizer = RouteOptimizer()

    # Example coordinates
    origin = (40.6413, -73.7781)  # New York
    destination = (51.4700, -0.4543)  # London

    route, score = optimizer.find_best_route(origin, destination)

    print("Best route risk score:", score)
    print("Route waypoints:", route)