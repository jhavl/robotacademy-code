import roboticstoolbox as rtb
import numpy as np
import scipy

# 4:20 - 6:11
robot = rtb.models.DH.Hyper3d(N=20)

q = np.random.rand(20)
print(q, "\n")

robot.plot(q)

J = robot.jacobe(q)
print(J, "\n")

# This will just raise an error, comment out to run the rest
# print(np.linalg.inv(J), "\n")

print(np.linalg.pinv(J), "\n")

N = scipy.linalg.null_space(J)
print(N, "\n")

print(np.linalg.matrix_rank(J), "\n")
