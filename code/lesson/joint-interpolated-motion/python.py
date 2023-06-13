import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np

# 0:51
p560 = rtb.models.DH.Puma560()

# 1:11
TA = sm.SE3.Trans(0.4, 0.2, 0) * sm.SE3.Rx(np.pi)
print(TA, "\n")

# 1:32
TB = sm.SE3.Trans(0.4, -0.2, 0) * sm.SE3.Rx(np.pi/2)
print(TB, "\n")

# 1:44
qA = p560.ikine_a(TA)
print(qA, "\n")

# 1:52
qB = p560.ikine_a(TB)
print(qB, "\n")

# 2:04
tg = rtb.jtraj(qA, qB, 50)

# 2:25
p560.plot(tg)

# 2:43
rtb.qplot(tg)