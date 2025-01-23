
    
import random
def hill_climbing(function, start_x, step_size=0.1, max_iterations=1000):
 current_x = start_x
 current_value = function(current_x)
 for i in range(max_iterations):
    next_x = current_x + step_size * random.choice([-1, 1])
    next_value = function(next_x)
 if next_value > current_value:
    current_x = next_x
    current_value = next_value
    return current_x, current_value

def objective_function(x):
 return -(x - 3)**2 + 10

start_x = random.uniform(-10, 10)

optimal_x, optimal_value = hill_climbing(objective_function, start_x)
print(f"Optimal x: {optimal_x}, Optimal value: {optimal_value}")