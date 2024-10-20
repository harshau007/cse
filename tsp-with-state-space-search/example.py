from tsp import TSPSolver

# Define a distance matrix where each entry is the distance between two cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver(distance_matrix)

# Solve using BFS
best_route_bfs, min_distance_bfs = solver.bfs()
print("Best route (BFS):")
solver.print_route(best_route_bfs)
print(f"Minimum Distance (BFS): {min_distance_bfs}")

# Solve using DFS
best_route_dfs, min_distance_dfs = solver.dfs()
print("\nBest route (DFS):")
solver.print_route(best_route_dfs)
print(f"Minimum Distance (DFS): {min_distance_dfs}")

# Solve using A*
best_route_astar, min_distance_astar = solver.a_star()
print("\nBest route (A*):")
solver.print_route(best_route_astar)
print(f"Minimum Distance (A*): {min_distance_astar}")