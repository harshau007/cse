from AlphaBetaPruning import minimax_with_alpha_beta
import math

if __name__ == "__main__":
    # Define root node, depth of the tree, and initial alpha-beta values
    root_node = 'A'
    max_depth = 3
    initial_alpha = -math.inf
    initial_beta = math.inf

    # Call the minimax algorithm with alpha-beta pruning starting at the root node
    optimal_value = minimax_with_alpha_beta(root_node, max_depth, initial_alpha, initial_beta, False)

    # Display the result
    print(f"The optimal value for the root node is: {optimal_value}")
