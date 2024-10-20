# Importing copy for deepcopy function
import copy

# This variable can be changed to change
# the program from 8 puzzle(n=3) to 15
# puzzle(n=4) to 24 puzzle(n=5)...
n = 3

# Bottom, left, top, right movements
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

class Node:
    """Node class to represent each state of the puzzle."""
    
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent  # Parent node
        self.mat = mat  # Current state of the puzzle
        self.empty_tile_pos = empty_tile_pos  # Position of the empty tile
        self.cost = cost  # Number of misplaced tiles
        self.level = level  # Number of moves so far

    def __lt__(self, other):
        """Define less than for priority queue behavior."""
        return self.cost < other.cost

def calculateCost(mat, final) -> int:
    """Calculate the number of misplaced tiles."""
    count = 0
    for i in range(n):
        for j in range(n):
            if (mat[i][j] != final[i][j]) and (mat[i][j] != 0):
                count += 1
    return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> Node:
    """Create a new node for a given state of the puzzle."""
    new_mat = copy.deepcopy(mat)  # Deep copy of the current matrix

    # Swap the empty tile with the adjacent tile
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    # Calculate the number of misplaced tiles for the new state
    cost = calculateCost(new_mat, final)
    return Node(parent, new_mat, new_empty_tile_pos, cost, level)

def isSafe(x, y):
    """Check if the new position is within bounds."""
    return 0 <= x < n and 0 <= y < n

def printMatrix(mat):
    """Print the matrix representation of the puzzle."""
    for row in mat:
        print(" ".join(str(x) for x in row))
    print()

def printPath(root):
    """Print the path from the root node to the solution."""
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mat)

def hill_climbing(initial, final, empty_tile_pos):
    """Implement the Hill Climbing algorithm to solve the puzzle."""
    current_node = Node(None, initial, empty_tile_pos, calculateCost(initial, final), 0)

    while True:
        # Generate all possible moves
        neighbors = []
        for i in range(4):
            new_tile_pos = (current_node.empty_tile_pos[0] + row[i], current_node.empty_tile_pos[1] + col[i])
            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                neighbor = newNode(current_node.mat, current_node.empty_tile_pos, new_tile_pos, current_node.level + 1, current_node, final)
                neighbors.append(neighbor)

        # Find the neighbor with the least cost
        next_node = min(neighbors, key=lambda neighbor: neighbor.cost, default=None)

        # If the next node is not better than the current node, we've reached a local optimum
        if next_node is None or next_node.cost >= current_node.cost:
            break

        current_node = next_node  # Move to the best neighbor

    # If the solution is found
    if current_node.cost == 0:
        print("Solution found!")
        printPath(current_node)
    else:
        print("No solution found!")

# Driver Code

# Initial configuration of the puzzle
initial = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Goal configuration of the puzzle
final = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Blank tile coordinates in initial configuration
empty_tile_pos = (1, 1)

# Function call to solve the puzzle using Hill Climbing
hill_climbing(initial, final, empty_tile_pos)