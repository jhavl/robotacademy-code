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
print(qA.q, "\n")

# 1:52
qB = p560.ikine_a(TB)
print(qB.q, "\n")

# 2:04
tg = rtb.jtraj(qA.q, qB.q, 50)

# 2:25
p560.plot(tg.q)

# 2:43
rtb.xplot(np.arange(0, 50, 1), tg.q)