import spatialmath.base as smb
import numpy as np
import matplotlib.pyplot as plt

# 5:22 - 6:40

print(smb.rotx(0.2), "\n")

print(smb.rotx(30, "deg"), "\n")

R = smb.rotx(30, "deg")

print(np.linalg.det(R), "\n")

print(np.linalg.inv(R), "\n")

print(np.transpose(R), "\n")

print(smb.roty(0.2), "\n")

print(smb.rotz(0.3), "\n")

smb.trplot(smb.rotz(0.3))
plt.show()