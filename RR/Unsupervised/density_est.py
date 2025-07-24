from sklearn.neighbors import KernelDensity
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Your 2D data
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# Project onto 1D axis (e.g., x-axis)
x_proj = X[:, 0]

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
kde.score_samples(X)

# Plot histogram as density estimator
plt.hist(x_proj, bins=10, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title("Histogram Density Estimation (x-axis projection)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()

plt.hist2d(X[:, 0], X[:, 1], bins=10, density=True, cmap='Blues')
plt.colorbar(label='Density')
plt.title("2D Histogram Density Estimation")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()



