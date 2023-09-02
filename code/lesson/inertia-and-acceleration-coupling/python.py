import roboticstoolbox as rtb
import sympy as sym
import numpy as np

# 0:12
# Python Robotics toolbox does not support symbolics for use in these functions

# 0:29
# Python Robotics toolbox does not support symbolics for use in these functions

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