## ADD 2: Phase Alignment Tracking
#We’ll simulate phase alignment of spinor vectors by computing their angular deviation from a reference vector (e.g., the z-axis). This helps visualize symbolic resonance or cognition flow.

# Code Additions: Add this after spinor vector generation:
# Phase alignment tracking (angle from z-axis)
reference_vector = np.array([0, 0, 1])
dot_products = np.dot(spinor_vectors, reference_vector)
magnitudes = np.linalg.norm(spinor_vectors, axis=1)
phase_angles = np.arccos(dot_products / magnitudes)  # In radians

# Then add a second color map to visualize phase alignment.
# Overlay phase alignment as node edge color
sc_phase = ax.scatter(x, y, z, c=phase_angles, cmap='viridis', s=60, edgecolors='black')
fig.colorbar(sc_phase, ax=ax, shrink=0.6, label='Phase Alignment (radians)')
