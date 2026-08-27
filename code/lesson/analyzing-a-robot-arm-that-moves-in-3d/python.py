import roboticstoolbox as rtb
import sympy as sym

# 4:00
a1, a2, a3, a4, q1, q2, q3, q4 = sym.symbols("a1 a2 a3 a4 q1 q2 q3 q4")

# 5:06
T = rtb.trchain(
    "Rz(q1)Tz(a1)Ry(q2)Tz(a2)Ry(q3)Tz(a3)Ry(q4)Tz(a4)",
    [q1, q2, q3, q4],
    variables={"a1": a1, "a2": a2, "a3": a3, "a4": a4},
)
print(T, "\n")

# 5:41
print(T[0, 3])
