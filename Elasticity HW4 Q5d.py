import numpy as np

# Original stress tensor T in the ei basis set (MPa)
T_ei = np.array([[1, 3, -5], 
                 [3, 0, 0], 
                 [-5, 0, 1]])

# Transformation matrix Q from ei to ei'
Q = np.array([[0, -1, 0], 
              [-1/np.sqrt(5), 0, -2/np.sqrt(5)], 
              [2/np.sqrt(5), 0, -1/np.sqrt(5)]])

# Tensor components of T in the ei' basis set (T') are calculated as: T' = Q^T * T * Q
T_ei_prime = Q.T @ T_ei @ Q

T_ei_prime