import roboticstoolbox as rtb
import sympy as sym

# 2:31
a1, a2, a3, q1, q2, q3 = sym.symbols("a1 a2 a3 q1 q2 q3")

# 3:10
T = rtb.trchain2(
    "R(q1) Tx(a1) R(q2) Tx(a2) R(q3) Tx(a3)",
    [q1, q2, q3],
    variables={"a1": a1, "a2": a2, "a3": a3},
)
print(T, "\n")

# 3:32
x = T[0, 2]
print(x, "\n")

# 3:49
p3 = rtb.models.DH.Planar3()

# 3:59
p3.teach()
