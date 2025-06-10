import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_steps = 1000

# Step choices: +1 (right or up), -1 (left or down)
steps = np.random.choice([-1, 1], size=n_steps)

# Random walk: cumulative sum of steps
position = np.cumsum(steps) 

# Plot
plt.figure(figsize=(10, 4))
plt.plot(position)
plt.title("1D Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.grid(True)
plt.show()
