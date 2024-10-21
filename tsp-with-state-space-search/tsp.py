import itertools
import sys
import random
from queue import Queue, LifoQueue, PriorityQueue


class TSPSolver:
    def __init__(self, distance_matrix):
        """
        Initialize the TSP Solver with a distance matrix.
        :param distance_matrix: 2D list representing distances between cities
        """
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
    
    def brute_force(self):
        """
        Solves the TSP using brute-force approach (checking all permutations).
        :return: The minimum distance and the best route.
        """
        cities = list(range(self.num_cities))
        min_distance = sys.maxsize
        best_route = None

        # Check all possible permutations of city routes
        for route in itertools.permutations(cities):
            total_distance = self.calculate_total_distance(route, self.distance_matrix)
            if total_distance < min_distance:
                min_distance = total_distance
                best_route = route

        return best_route, min_distance

    def bfs(self):
        """
        Solves the TSP using Breadth-First Search.
        :return: The minimum distance and the best route.
        """
        cities = list(range(self.num_cities))
        q = Queue()
        q.put((0, [0], 0))  # (current city, path, current distance)
        min_distance = sys.maxsize
        best_route = None

        while not q.empty():
            current_city, path, current_distance = q.get()

            # If all cities are visited, check the return to the starting city
            if len(path) == self.num_cities:
                total_distance = current_distance + self.distance_matrix[current_city][0]
                if total_distance < min_distance:
                    min_distance = total_distance
                    best_route = path + [0]
                continue

            # Explore next cities
            for next_city in cities:
                if next_city not in path:
                    new_distance = current_distance + self.distance_matrix[current_city][next_city]
                    q.put((next_city, path + [next_city], new_distance))

        return best_route, min_distance

    def dfs(self):
        """
        Solves the TSP using Depth-First Search.
        :return: The minimum distance and the best route.
        """
        cities = list(range(self.num_cities))
        stack = LifoQueue()
        stack.put((0, [0], 0))  # (current city, path, current distance)
        min_distance = sys.maxsize
        best_route = None

        while not stack.empty():
            current_city, path, current_distance = stack.get()

            # If all cities are visited, check the return to the starting city
            if len(path) == self.num_cities:
                total_distance = current_distance + self.distance_matrix[current_city][0]
                if total_distance < min_distance:
                    min_distance = total_distance
                    best_route = path + [0]
                continue

            # Explore next cities
            for next_city in cities:
                if next_city not in path:
                    new_distance = current_distance + self.distance_matrix[current_city][next_city]
                    stack.put((next_city, path + [next_city], new_distance))

        return best_route, min_distance

    def a_star(self):
        """
        Solves the TSP using the A* search algorithm.
        :return: The minimum distance and the best route.
        """
        cities = list(range(self.num_cities))
        pq = PriorityQueue()
        pq.put((0, 0, [0]))  # (f-cost (priority), current distance, path)
        min_distance = sys.maxsize
        best_route = None

        while not pq.empty():
            _, current_distance, path = pq.get()

            current_city = path[-1]

            # If all cities are visited, check the return to the starting city
            if len(path) == self.num_cities:
                total_distance = current_distance + self.distance_matrix[current_city][0]
                if total_distance < min_distance:
                    min_distance = total_distance
                    best_route = path + [0]
                continue

            # Explore next cities
            for next_city in cities:
                if next_city not in path:
                    new_distance = current_distance + self.distance_matrix[current_city][next_city]
                    heuristic = self.estimate_heuristic(next_city, path)
                    pq.put((new_distance + heuristic, new_distance, path + [next_city]))

        return best_route, min_distance

    def greedy_search(self, start=0):
        """
        Performs Greedy search to solve TSP starting from a specified city.
        :return: The best route and minimum distance.
        """
        visited = [False] * self.num_cities
        route = [start]
        visited[start] = True
        total_distance = 0

        current_city = start
        for _ in range(self.num_cities - 1):
            nearest_city = None
            nearest_distance = float('inf')
            
            # Find nearest unvisited city
            for next_city in range(self.num_cities):
                if not visited[next_city] and self.distance_matrix[current_city][next_city] < nearest_distance:
                    nearest_city = next_city
                    nearest_distance = self.distance_matrix[current_city][next_city]
            
            route.append(nearest_city)
            visited[nearest_city] = True
            total_distance += nearest_distance
            current_city = nearest_city

        # Return to the starting city
        total_distance += self.distance_matrix[current_city][start]
        route.append(start)

        return route, total_distance

    def hill_climbing(self):
        """
        Solves the TSP using Hill Climbing algorithm.
        :return: The best route and minimum distance.
        """
        # Start with a random route
        current_route = list(range(self.num_cities))
        random.shuffle(current_route)
        current_distance = self.calculate_total_distance(current_route, self.distance_matrix)
        
        while True:
            neighbors = self.get_neighbors(current_route)
            next_route = None
            next_distance = current_distance
            
            # Find the best neighbor
            for neighbor in neighbors:
                neighbor_distance = self.calculate_total_distance(neighbor, self.distance_matrix)
                if neighbor_distance < next_distance:
                    next_route = neighbor
                    next_distance = neighbor_distance
            
            # If no better neighbor is found, stop
            if next_route is None:
                break
            
            # Move to the better neighbor
            current_route = next_route
            current_distance = next_distance

        return current_route, current_distance

    def get_neighbors(self, route):
        """
        Generate neighboring routes by swapping two cities.
        :param route: Current route.
        :return: A list of neighboring routes.
        """
        neighbors = []
        for i in range(len(route)):
            for j in range(i + 1, len(route)):
                neighbor = route[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def estimate_heuristic(self, current_city, path):
        """
        A heuristic function for A* algorithm.
        :param current_city: Current city in the path
        :param path: The current path
        :return: Heuristic value (minimum cost estimate to complete the tour)
        """
        remaining_cities = set(range(self.num_cities)) - set(path)
        if not remaining_cities:
            return 0

        # Find minimum distance to any remaining city
        min_heuristic = min(self.distance_matrix[current_city][city] for city in remaining_cities)
        return min_heuristic

    def calculate_total_distance(self, route, distance_matrix):
        """
        Calculate the total distance of the given route.
        :param route: Tuple or list representing the order of cities.
        :param distance_matrix: 2D list with distances between cities.
        :return: Total distance of the route.
        """
        total_distance = 0
        for i in range(len(route)):
            from_city = route[i]
            to_city = route[(i + 1) % len(route)]  # Loop back to the start city
            total_distance += distance_matrix[from_city][to_city]
        return total_distance

    def print_route(self, route):
        """
        Prints the route in a readable format.
        :param route: List or tuple of city indices.
        """
        print(" -> ".join(map(str, route)))
