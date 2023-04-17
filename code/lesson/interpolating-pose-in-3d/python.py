import spatialmath.base as smb
import spatialmath as sm
import roboticstoolbox as rtb

# 1:11 - 2:26
T0 = sm.SE3()

T1 = sm.SE3.Trans(1, 2, 3) * sm.SE3.RPY(0.6, 0.8, 1.4)

T = rtb.ctraj(T0, T1, 50)

print(T[0], "\n")

print(T[10])

smb.tranimate(T)
