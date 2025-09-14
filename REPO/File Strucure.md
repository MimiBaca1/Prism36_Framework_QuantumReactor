## Ideal Repository Structure for Prism36 Quantum Reactor

Prism36 Reactor/
├── README.md
├── LICENSE
├── docs/
│   ├── overview.md
│   ├── theory/
│   │   ├── quaternions.md
│   │   ├── spinors.md
│   │   ├── symbolic-dirac.md
│   ├── architecture/
│   │   ├── prism36-geometry.md
│   │   ├── field-coupling.md
│   │   ├── vault-logic.md
│   └── implementation/
│       ├── numerical-modeling.md
│       ├── FEM-notes.md
│       ├── symbolic-computation.md
├── src/
│   ├── core/
│   │   ├── quaternion_field.py
│   │   ├── spinor_solver.py
│   │   ├── dirac_operator.py
│   ├── mesh/
│   │   ├── prism36_mesh.py
│   │   ├── boundary_conditions.py
│   ├── utils/
│   │   ├── symbolic_tools.py
│   │   ├── visualization.py
├── notebooks/
│   ├── demo_quaternion_rotation.ipynb
│   ├── symbolic_dirac_solver.ipynb
│   ├── prism36_simulation.ipynb
├── tests/
│   ├── test_quaternion_field.py
│   ├── test_spinor_solver.py
├── examples/
│   ├── sample_config.yaml
│   ├── sample_output/
│   │   ├── eigenmodes_plot.png
│   │   ├── field_map.json
└── requirements.txt
