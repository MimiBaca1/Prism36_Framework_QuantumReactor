import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Define Prism36 node geometry on a sphere
num_nodes = 36
radius = 1.0
nodes = []
for i in range(num_nodes):
    theta = 2 * np.pi * (i / num_nodes)
    phi = np.arccos(1 - 2 * (i / num_nodes))
    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)
    nodes.append((x, y, z))
nodes = np.array(nodes)

# Step 2: Assign quaternionic field values Φₙ at each node (4-component vectors)
# For simplicity, use random values normalized to unit quaternions
def random_unit_quaternion():
    q = np.random.randn(4)
    return q / np.linalg.norm(q)

fields = np.array([random_unit_quaternion() for _ in range(num_nodes)])

# Step 3: Construct Dirac Hamiltonian matrix H using simplified covariant derivatives
# For demonstration, use a symmetric matrix with quaternionic influence
H = lil_matrix((num_nodes, num_nodes))
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            dist = np.linalg.norm(nodes[i] - nodes[j])
            coupling = np.dot(fields[i], fields[j]) / dist
            H[i, j] = coupling
        else:
            H[i, i] = np.dot(fields[i], fields[i])

# Convert to CSR format for efficient computation
H = H.tocsr()

# Step 4: Solve eigenvalue problem Hψₙ = Eₙψₙ
num_eigenvalues = 6
eigenvalues, eigenvectors = eigsh(H, k=num_eigenvalues, which='SM')

# Step 5: Visualize eigenvalues and node positions
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(nodes[:, 0], nodes[:, 1], nodes[:, 2], c=eigenvalues[0] * np.ones(num_nodes), cmap='viridis', s=50)
ax.set_title('Prism36 Node Geometry with Spinor Field Eigenvalue Overlay')
plt.savefig('/mnt/data/prism36_spinor_field_eigenvalues.png')

# Print eigenvalues
print("Eigenvalues of Dirac Hamiltonian:")
print(eigenvalues)  # Display the lowest eigenvalues
