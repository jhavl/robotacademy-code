import roboticstoolbox as rtb
import sympy as sym

# 7:08
twolink = rtb.models.DH.Planar2()


# 8:22
tau = twolink.rne([0, 0], qd = [0, 0], qdd = [0, 0])

# 2:10
twolink.plot([0, 0])

input("Press any key to exit")