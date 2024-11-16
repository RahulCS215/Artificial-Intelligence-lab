import heapq
from copy import deepcopy

class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def manhattan_distance(self, state):
        """Calculate the Manhattan distance of a state."""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:  # Skip the blank tile
                    goal_x, goal_y = [(x, y) for x in range(3) for y in range(3) if self.goal_state[x][y] == value][0]
                    distance += abs(goal_x - i) + abs(goal_y - j)
        return distance

    def is_goal_state(self, state):
        """Check if a state matches the goal state."""
        return state == self.goal_state

    def get_neighbors(self, state):
        """Generate all valid neighbor states from the current state."""
        neighbors = []
        x, y = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]  # Locate blank tile
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Swap blank tile with the adjacent tile
                new_state = deepcopy(state)
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                neighbors.append(new_state)
        
        return neighbors

    def iddfs(self, state, max_depth=50):
        """Perform Iterative Deepening Depth First Search (IDDFS)."""
        def dls(current_state, depth):
            if depth == 0:
                return None
            if self.is_goal_state(current_state):
                return [current_state]

            for neighbor in self.get_neighbors(current_state):
                result = dls(neighbor, depth - 1)
                if result:
                    return [current_state] + result
            return None

        for depth in range(1, max_depth + 1):
            result = dls(state, depth)
            if result:
                return result
        return None

    def a_star(self):
        """Perform A* search to solve the puzzle."""
        open_set = []
        heapq.heappush(open_set, (0, self.initial_state, []))  # (f, state, path)

        closed_set = set()

        while open_set:
            f, current_state, path = heapq.heappop(open_set)

            if self.is_goal_state(current_state):
                return path + [current_state]

            closed_set.add(tuple(map(tuple, current_state)))

            for neighbor in self.get_neighbors(current_state):
                if tuple(map(tuple, neighbor)) not in closed_set:
                    g = len(path) + 1  # Cost to reach this neighbor
                    h = self.manhattan_distance(neighbor)  # Heuristic cost
                    heapq.heappush(open_set, (g + h, neighbor, path + [current_state]))

        return None


# Main execution
def main():
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solver = PuzzleSolver(initial_state, goal_state)

    print("Using IDDFS:")
    iddfs_solution = solver.iddfs(initial_state)
    if iddfs_solution:
        for step, state in enumerate(iddfs_solution):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found with IDDFS.")

    print("Using A* Algorithm:")
    a_star_solution = solver.a_star()
    if a_star_solution:
        for step, state in enumerate(a_star_solution):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found with A* Algorithm.")


if __name__ == "__main__":
    main()
