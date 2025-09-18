## Symbolic Simulation Module: 
# What This Does: Constructs the Dirac operator symbolically/ Applies it to a 4-component spinor field /Outputs the full symbolic system of equations/ Ready for eigenmode extraction, symmetry analysis, or symbolic simplification

#prism36_dirac_solver.py
import sympy as sp

# Define spacetime coordinates
t, x, y, z = sp.symbols('t x y z')

# Define spinor components
psi1, psi2, psi3, psi4 = sp.symbols('psi1 psi2 psi3 psi4')
psi = sp.Matrix([psi1, psi2, psi3, psi4])

# Define mass term
m = sp.Symbol('m')

# Define gamma matrices (Dirac representation)
gamma0 = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, -1]
])

gamma1 = sp.Matrix([
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, -1, 0, 0],
    [-1, 0, 0, 0]
])

gamma2 = sp.Matrix([
    [0, 0, 0, -sp.I],
    [0, 0, sp.I, 0],
    [0, sp.I, 0, 0],
    [-sp.I, 0, 0, 0]
])

gamma3 = sp.Matrix([
    [0, 0, 1, 0],
    [0, 0, 0, -1],
    [-1, 0, 0, 0],
    [0, 1, 0, 0]
])

# Define partial derivatives of psi
d_psi_t = sp.Matrix([sp.diff(psi1, t), sp.diff(psi2, t), sp.diff(psi3, t), sp.diff(psi4, t)])
d_psi_x = sp.Matrix([sp.diff(psi1, x), sp.diff(psi2, x), sp.diff(psi3, x), sp.diff(psi4, x)])
d_psi_y = sp.Matrix([sp.diff(psi1, y), sp.diff(psi2, y), sp.diff(psi3, y), sp.diff(psi4, y)])
d_psi_z = sp.Matrix([sp.diff(psi1, z), sp.diff(psi2, z), sp.diff(psi3, z), sp.diff(psi4, z)])

# Construct Dirac operator
dirac_op = sp.I * (gamma0 * d_psi_t + gamma1 * d_psi_x + gamma2 * d_psi_y + gamma3 * d_psi_z) - m * sp.eye(4)

# Apply operator to spinor field
equation = dirac_op * psi

# Display symbolic Dirac equation
for i in range(4):
    print(f"Equation {i+1}:")
    sp.pprint(equation[i])
    print()
