import spatialmath.base as smb
import numpy as np
import matplotlib.pyplot as plt

# 5:50 - 7:36
print(smb.rot2(0), "\n")
print(smb.rot2(0.2), "\n")

R = smb.rot2(30, "deg")

print(R, "\n")

c1 = R[:, 0]

print(c1, "\n")

c2 = R[:, 1]

print(c2, "\n")
print(np.dot(c1, c2), "\n")
print(np.linalg.det(R), "\n")
print(np.linalg.inv(R), "\n")
print(np.transpose(R), "\n")

smb.trplot2(R)
plt.xlim(-1, 1.5)
plt.ylim(-1, 1.5)
plt.show()
