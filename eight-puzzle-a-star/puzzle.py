import heapq

class EightPuzzleAStar:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state  # Goal state

    def display_state(self, state):
        """Displays the puzzle state."""
        for row in state:
            print(row)
        print()

    def get_possible_moves(self, state):
        """Returns the possible states after moving the blank tile."""
        possible_moves = []
        blank_position = [(r, c) for r, row in enumerate(state) for c, val in enumerate(row) if val == 0][0]

        r, c = blank_position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [list(row) for row in state]  # Copy the current state
                new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]  # Swap blank with target tile
                possible_moves.append(new_state)

        return possible_moves

    def heuristic(self, state):
        """Calculates the Manhattan distance."""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    target_x = (value - 1) // 3
                    target_y = (value - 1) % 3
                    distance += abs(i - target_x) + abs(j - target_y)
        return distance

    def a_star(self):
        """A* search algorithm for solving the 8-puzzle problem."""
        heap = []
        heapq.heappush(heap, (0, self.initial_state))
        visited = set()

        while heap:
            _, current_state = heapq.heappop(heap)

            if current_state == self.goal_state:
                self.display_state(current_state)
                print("Reached the goal!")
                return

            visited.add(tuple(map(tuple, current_state)))  # Convert list to tuple for hashing
            self.display_state(current_state)

            for next_state in self.get_possible_moves(current_state):
                if tuple(map(tuple, next_state)) not in visited:
                    cost = self.heuristic(next_state)
                    heapq.heappush(heap, (cost, next_state))

        print("No solution found.")


if __name__ == "__main__":
    initial_state = [
        [1, 0, 3],
        [4, 2, 6],
        [7, 5, 8]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    puzzle = EightPuzzleAStar(initial_state, goal_state)
    puzzle.a_star()
