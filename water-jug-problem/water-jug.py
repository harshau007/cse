from collections import deque

# Helper function to check if a state has been visited
def is_visited(visited_states, state):
    return state in visited_states

# Helper function to display the steps taken to reach the solution
def display_steps(steps):
    for i, step in enumerate(steps):
        print(f"Step {i + 1}: Jug 1 = {step[0]}L, Jug 2 = {step[1]}L")

# BFS implementation for Water Jug Problem
def bfs_water_jug(jug1_capacity, jug2_capacity, target_amount):
    queue = deque([(0, 0, [])])  # Initial state: both jugs empty and an empty list for steps
    visited_states = set()       # Set to track visited states

    while queue:
        jug1, jug2, steps = queue.popleft()

        if jug1 == target_amount or jug2 == target_amount:
            steps.append((jug1, jug2))
            return steps

        if is_visited(visited_states, (jug1, jug2)):
            continue

        visited_states.add((jug1, jug2))

        # Generate all possible next states and add them to the queue
        queue.append((jug1_capacity, jug2, steps + [(jug1, jug2)]))  # Fill jug 1
        queue.append((jug1, jug2_capacity, steps + [(jug1, jug2)]))  # Fill jug 2
        queue.append((0, jug2, steps + [(jug1, jug2)]))              # Empty jug 1
        queue.append((jug1, 0, steps + [(jug1, jug2)]))              # Empty jug 2

        # Pour from jug 1 to jug 2
        transfer = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - transfer, jug2 + transfer, steps + [(jug1, jug2)]))

        # Pour from jug 2 to jug 1
        transfer = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + transfer, jug2 - transfer, steps + [(jug1, jug2)]))

    return None  # If no solution is found

# DFS implementation for Water Jug Problem
def dfs_water_jug(jug1_capacity, jug2_capacity, target_amount):
    stack = [(0, 0, [])]  # Initial state: both jugs empty and an empty list for steps
    visited_states = set()  # Set to track visited states

    while stack:
        jug1, jug2, steps = stack.pop()

        if jug1 == target_amount or jug2 == target_amount:
            steps.append((jug1, jug2))
            return steps

        if is_visited(visited_states, (jug1, jug2)):
            continue

        visited_states.add((jug1, jug2))

        # Generate all possible next states and push them to the stack
        stack.append((jug1_capacity, jug2, steps + [(jug1, jug2)]))  # Fill jug 1
        stack.append((jug1, jug2_capacity, steps + [(jug1, jug2)]))  # Fill jug 2
        stack.append((0, jug2, steps + [(jug1, jug2)]))              # Empty jug 1
        stack.append((jug1, 0, steps + [(jug1, jug2)]))              # Empty jug 2

        # Pour from jug 1 to jug 2
        transfer = min(jug1, jug2_capacity - jug2)
        stack.append((jug1 - transfer, jug2 + transfer, steps + [(jug1, jug2)]))

        # Pour from jug 2 to jug 1
        transfer = min(jug2, jug1_capacity - jug1)
        stack.append((jug1 + transfer, jug2 - transfer, steps + [(jug1, jug2)]))

    return None  # If no solution is found

# Main function to test both BFS and DFS approaches
def main():
    jug1_capacity = 4  # Capacity of the first jug (in liters)
    jug2_capacity = 3  # Capacity of the second jug (in liters)
    target_amount = 2  # The target amount we want to measure (in liters)

    # Solve using BFS
    print("Solving using BFS:")
    bfs_solution = bfs_water_jug(jug1_capacity, jug2_capacity, target_amount)
    if bfs_solution:
        display_steps(bfs_solution)
    else:
        print("No solution found using BFS.")

    print("\nSolving using DFS:")
    # Solve using DFS
    dfs_solution = dfs_water_jug(jug1_capacity, jug2_capacity, target_amount)
    if dfs_solution:
        display_steps(dfs_solution)
    else:
        print("No solution found using DFS.")

# Run the main function
if __name__ == "__main__":
    main()
