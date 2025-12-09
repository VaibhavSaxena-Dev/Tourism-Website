# Code for the Solution using numerical method(euler's method)
import numpy as np
# Initial conditions
x0 = 0
y0 = 0
h = 0.1
steps = 5  # Number of steps

# Differential equation function
def f(x, y):
    return (np.pi / 2) * np.sqrt(1 - y**2)

# Euler's method
x_values = [x0]
y_values = [y0]

# Applying Euler's method for 5 steps
for i in range(steps):
    y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
    x_new = x_values[-1] + h
    x_values.append(x_new)
    y_values.append(y_new)

# Display results
for i in range(len(x_values)):
    print(f"x = {x_values[i]:.1f}, y = {y_values[i]:.5f}")