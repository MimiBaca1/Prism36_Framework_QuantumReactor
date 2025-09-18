## Here’s your fully modularized version of the Prism36 Node Resonance Simulation—structured as a clean Python module.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Set plot style
plt.style.use('seaborn-v0_8')

def generate_nodes():
    theta = np.linspace(0, np.pi, 6)
    phi = np.linspace(0, 2*np.pi, 6)
    theta, phi = np.meshgrid(theta, phi)
    theta = theta.flatten()
    phi = phi.flatten()

    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    return x, y, z, theta, phi

def compute_resonance(theta, phi, t):
    return np.sin(3 * theta + 0.1 * t) * np.cos(2 * phi + 0.05 * t)

def generate_spinors(amplitudes):
    spinors = np.random.randn(36, 3)
    spinors /= np.linalg.norm(spinors, axis=1)[:, np.newaxis]
    spinors *= amplitudes[:, np.newaxis]
    return spinors

def plot_frame(x, y, z, spinors, amplitudes, t, ax, ring_radii, ring_colors):
    ax.clear()
    sc = ax.scatter(x, y, z, c=amplitudes, cmap='plasma', s=60, edgecolors='k')

    for i in range(36):
        ax.quiver(x[i], y[i], z[i], spinors[i,0], spinors[i,1], spinors[i,2], 
                  length=0.2, normalize=True, color=cm.plasma((amplitudes[i] - min(amplitudes)) / (max(amplitudes) - min(amplitudes))) )

    for r, color in zip(ring_radii, ring_colors):
        phi_ring = np.linspace(0, 2*np.pi, 100)
        x_ring = r * np.cos(phi_ring)
        y_ring = r * np.sin(phi_ring)
        z_ring = np.zeros_like(phi_ring)
        ax.plot(x_ring, y_ring, z_ring, color=color, linewidth=1.5, alpha=0.6)

    ax.set_title(f"Prism36 Resonance – Frame {t}", fontsize=14)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

def run_simulation(frames=50):
    x, y, z, theta, phi = generate_nodes()
    ring_radii = [1.1, 1.2, 1.3]
    ring_colors = ['cyan', 'magenta', 'lime']

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    for t in range(frames):
        amplitudes = compute_resonance(theta, phi, t)
        spinors = generate_spinors(amplitudes)
        plot_frame(x, y, z, spinors, amplitudes, t, ax, ring_radii, ring_colors)
        plt.pause(0.05)

    plt.tight_layout()
    plt.savefig("prism36_node_resonance.png")
    plt.show()

if __name__ == "__main__":
    run_simulation()
