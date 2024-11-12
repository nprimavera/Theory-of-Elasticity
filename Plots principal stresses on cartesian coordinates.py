import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Cartesian basis vectors {e_i}
e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.array([0, 0, 1])

# Define the principal stress basis vectors {n_i}
n1 = np.array([0, -3/5, 4/5])
n2 = np.array([1, 0, 0])
n3 = np.array([0, 4/5, 3/5])

# Plot the vectors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot e_i (Cartesian basis)
ax.quiver(0, 0, 0, e1[0], e1[1], e1[2], color='r', label='e1 (x-axis)', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, e2[0], e2[1], e2[2], color='g', label='e2 (y-axis)', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, e3[0], e3[1], e3[2], color='b', label='e3 (z-axis)', arrow_length_ratio=0.1)

# Plot n_i (Principal stress basis)
ax.quiver(0, 0, 0, n1[0], n1[1], n1[2], color='orange', label='n1 (Principal 1)', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, n2[0], n2[1], n2[2], color='purple', label='n2 (Principal 2)', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, n3[0], n3[1], n3[2], color='cyan', label='n3 (Principal 3)', arrow_length_ratio=0.1)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the aspect ratio for better viewing
ax.set_box_aspect([1, 1, 1])

# Add legend
ax.legend()

# Display the plot
plt.show()
