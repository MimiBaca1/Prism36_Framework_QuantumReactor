import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
from mpl_toolkits.mplot3d import Axes3D

# Set style for visualization
plt.style.use('seaborn-v0_8')

# Define Prism36 mesh using spherical coordinates with D18 symmetry approximation
def generate_prism36_mesh(radius=1.0):
    nodes = []
    for i in range(18):
        theta = 2 * np.pi * i / 18
        for j in range(2):
            phi = np.pi * j / 2  # 0 and pi/2
            x = radius * np.sin(phi) * np.cos(theta)
            y = radius * np.sin(phi) * np.sin(theta)
            z = radius * np.cos(phi)
            nodes.append((x, y, z))
    return np.array(nodes)

# Quaternionic field Φ(r) at each node (simplified as 4D vector)
def generate_quaternionic_field(nodes):
    field = []
    for x, y, z in nodes:
        norm = np.sqrt(x**2 + y**2 + z**2)
        q0 = np.cos(norm)
        q1 = x / (norm + 1e-6)
        q2 = y / (norm + 1e-6)
        q3 = z / (norm + 1e-6)
        field.append([q0, q1, q2, q3])
    return np.array(field)

# Dirac-like operator matrix (simplified Laplacian + mass term)
def build_dirac_operator(nodes, mass=1.0):
    N = len(nodes)
    H = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                dist = np.linalg.norm(nodes[i] - nodes[j])
                H[i, j] = -1.0 / (dist + 1e-6)
        H[i, i] = mass + np.sum(np.abs(H[i]))
    return H

# Generate mesh and field
nodes = generate_prism36_mesh()
field = generate_quaternionic_field(nodes)

# Build Dirac-like operator and solve eigenvalue problem
H = build_dirac_operator(nodes)
eigenvalues, eigenvectors = eigsh(H, k=6, which='SM')

# Visualize eigenmodes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
colors = plt.cm.viridis((eigenvalues - eigenvalues.min()) / (eigenvalues.max() - eigenvalues.min()))

for i, (x, y, z) in enumerate(nodes):
    ax.scatter(x, y, z, color=colors[i], s=60)

ax.set_title("Spinor Eigenmodes in Prism36 ARC Reactor")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.tight_layout()
plt.savefig("/mnt/data/prism36_spinor_eigenmodes.png")
plt.show()

# Print eigenvalues
print("Eigenvalues (En):", eigenvalues)
