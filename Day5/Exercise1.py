import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 0], [1, 2]])

print(np.dot(a, b))

print(np.linalg.inv(a))

print(np.linalg.det(a))

eig_vals, eig_vecs = np.linalg.eig(a)
print("Eigenvalues:", eig_vals)
print("Eigenvectors:", eig_vecs)
