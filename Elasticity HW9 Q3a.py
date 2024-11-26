import numpy as np
import math

# Define the rotation matrix R1 for N1
theta1 = 30 * np.pi / 180  # Convert to radians for 30 degrees
R1 = np.array([[np.cos(theta1), np.sin(theta1), 0],
               [-np.sin(theta1), np.cos(theta1), 0],
               [0, 0, 1]])

# Define the rotation matrix R2 for N2 (120 degrees counterclockwise)
theta2 = 120 * np.pi / 180  # Convert to radians for 120 degrees
R2 = np.array([[np.cos(theta2), np.sin(theta2), 0],
               [-np.sin(theta2), np.cos(theta2), 0],
               [0, 0, 1]])

# Combine the rotations to form the total rotation matrix
R_total = R2 @ R1
R_total

# Define the Right Cauchy Stretch Tensor U in the principal axes basis
U_principal = np.array([[3/2, 0, 0],
                        [0, 1/2, 0],
                        [0, 0, 1]])

# Compute U in the global frame by R_total * U * R_total^T
U_global = R_total @ U_principal @ R_total.T
U_global

print(f"\nR_total:\n \n{R_total}\n")
print(f"\nU_global:\n \n{U_global}\n")