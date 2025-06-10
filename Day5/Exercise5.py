import numpy as np
import matplotlib.pyplot as plt


# 2D random walk
n_steps = 1000
x_steps = np.random.choice([-1, 1], size=n_steps)
y_steps = np.random.choice([-1, 1], size=n_steps)

x_position = np.cumsum(x_steps)
y_position = np.cumsum(y_steps)

plt.figure(figsize=(6, 6))
plt.plot(x_position, y_position)
plt.title("2D Random Walk")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
