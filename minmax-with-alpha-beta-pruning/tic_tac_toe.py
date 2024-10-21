import math

# Constants
PLAYER_X = 'X'  # AI Player
PLAYER_O = 'O'  # Human Player
EMPTY = '_'


class TicTacToe:
    def __init__(self):
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def print_board(self):
        """Print the Tic-Tac-Toe board."""
        for row in self.board:
            print(' '.join(row))
        print()

    def is_full(self):
        """Check if the board is full."""
        for row in self.board:
            if EMPTY in row:
                return False
        return True

    def check_winner(self):
        """Check if there is a winner."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != EMPTY:
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != EMPTY:
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return self.board[0][2]

        return None

    def is_terminal(self):
        """Check if the game has ended (either win or draw)."""
        return self.check_winner() is not None or self.is_full()

    def get_available_moves(self):
        """Get a list of available moves."""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    moves.append((i, j))
        return moves

    def make_move(self, row, col, player):
        """Make a move on the board."""
        self.board[row][col] = player

    def undo_move(self, row, col):
        """Undo a move on the board."""
        self.board[row][col] = EMPTY

    def minimax(self, depth, is_maximizing, alpha, beta):
        """Minimax algorithm with alpha-beta pruning."""
        winner = self.check_winner()
        if winner == PLAYER_X:
            return 10 - depth  # AI wins
        elif winner == PLAYER_O:
            return depth - 10  # Human wins
        elif self.is_full():
            return 0  # Draw

        if is_maximizing:
            max_eval = -math.inf
            for move in self.get_available_moves():
                self.make_move(move[0], move[1], PLAYER_X)
                eval = self.minimax(depth + 1, False, alpha, beta)
                self.undo_move(move[0], move[1])
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_available_moves():
                self.make_move(move[0], move[1], PLAYER_O)
                eval = self.minimax(depth + 1, True, alpha, beta)
                self.undo_move(move[0], move[1])
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self):
        """Find the best move for AI using Minimax with alpha-beta pruning."""
        best_val = -math.inf
        best_move = None

        for move in self.get_available_moves():
            self.make_move(move[0], move[1], PLAYER_X)
            move_val = self.minimax(0, False, -math.inf, math.inf)
            self.undo_move(move[0], move[1])

            if move_val > best_val:
                best_val = move_val
                best_move = move

        return best_move

    def play_game(self):
        """Main function to play the game."""
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while not self.is_terminal():
            # Human move
            row, col = map(int, input("Enter your move (row and column): ").split())
            if self.board[row][col] == EMPTY:
                self.make_move(row, col, PLAYER_O)
                self.print_board()

                if self.is_terminal():
                    break

                # AI move
                print("AI is making a move...")
                move = self.best_move()
                if move:
                    self.make_move(move[0], move[1], PLAYER_X)
                    self.print_board()
            else:
                print("Invalid move, try again.")

        winner = self.check_winner()
        if winner == PLAYER_X:
            print("AI wins!")
        elif winner == PLAYER_O:
            print("You win!")
        else:
            print("It's a draw!")


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
