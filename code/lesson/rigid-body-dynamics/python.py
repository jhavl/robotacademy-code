import roboticstoolbox as rtb
import sympy as sym

# 0:21
twolink = rtb.models.DH.Planar2(symbolic = True)

# 0:51
q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q1d = sym.Symbol('q1d')
q2d = sym.Symbol('q2d')
q1dd = sym.Symbol('q1dd')
q2dd = sym.Symbol('q2dd')

# 1:27
tau = twolink.rne([q1, q2], qd = [q1d, q2d], qdd = [q1dd, q2dd])

# 1:31
print(tau[0], "\n")

# 2:10
print(tau[1], "\n")