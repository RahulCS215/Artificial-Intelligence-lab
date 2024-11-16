import math
import random

def objective_function(x):
    """Calculate the value of the objective function: f(x) = x^2 + 5*sin(x)."""
    return x**2 + 5 * math.sin(x)

def simulated_annealing(objective, x_start, temperature, cooling_rate, max_iterations):
    """
    Solve the objective function using the Simulated Annealing algorithm.
    
    Parameters:
    - objective: The objective function to minimize.
    - x_start: Initial guess.
    - temperature: Initial temperature.
    - cooling_rate: Rate at which the temperature decreases.
    - max_iterations: Maximum number of iterations.
    
    Returns:
    - Best solution found and its objective value.
    """
    current_x = x_start
    current_value = objective(current_x)
    best_x = current_x
    best_value = current_value

    for i in range(max_iterations):
        # Generate a new candidate solution in the neighborhood
        new_x = current_x + random.uniform(-1, 1)
        new_value = objective(new_x)

        # Calculate the change in the objective function
        delta = new_value - current_value

        # Accept the new solution with probability based on temperature
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature):
            current_x = new_x
            current_value = new_value

            # Update the best solution found
            if current_value < best_value:
                best_x = current_x
                best_value = current_value

        # Decrease the temperature
        temperature *= cooling_rate

        # Log the process
        print(f"Iteration {i + 1}: Current x = {current_x:.5f}, Current value = {current_value:.5f}, Temperature = {temperature:.5f}")

        # Stop if temperature is very low
        if temperature < 1e-8:
            break

    return best_x, best_value


# Main execution
if __name__ == "__main__":
    # Problem settings
    initial_guess = random.uniform(-10, 10)  # Random initial guess in the range [-10, 10]
    initial_temperature = 1000
    cooling_rate = 0.99
    max_iterations = 1000

    # Solve using Simulated Annealing
    best_solution, best_value = simulated_annealing(
        objective_function,
        initial_guess,
        initial_temperature,
        cooling_rate,
        max_iterations
    )

    print("\nBest solution found:")
    print(f"x = {best_solution:.5f}")
    print(f"f(x) = {best_value:.5f}")
