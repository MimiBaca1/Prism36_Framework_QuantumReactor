from sympy import symbols, Matrix, I, Function, diff, simplify

# Coordinates and time
x, y, z, t = symbols('x y z t')

# Spinor field components
psi1 = Function('psi1')(x, y, z, t)
psi2 = Function('psi2')(x, y, z, t)
psi = Matrix([psi1, psi2])

# Quaternionic potential components
phi0, phi1, phi2, phi3 = symbols('phi0 phi1 phi2 phi3')

# Covariant derivative components
A_mu = Matrix([phi1, phi2, phi3, phi0])
D_mu = [diff(psi, coord) + I * A for coord, A in zip([x, y, z, t], A_mu)]

# Gamma matrices (simplified 2D representation)
gamma = [
    Matrix([[0, 1], [1, 0]]),
    Matrix([[0, -I], [I, 0]]),
    Matrix([[1, 0], [0, -1]]),
    Matrix([[0, 1], [-1, 0]])
]

# Dirac operator
m = symbols('m')
Dirac_op = sum([I * gamma[i] * D_mu[i] for i in range(4)]) - m * psi

# Simplify and display
print("Symbolic Dirac operator:")
print(simplify(Dirac_op))
