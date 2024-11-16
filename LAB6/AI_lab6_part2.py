import heapq

class EightQueensSolverAStar:
    def __init__(self, size=8):
        self.size = size

    def calculate_conflicts(self, board):
        """Calculate the number of conflicts for a given board."""
        conflicts = 0
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                # Check for conflicts in rows or diagonals
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbors(self, board):
        """Generate all possible neighbors of the current board."""
        neighbors = []
        for col in range(len(board)):
            for row in range(self.size):
                if board[col] != row:
                    new_board = board[:]
                    new_board[col] = row
                    neighbors.append(new_board)
        return neighbors

    def a_star(self):
        """Solve the 8-Queens problem using the A* algorithm."""
        # Priority queue for A* search
        open_set = []
        initial_board = [0] * self.size  # Start with all queens in the first row
        heapq.heappush(open_set, (0, 0, initial_board))  # (f, g, state)

        while open_set:
            f, g, current_board = heapq.heappop(open_set)

            # Calculate conflicts in the current state
            current_conflicts = self.calculate_conflicts(current_board)
            if current_conflicts == 0:
                return current_board  # Solution found

            # Generate neighbors and add them to the priority queue
            for neighbor in self.get_neighbors(current_board):
                h = self.calculate_conflicts(neighbor)  # Heuristic cost
                heapq.heappush(open_set, (g + 1 + h, g + 1, neighbor))  # f = g + h

        return None  # No solution found

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
    solver = EightQueensSolverAStar(size=8)
    solution = solver.a_star()

    if solution:
        print("Solution found:")
        solver.print_board(solution)
    else:
        print("No solution found.")
