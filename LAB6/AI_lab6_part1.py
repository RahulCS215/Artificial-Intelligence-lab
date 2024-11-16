import random

class EightQueensSolver:
    def __init__(self, size=8):
        self.size = size
        self.board = self.initialize_board()

    def initialize_board(self):
        """Initialize the board with one queen in each column at a random row."""
        return [random.randint(0, self.size - 1) for _ in range(self.size)]

    def calculate_conflicts(self, board):
        """Calculate the number of conflicts for a given board."""
        conflicts = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                # Check if queens are in the same row or diagonal
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbors(self, board):
        """Generate all possible neighbors of the current board."""
        neighbors = []
        for col in range(self.size):
            for row in range(self.size):
                if row != board[col]:
                    new_board = board[:]
                    new_board[col] = row
                    neighbors.append(new_board)
        return neighbors

    def hill_climbing(self):
        """Solve the 8-Queens problem using the Hill Climbing algorithm."""
        current_board = self.board
        current_conflicts = self.calculate_conflicts(current_board)

        while True:
            neighbors = self.get_neighbors(current_board)
            # Evaluate neighbors and find the best one
            neighbor_conflicts = [(self.calculate_conflicts(neighbor), neighbor) for neighbor in neighbors]
            best_neighbor_conflicts, best_neighbor = min(neighbor_conflicts, key=lambda x: x[0])

            # If no better neighbor is found, return the current board
            if best_neighbor_conflicts >= current_conflicts:
                return current_board, current_conflicts

            # Move to the better neighbor
            current_board = best_neighbor
            current_conflicts = best_neighbor_conflicts

    def print_board(self, board):
        """Print the chessboard."""
        for row in range(self.size):
            line = ""
            for col in range(self.size):
                if board[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


# Main execution
if __name__ == "__main__":
    solver = EightQueensSolver()
    solution, conflicts = solver.hill_climbing()

    print("Solution found:")
    solver.print_board(solution)
    print(f"Number of conflicts: {conflicts}")
