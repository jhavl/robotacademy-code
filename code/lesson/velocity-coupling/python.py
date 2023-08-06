import roboticstoolbox as rtb
import sympy as sym

# 0:46
twolink = rtb.models.DH.Planar2(symbolic = True)

q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q1d = sym.Symbol('q1d')
q2d = sym.Symbol('q2d')

# 1:06
print(twolink.coriolis([q1, q2], [q1d, q2d]))