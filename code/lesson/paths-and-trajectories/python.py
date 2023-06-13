import roboticstoolbox as rtb
import numpy as np
import spatialmath.base as smb
import spatialmath as sm
import matplotlib.pyplot as plt

# 0:45
T0 = np.identity(4)

T1 = np.matmul(smb.transl(1,2,3), smb.rpy2tr(0.6, 0.8, 1.4, order = 'xyz'))

# 1:36
smb.trplot(T0)
plt.show()

# 1:39
smb.trplot(T1)
plt.show()

# 1:53
T0 = sm.SE3(T0)
T1 = sm.SE3(T1)
traj = rtb.ctraj(T0, T1, t=100)
smb.tranimate(traj)