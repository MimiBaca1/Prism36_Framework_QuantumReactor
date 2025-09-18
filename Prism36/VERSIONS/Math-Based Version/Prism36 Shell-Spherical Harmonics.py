## The math-based simulation of the Prism36 shell using spherical harmonics and symbolic modeling. This Python module uses sympy for symbolic math and scipy.special for harmonic evaluation, allowing you to visualize and analyze resonance patterns across the 36-node lattice.

#What This Does: Defines symbolic spherical harmonics using sympy/ Evaluates them numerically using scipy.special.sph_harm/ Maps 36 nodes on a sphere and visualizes resonance amplitudes/Ready for symbolic eigenmode extraction or symmetry analysis

#🔗 Notes SciPy’s sph_harm uses the convention: sph_harm(m, l, theta, phi) You can change l_val and m_val to explore different harmonic modes Symbolic expressions can be expanded further using sympy for algebraic analysis


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
import sympy as sp

# Define symbolic variables
theta_sym, phi_sym = sp.symbols('theta phi')
l, m = sp.symbols('l m', integer=True)

# Symbolic spherical harmonic expression (real part)
Y_lm_expr = sp.re(sp.functions.special.spherical_harmonics.Ynm(l, m, theta_sym, phi_sym))

# Generate 36 nodes on a sphere
theta_vals = np.linspace(0, np.pi, 6)
phi_vals = np.linspace(0, 2*np.pi, 6)
theta_grid, phi_grid = np.meshgrid(theta_vals, phi_vals)
theta = theta_grid.flatten()
phi = phi_grid.flatten()

# Convert to Cartesian coordinates
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Evaluate spherical harmonics numerically
l_val = 3  # Degree
m_val = 2  # Order
Y_lm_vals = sph_harm(m_val, l_val, phi, theta)  # SciPy uses (m, l, theta, phi)
resonance_amplitudes = np.real(Y_lm_vals)

# Plot the resonance field
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x, y, z, c=resonance_amplitudes, cmap='viridis', s=60, edgecolors='k')

# Annotate plot
ax.set_title(f"Prism36 Spherical Harmonic Resonance (l={l_val}, m={m_val})", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
fig.colorbar(sc, ax=ax, shrink=0.6, label='Resonance Amplitude')

plt.tight_layout()
plt.savefig("prism36_math_resonance.png")
plt.show()
