import math
import random
def simulated_annealing(function, start_x, initial_temp, cooling_rate, min_temp, max_iterations):
 current_x = start_x
 current_value = function(current_x)
 temp = initial_temp
 for i in range(max_iterations):
  if temp <= min_temp:
     break
 next_x = current_x + random.uniform(-1, 1) # A random step left or right
 next_value = function(next_x)
 delta_e = next_value - current_value
 if delta_e > 0:
    current_x = next_x
    current_value = next_value
 else:
    if random.uniform(0, 1) < math.exp(delta_e / temp):
     current_x = next_x
     current_value = next_value

 temp *= cooling_rate

 return current_x, current_value
def objective_function(x):
 return -(x - 3)**2 + 10
# Parameters for simulated annealing
start_x = random.uniform(-10, 10) # Random initial solution
initial_temp = 1000 # Starting temperature
cooling_rate = 0.95 # Cooling rate (temperature decreases by 5% every iteration)
min_temp = 0.01 # Minimum temperature before stopping
max_iterations = 1000 # Number of iterations to run
# Run the simulated annealing algorithm
optimal_x, optimal_value = simulated_annealing(objective_function, start_x, initial_temp, cooling_rate, min_temp,
max_iterations)
print(f"Optimal x: {optimal_x}, Optimal value: {optimal_value}")