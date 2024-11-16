import numpy as np
from copy import deepcopy

class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.visited = set()

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
        state_array = np.array(state)
        x, y = np.where(state_array == 0)
        x, y = x.item(), y.item()  # Blank tile's position as scalars
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Swap blank tile with the adjacent tile
                new_state = deepcopy(state)
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                neighbors.append(new_state)
        
        return neighbors

    def dfs(self, state, depth=0, max_depth=50):
        """Perform DFS to find the solution."""
        if depth > max_depth:  # Depth limit to avoid infinite loops
            return None

        if self.is_goal_state(state):
            return [state]

        # Convert state to a tuple to hash it
        self.visited.add(tuple(map(tuple, state)))

        neighbors = self.get_neighbors(state)
        # Sort neighbors by Manhattan distance to prioritize promising states
        neighbors.sort(key=lambda n: self.manhattan_distance(n))

        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in self.visited:
                path = self.dfs(neighbor, depth + 1, max_depth)
                if path:
                    return [state] + path

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
    solution = solver.dfs(initial_state)

    if solution:
        print("Solution found:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found within the depth limit.")


if __name__ == "__main__":
    main()
