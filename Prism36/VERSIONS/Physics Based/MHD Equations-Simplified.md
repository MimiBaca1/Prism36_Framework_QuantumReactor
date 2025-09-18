## 🔬 Magnetohydrodynamics (MHD) Equations

### 1. Continuity Equation (Mass Conservation)
$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
$$

### 2. Momentum Equation (Fluid Motion)
$$
\rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla) \mathbf{v} \right) = -\nabla p + \mathbf{J} \times \mathbf{B} + \mu \nabla^2 \mathbf{v}
$$

### 3. Induction Equation (Magnetic Field Evolution)
$$
\frac{\partial \mathbf{B}}{\partial t} = \nabla \times (\mathbf{v} \times \mathbf{B}) + \eta \nabla^2 \mathbf{B}
$$

### 4. Ohm’s Law (Current Density)
$$
\mathbf{J} = \nabla \times \mathbf{B}
$$

### 5. Energy Equation (Optional)
$$
\frac{\partial E}{\partial t} + \nabla \cdot \left[ (E + p) \mathbf{v} \right] = \text{heat + dissipation terms}
$$
