import roboticstoolbox as rtb
import sympy as sym
import numpy as np

# 0:12
twolink = rtb.models.DH.Planar2(symbolic = True)

q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q1d = sym.Symbol('q1d')
q2d = sym.Symbol('q2d')
q1dd = sym.Symbol('q1dd')
q2dd = sym.Symbol('q2dd')

# 0:29
#twolink.inertia([q1, q2])

# 2:44
twolink = rtb.models.DH.Planar2()

# 2:55
twolink.inertia([0, 0])

# 3:06
twolink.plot([0, 0])

# 3:21
twolink.plot([0, np.pi/2])

# 3:29
twolink.inertia([0, np.pi/2])

# 3:56
twolink.plot([0, np.pi])

# 4:10
twolink.inertia([0, np.pi])

input("Press any key to exit")