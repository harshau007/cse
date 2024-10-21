class EightPuzzleHillClimbing:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def display_state(self, state):
        """Displays the current puzzle state in a 3x3 grid format."""
        for row in state:
            print(row)
        print()

    def get_possible_moves(self, state):
        """Returns the possible states after moving the blank tile (0) up, down, left, or right."""
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
        """Calculates the number of misplaced tiles (excluding the blank tile)."""
        misplaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j] and state[i][j] != 0:
                    misplaced_tiles += 1
        return misplaced_tiles

    def hill_climbing(self):
        """Solves the 8-puzzle problem using Hill Climbing."""
        current_state = self.initial_state
        self.display_state(current_state)

        while True:
            possible_moves = self.get_possible_moves(current_state)
            next_state = min(possible_moves, key=self.heuristic)

            if self.heuristic(next_state) >= self.heuristic(current_state):
                print("Reached a local optimum!")
                break

            current_state = next_state
            self.display_state(current_state)

        if current_state == self.goal_state:
            print("Reached the goal state!")
        else:
            print("Couldn't solve the puzzle with Hill Climbing.")


if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    puzzle = EightPuzzleHillClimbing(initial_state, goal_state)
    puzzle.hill_climbing()
