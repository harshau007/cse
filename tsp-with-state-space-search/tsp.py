import itertools
import sys
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

    """
        1) We use a Queue to explore nodes level by level. In each level, all cities are explored one at a time.
        2) The current city, path, and distance are stored in the queue.
        3) Once all cities are visited, the cost to return to the starting city is calculated and compared to the minimum distance found so far.
        
        Time Complexity:
            O(b^d): BFS explores every possible path, meaning it expands all nodes at a given depth before moving to the next. For TSP, this can be very expensive since the branching factor grows with the number of cities.
        Space Complexity:
            O(b^d): BFS stores all nodes at the current level of the search tree, leading to exponential space consumption as the number of cities increases.
        Solution Optimality:
            BFS guarantees an optimal solution because it explores all possible routes level by level. However, it's impractical for larger instances due to high time and space complexity.
    """
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

    """
        1) We use a LifoQueue (stack) to explore as deep as possible along each path before backtracking.
        2) Like BFS, we store the current city, path, and distance on the stack.
        3) The difference is in the order of exploration, as DFS goes deeper into the solution tree first.
        
        Time Complexity:
            O(b^d): DFS may explore as many states as BFS, as it will visit all permutations in the worst case. However, DFS may stop early, making it faster in some cases, but it's not guaranteed.
        Space Complexity:
            O(d): DFS only needs to store the current path and the recursion stack, so its space complexity is linear in the depth (or the number of cities). It has a significant space advantage over BFS.
        Solution Optimality:
            DFS does not guarantee an optimal solution unless it explores every possible path, which would make it behave like BFS. Without optimization (like pruning), it might find suboptimal paths. Optimizations like branch-and-bound can improve it.
    """
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

    """
        1) A* uses a priority queue (PriorityQueue), where the queue is ordered by a cost function f(n) = g(n) + h(n) where:
                g(n) is the current distance.
                h(n) is the heuristic estimate of the remaining cost.
        2) The heuristic function here estimates the remaining cost by considering the minimum distance to unvisited cities.
        
        Time Complexity:
            O(b^d) (worst case): In the worst case, A* may have to explore all nodes, but it often performs much better than BFS or DFS because it uses a heuristic to prune large portions of the search tree. A good heuristic can reduce the time complexity significantly.
        Space Complexity:
            O(b^d): Like BFS, A* stores all nodes in memory since it expands nodes in order of the lowest cost. This can lead to high space usage, but it's generally more efficient than BFS for large problems because it explores fewer states.
        Solution Optimality:
            A* guarantees an optimal solution as long as the heuristic is admissible (i.e., it never overestimates the true cost to reach the goal). It is more efficient than BFS while still maintaining optimality.
    """
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

    def estimate_heuristic(self, current_city, path):
        """
        A heuristic function for A* algorithm. Here, we will use the minimum distance from the current city
        to any remaining city as the heuristic.
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
