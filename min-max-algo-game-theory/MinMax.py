"""
    Minmax Algo:
        The Minimax algorithm is a decision-making algorithm used in two-player, zero-sum games (games where one player's gain is equivalent to the other's loss). It explores all possible moves and outcomes to determine the optimal move for both players. The players are:
            * Maximizer: A player trying to maximize the score (usually the main player).
            * Minimizer: A player trying to minimize the score (usually the opponent).
        The minimax algorithm assumes that both players play optimally and selects moves based on the idea that the maximizer tries to maximize the score and the minimizer tries to minimize it.
"""
class MinMax:
    def minimax(self, board, depth, is_maximizing):
        """
        Min-Max algorithm to determine the optimal move for the maximizing player.

        :param board: The current state of the Tic-Tac-Toe board.
        :param depth: The current depth in the game tree (how many moves ahead to consider).
        :param is_maximizing: Boolean indicating if it's the maximizing player's turn (True for 'X', False for 'O').
        :return: Optimal value for the maximizing player based on the board's evaluation.
        """

        # Check if the game has ended (win/loss/draw) and return score.
        if self.check_winner(board, 'X'):
            return 10 - depth  # 'X' is maximizing player (returns higher score for 'X' wins)
        elif self.check_winner(board, 'O'):
            return depth - 10  # 'O' is minimizing player (returns lower score for 'O' wins)
        elif self.is_full(board):
            return 0  # Draw

        if is_maximizing:
            best_value = float('-inf')  # Start with the lowest possible value
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'  # Simulate 'X' move
                        value = self.minimax(board, depth + 1, False)  # Minimize for 'O'
                        board[i][j] = ' '  # Undo move
                        best_value = max(best_value, value)  # Get the maximum score
            return best_value
        else:
            best_value = float('inf')  # Start with the highest possible value
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'  # Simulate 'O' move
                        value = self.minimax(board, depth + 1, True)  # Maximize for 'X'
                        board[i][j] = ' '  # Undo move
                        best_value = min(best_value, value)  # Get the minimum score
            return best_value

    def check_winner(self, board, player):
        """
        Checks if the specified player has won.

        :param board: The current state of the Tic-Tac-Toe board.
        :param player: The player to check for ('X' or 'O').
        :return: True if the player has won, False otherwise.
        """
        # Check rows, columns, and diagonals for a winning combination
        for i in range(3):
            if all([cell == player for cell in board[i]]):  # Check rows
                return True
            if all([board[j][i] == player for j in range(3)]):  # Check columns
                return True
        if all([board[i][i] == player for i in range(3)]):  # Check diagonal
            return True
        if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
            return True
        return False

    def is_full(self, board):
        """
        Checks if the board is full (no empty spaces left).

        :param board: The current state of the Tic-Tac-Toe board.
        :return: True if the board is full, False otherwise.
        """
        return all(cell != ' ' for row in board for cell in row)
