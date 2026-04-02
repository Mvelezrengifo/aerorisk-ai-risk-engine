import math


class RouteGraph:
    """
    Global spherical route graph
    """

    def __init__(self, step_degrees=1.0):
        self.step = step_degrees
        self.nodes = []

    def generate_nodes(self):
        """
        Generate nodes across the globe
        """
        lat = -90

        while lat <= 90:
            lon = -180
            while lon <= 180:
                self.nodes.append((lat, lon))
                lon += self.step
            lat += self.step

        return self.nodes

    def node_count(self):
        return len(self.nodes)


if __name__ == "__main__":

    graph = RouteGraph(step_degrees=1)

    graph.generate_nodes()

    print("Total nodes in global graph:", graph.node_count())