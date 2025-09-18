## 2D Toroidal Plasma Simulation
#This model simulates a cross-section of a torus—ideal for visualizing rotational plasma flow and magnetic confinement, like in a tokamak.

# Key Concepts: Toroidal coordinates simplified as a circular ring/ Plasma velocity wraps around the ring/ Magnetic field pinches inward for confinement/ Symbolic resonance pulses along the loop
# Python Scaffold: prism36_mhd_2d_torus.py

import numpy as np
import matplotlib.pyplot as plt

# Grid setup (2D torus cross-section)
N = 100
theta = np.linspace(0, 2*np.pi, N)
r_major = 1.0  # Major radius
r_minor = 0.3  # Minor radius

# Parametric torus coordinates
X = (r_major + r_minor * np.cos(theta)) * np.cos(theta)
Y = (r_major + r_minor * np.cos(theta)) * np.sin(theta)

# Initial plasma density (symbolic pulse)
rho = 1 + 0.2 * np.sin(3 * theta)

# Velocity field (toroidal rotation)
v_x = -np.sin(theta)
v_y = np.cos(theta)

# Magnetic field (pinch inward)
B_x = -0.5 * np.cos(theta)
B_y = -0.5 * np.sin(theta)

# Time evolution
dt = 0.01
steps = 100

for t in range(steps):
    rho = 1 + 0.2 * np.sin(3 * theta + t * dt)

    plt.clf()
    plt.plot(X, Y, 'k--', alpha=0.3)
    plt.scatter(X, Y, c=rho, cmap='plasma', s=60, edgecolors='k')
    plt.quiver(X, Y, B_x, B_y, color='cyan', scale=20)
    plt.title(f"Prism36 Toroidal Plasma – Frame {t}")
    plt.axis('equal')
    plt.pause(0.05)

plt.show()
