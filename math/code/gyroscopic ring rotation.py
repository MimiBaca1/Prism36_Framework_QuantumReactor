import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

style.use('seaborn-v0_8')

# Quaternion utilities
def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])

def quaternion_rotate(q, v):
    q_conj = np.array([q[0], -q[1], -q[2], -q[3]])
    v_quat = np.array([0] + list(v))
    return quaternion_multiply(quaternion_multiply(q, v_quat), q_conj)[1:]

def normalize_quaternion(q):
    return q / np.linalg.norm(q)

# Simulation parameters
num_steps = 200
angle_per_step = np.pi / 100  # small rotation per step
axis = np.array([0, 0, 1])  # rotation around z-axis
axis = axis / np.linalg.norm(axis)

# Initial orientation vector of the ring
initial_vector = np.array([1, 0, 0])

# Quaternion representing rotation per step
theta = angle_per_step
q_step = normalize_quaternion(np.array([
    np.cos(theta / 2),
    *(np.sin(theta / 2) * axis)
]))

# Simulate orientation over time
orientations = []
q_current = np.array([1, 0, 0, 0])  # identity quaternion
for _ in range(num_steps):
    q_current = normalize_quaternion(quaternion_multiply(q_step, q_current))
    rotated_vector = quaternion_rotate(q_current, initial_vector)
    orientations.append(rotated_vector)

orientations = np.array(orientations)

# Visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(orientations[:, 0], orientations[:, 1], orientations[:, 2], label='Gyroscopic Ring Orientation')
ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='Initial Orientation')
ax.set_title('Quaternion-Based Gyroscopic Ring Rotation')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.tight_layout()
plt.savefig('/mnt/data/gyroscopic_ring_quaternion_simulation.png')
plt.close()
