## ADD 3: Step 3: Time Evolution of Resonance Patterns
# We’ll animate the resonance amplitudes and spinor vectors over time using a simple sinusoidal modulation.

# Code Additions: Replace static amplitude generation with a time-evolving function:
# Time evolution setup
frames = 50
for t in range(frames):
    ax.clear()
    
    # Update resonance amplitudes over time
    resonance_amplitudes = np.sin(3 * theta + 0.1 * t) * np.cos(2 * phi + 0.05 * t)
    
    # Update spinor vectors
    spinor_vectors = np.random.randn(36, 3)
    spinor_vectors /= np.linalg.norm(spinor_vectors, axis=1)[:, np.newaxis]
    spinor_vectors *= resonance_amplitudes[:, np.newaxis]
    
    # Replot nodes and vectors
    sc = ax.scatter(x, y, z, c=resonance_amplitudes, cmap='plasma', s=60, edgecolors='k')
    for i in range(36):
        ax.quiver(x[i], y[i], z[i], spinor_vectors[i,0], spinor_vectors[i,1], spinor_vectors[i,2], 
                  length=0.2, normalize=True, color=cm.plasma((resonance_amplitudes[i] - min(resonance_amplitudes)) / (max(resonance_amplitudes) - min(resonance_amplitudes))) )
    
    # Replot gyroscopic rings
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
    plt.pause(0.05)
