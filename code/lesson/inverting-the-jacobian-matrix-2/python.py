import roboticstoolbox as rtb
import numpy as np

# 0:00 - 4:07
robot = rtb.models.DH.Puma560()
qn = [0, 0.785398163397448, 3.141592653589793, 0, 0.785398163397448, 0]
J = robot.jacobe(qn)
print(J, "\n")

print(np.linalg.det(J), "\n")

print(np.linalg.inv(J), "\n")

qz = [0, 0, 0, 0, 0, 0]
print(qz, "\n")

J = robot.jacobe(qz)
print(J, "\n")

J = robot.jacobe(qn)
print(J, "\n")

nu = [0, 0, 1, 0, 0, 0]

ans = np.matmul(np.linalg.inv(J), nu)
print(ans, "\n")
