# Numeric simulation for the Prism36 Quantum Reactor—testing resonance across the 36-node lattice using spinor vectors and harmonic amplitudes. This simulation will visualize how energy modulates across symbolic shell.

# What This Simulates: 36 nodes arranged on a spherical shell/ Resonance amplitudes modulated by harmonic functions Spinor vectors showing directional energy flow/ Color-coded visualization of resonance intensity

## Simulation: Prism36 Node Resonance (Numeric)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Set plot style
plt.style.use('seaborn-v0_8')

# Generate 36 nodes on a sphere using spherical coordinates
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

# Simulate harmonic resonance amplitudes
resonance_amplitudes = np.sin(3 * theta) * np.cos(2 * phi)

# Generate spinor vectors modulated by resonance
spinor_vectors = np.random.randn(36, 3)
spinor_vectors /= np.linalg.norm(spinor_vectors, axis=1)[:, np.newaxis]
spinor_vectors *= resonance_amplitudes[:, np.newaxis]

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot nodes with color-coded resonance amplitudes
sc = ax.scatter(x, y, z, c=resonance_amplitudes, cmap='plasma', s=60, edgecolors='k')

# Add spinor vectors as arrows
for i in range(36):
    ax.quiver(x[i], y[i], z[i], spinor_vectors[i,0], spinor_vectors[i,1], spinor_vectors[i,2], 
              length=0.2, normalize=True, color=cm.plasma((resonance_amplitudes[i] - min(resonance_amplitudes)) / (max(resonance_amplitudes) - min(resonance_amplitudes))) )

# Annotate plot
ax.set_title("Prism36 Node Resonance Simulation", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
fig.colorbar(sc, ax=ax, shrink=0.6, label='Resonance Amplitude')

# Save plot
plt.tight_layout()
plt.savefig("prism36_node_resonance.png")
plt.show()
