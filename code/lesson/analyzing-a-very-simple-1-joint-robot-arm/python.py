import roboticstoolbox as rtb
import sympy as sym

# 2:46
a1 = 1

# 2:50
q1 = 0.2

# 3:27
T = rtb.trchain2("R(q1) Tx(a1)", [q1], variables={"a1": a1})
print(T, "\n")

# 4:12
q1, a1 = sym.symbols("q1 a1")

# 4:15
T = rtb.trchain2("R(q1) Tx(a1)", [q1], variables={"a1": a1})
print(T, "\n")

# 4:31
p1 = rtb.models.DH.Planar1()

# 4:53
p1.teach()
