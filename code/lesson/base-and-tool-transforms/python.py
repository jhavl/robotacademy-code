import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np

# 2:20
p560 = rtb.models.DH.Puma560()

print(p560, "\n")

print(p560.fkine([0.1, 0.2, 0.3, 0, 0, 0]), "\n")

# 3:02
p560.base = sm.SE3.Trans(10, 15, 2)

# 3:14
print(p560.fkine([0.1, 0.2, 0.3, 0, 0, 0]), "\n")

# 3:32
p560.base = sm.SE3.Trans(10, 15, 2)* sm.SE3.Rx(np.pi)

# 3:39
print(p560.fkine([0.1, 0.2, 0.3, 0, 0, 0]), "\n")

# 4:18
p560.tool = sm.SE3.Trans(0, 0, 0.2)

# 4:32
print(p560.fkine([0.1, 0.2, 0.3, 0, 0, 0]), "\n")

