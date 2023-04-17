import spatialmath.base as smb
import numpy as np
import matplotlib.pyplot as plt

# 1:32 - 4:03

R = smb.eul2r(0.1, 0.2, 0.3)
print(R, "\n")

smb.trplot(R)
plt.show()

print(np.linalg.eig(R)[0], "\n")

e, v = np.linalg.eig(R)
print(v, "\n")
print(e, "\n")

print(smb.tr2angvec(R), "\n")

th, v = smb.tr2angvec(R)
print(th, "\n")
print(v, "\n")

print(smb.angvec2r(th, v), "\n")
