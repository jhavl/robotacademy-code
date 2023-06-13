import roboticstoolbox as rtb
import sympy as sym
import numpy as np

# 0:40
twolink = rtb.models.DH.Planar2(symbolic = True)

q1 = sym.Symbol('q1')
q2 = sym.Symbol('q2')
q1d = sym.Symbol('q1d')
q2d = sym.Symbol('q2d')
q1dd = sym.Symbol('q1dd')
q2dd = sym.Symbol('q2dd')

# 1:00
print(twolink.gravload([q1, q2]), "\n")

# 3:04
twolink = rtb.models.DH.Planar2()

# 3:18
print(twolink.gravload([0, 0]), "\n")

# 3:38
twolink.plot([0, 0])

# 3:49
twolink.plot([np.pi/2, 0])

# 4:06
print(twolink.gravload([np.pi/2, 0]), "\n")

# 4:57
print(twolink.payload(1, [0, 0, 0]), "\n")

# 5:14
print(twolink.gravload([0, 0]), "\n")

# 5:22
twolink.plot([0, 0])

# 5:40
p560 = rtb.models.DH.Puma560()

# 5:57
print(p560.gravload([0, 0, 0, 0, 0, 0]), "\n")

# 6:08
p560.plot([0, 0, 0, 0, 0, 0])

# 6:37
p560 = p560.gravity([0, 0, 9.81/6])

# 6:50
print(p560.gravload([0, 0, 0, 0, 0, 0]), "\n")