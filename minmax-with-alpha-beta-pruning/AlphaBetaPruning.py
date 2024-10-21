"""
Definations:
    Minmax Algo:
        The Minimax algorithm is a decision-making algorithm used in two-player, zero-sum games (games where one player's gain is equivalent to the other's loss). It explores all possible moves and outcomes to determine the optimal move for both players. The players are:
            * Maximizer: A player trying to maximize the score (usually the main player).
            * Minimizer: A player trying to minimize the score (usually the opponent).
        The minimax algorithm assumes that both players play optimally and selects moves based on the idea that the maximizer tries to maximize the score and the minimizer tries to minimize it.
        
    Alpha-Beta Pruning

        Alpha-Beta Pruning is an optimization technique for the minimax algorithm that reduces the number of nodes evaluated in the game tree. The idea is to prune (cut off) branches of the tree that are not necessary to evaluate, making the algorithm more efficient without affecting the result.

        Alpha: The best value that the maximizer can guarantee.
        Beta: The best value that the minimizer can guarantee.
        The pruning works by:
            * Updating the alpha value when the maximizer finds a better move.
            * Updating the beta value when the minimizer finds a worse move.
            * Pruning branches when a move is found that makes further exploration unnecessary (i.e., when alpha >= beta).
"""

# Simulated game tree with node values (example game states)
# The structure maps each node to its child nodes or final evaluation if terminal
# """
#         A
#        / \
#       B   C
#      / \ / \
#    D  E F  G
#   -1  3 5  0

#     A is the root node.
#     B and C are child nodes of A.
#     D, E, F, and G are terminal nodes with corresponding evaluation values (-1, 3, 5, 0).
# """
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': -1,  # Terminal node
    'E': 3,   # Terminal node
    'F': 5,   # Terminal node
    'G': 0    # Terminal node
}

# Function to get children of a node (non-terminal nodes have children, terminal nodes don't)
"""
    Returns the child nodes of the current node. If the node has no children (terminal node), it returns an empty list.
"""
def get_children(node):
    return game_tree.get(node, [])

# Function to determine if a node is terminal (i.e., no children)
"""
    Checks if a node is terminal (has no children) by confirming if its value is an integer rather than a list of child nodes.
"""
def is_terminal_node(node):
    return not isinstance(game_tree[node], list)

# Function to evaluate a terminal node by returning its heuristic value
def evaluate(node):
    return game_tree[node]  # Terminal nodes are mapped to their evaluation scores

# Minimax algorithm with Alpha-Beta Pruning
"""
    Implements the Minimax algorithm with Alpha-Beta Pruning. The algorithm searches the game tree, alternating between maximizing and minimizing player decisions, and prunes subtrees where further exploration is unnecessary.
"""
def minimax_with_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    """
    Implements the Minimax algorithm with Alpha-Beta Pruning.

    Parameters:
    node (str): The current node in the game tree.
    depth (int): The depth of the game tree to explore.
    alpha (float): The best value that the maximizer can guarantee so far.
    beta (float): The best value that the minimizer can guarantee so far.
    maximizingPlayer (bool): True if the current player is the maximizer, False if the minimizer.

    Returns:
    int: The optimal value for the current node.
    """
    # Base case: return the evaluation of terminal node or reach the depth limit
    if depth == 0 or is_terminal_node(node):
        return evaluate(node)  # Returns the heuristic value of the node

    if maximizingPlayer:
        max_eval = float('-inf')  # Initialize the worst case for maximizer
        for child in get_children(node):  # Explore each child of the current node
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)  # Maximizer chooses the maximum value
            alpha = max(alpha, eval)  # Update alpha (best guarantee for maximizer)
            if beta <= alpha:
                print(f"Pruning at node {node} with alpha={alpha}, beta={beta}")
                break  # Beta cutoff (prune the branch)
        return max_eval
    else:
        min_eval = float('inf')  # Initialize the worst case for minimizer
        for child in get_children(node):  # Explore each child of the current node
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)  # Minimizer chooses the minimum value
            beta = min(beta, eval)  # Update beta (best guarantee for minimizer)
            if beta <= alpha:
                print(f"Pruning at node {node} with alpha={alpha}, beta={beta}")
                break  # Alpha cutoff (prune the branch)
        return min_eval
