import roboticstoolbox as rtb
import numpy as np
import sympy as sym

# 3:08
a1 = 1
a2 = 1
q1 = 0.2
q2 = 0.3

# 3:53
T = rtb.trchain2("R(q1) Tx(a1) R(q2) Tx(a2)", [q1, q2], variables={"a1": a1, "a2": a2})
print(T, "\n")

# 4:21
q1, q2, a1, a2 = sym.symbols("q1 q2 a1 a2")

# 4:30
T = rtb.trchain2("R(q1) Tx(a1) R(q2) Tx(a2)", [q1, q2], variables={"a1": a1, "a2": a2})
print(T, "\n")

# 4:50
p2 = rtb.models.DH.Planar2()

# 5:00
p2.teach()

# 5:35
p2.plot([0, np.pi / 2])

# 5:49
p2.plot([np.pi / 2, -np.pi / 2])
