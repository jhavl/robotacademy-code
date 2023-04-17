import spatialmath.base as smb
import roboticstoolbox as rtb
import numpy as np

# 2:14 - 6:57
x = rtb.jtraj([0, 0, 0], [-np.pi / 2, np.pi / 2, np.pi / 4], 100)

x.plot()

R = [smb.rpy2r(q) for q in x.q]

print(R[0], "\n")

print(R[10], "\n")

smb.tranimate(R)

q1 = smb.qunit([1, 0, 0, 0])
smb.qprint(q1)
print("\n")

q2 = smb.qunit(smb.r2q(smb.rotx(np.pi / 2)))
smb.qprint(q2)
print("\n")

smb.qprint(smb.qslerp(q1, q2, 0))
print("\n")

smb.qprint(smb.qslerp(q1, q2, 1))
print("\n")

smb.qprint(smb.qslerp(q1, q2, 0.5))
print("\n")

print(smb.q2r(smb.qslerp(q1, q2, 0.5)))
