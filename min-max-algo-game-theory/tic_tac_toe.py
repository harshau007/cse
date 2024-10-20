from MinMaxTicTacToe import MinMax

class TicTacToe:
    def __init__(self):
        # Initialize an empty board with spaces
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.minmax = MinMax()  # Create an instance of MinMax class

    def print_board(self):
        """Prints the current state of the Tic-Tac-Toe board."""
        # for row in self.board:
        #     print(' | '.join(row))
        #     print('-' * 9)
        for i in range(3):
            print(' | '.join(self.board[i]))  # Print each row
            if i < 2:  # Print the dashes only between rows
                print('-' * 9)

    def play_game(self):
        """Controls the flow of the Tic-Tac-Toe game."""
        while True:
            self.print_board()
            # Player 'X' turn
            self.player_move('X')
            if self.check_game_over('X'):
                break  # End game if player 'X' wins or if it's a draw

            # Player 'O' turn (AI)
            print("AI is making its move...")
            self.ai_move()
            if self.check_game_over('O'):
                break  # End game if player 'O' wins or if it's a draw

    def player_move(self, player):
        """Handles player move input."""
        while True:
            move = input(f"Player {player}, enter your move (row and column, e.g., '1 1'): ")
            try:
                row, col = map(int, move.split())
                if self.board[row][col] == ' ':
                    self.board[row][col] = player  # Update board with player's move
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid move. Please enter row and column as two numbers from 0 to 2.")

    def ai_move(self):
        """Determines the best move for AI using Min-Max algorithm."""
        best_value = float('-inf')
        best_move = None

        # Iterate through the board to find the best move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'  # Simulate AI move
                    move_value = self.minmax.minimax(self.board, 0, False)  # Evaluate move
                    self.board[i][j] = ' '  # Undo move
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)  # Update best move

        if best_move:
            self.board[best_move[0]][best_move[1]] = 'O'  # Make the best move

    def check_game_over(self, player):
        """Checks if the game has ended (win/draw)."""
        if self.minmax.check_winner(self.board, player):
            self.print_board()
            print(f"Player {player} wins!")
            return True
        elif self.minmax.is_full(self.board):
            self.print_board()
            print("It's a draw!")
            return True
        return False

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
