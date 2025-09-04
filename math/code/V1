import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Set plot style
plt.style.use('seaborn-v0_8')

# Generate 36 quaternionic nodes mapped into 3D space (example: points on a sphere)
np.random.seed(42)
theta = np.linspace(0, np.pi, 6)
phi = np.linspace(0, 2*np.pi, 6)
theta, phi = np.meshgrid(theta, phi)
theta = theta.flatten()
phi = phi.flatten()

x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

nodes = np.vstack((x, y, z)).T

# Simulated eigenmode amplitudes (example values)
eigen_amplitudes = np.sin(3 * theta) * np.cos(2 * phi)

# Simulated spinor field vectors (example: random unit vectors modulated by amplitude)
spinor_vectors = np.random.randn(36, 3)
spinor_vectors /= np.linalg.norm(spinor_vectors, axis=1)[:, np.newaxis]
spinor_vectors *= eigen_amplitudes[:, np.newaxis]

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot nodes with color-coded amplitudes
sc = ax.scatter(x, y, z, c=eigen_amplitudes, cmap='coolwarm', s=60, edgecolors='k')

# Add spinor vectors as arrows
for i in range(36):
    ax.quiver(x[i], y[i], z[i], spinor_vectors[i,0], spinor_vectors[i,1], spinor_vectors[i,2], 
              length=0.2, normalize=True, color=cm.coolwarm((eigen_amplitudes[i] - min(eigen_amplitudes)) / (max(eigen_amplitudes) - min(eigen_amplitudes))) )

# Highlight symmetry-induced degeneracies (example: mark nodes with similar amplitudes)
degenerate_indices = np.where(np.abs(eigen_amplitudes - np.mean(eigen_amplitudes)) < 0.1)[0]
ax.scatter(x[degenerate_indices], y[degenerate_indices], z[degenerate_indices], s=100, facecolors='none', edgecolors='black', linewidths=2)

# Annotate plot
ax.set_title("Spinor Eigenmodes in Prism36 Quaternionic Shell", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
fig.colorbar(sc, ax=ax, shrink=0.6, label='Eigenmode Amplitude')

# Save plot
plt.tight_layout()
plt.savefig("/mnt/data/prism36_spinor_eigenmodes.png")
plt.close()
