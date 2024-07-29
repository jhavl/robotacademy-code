import spatialmath.base as smb
import numpy as np
import matplotlib.pyplot as plt

# 5:14 - 11:17

print(smb.transl2(1, 2), "\n")

print(smb.rot2(30, "deg"), "\n")

print(smb.trot2(30, "deg"), "\n")

print(np.matmul(smb.transl2(1, 2), smb.trot2(30, "deg")), "\n")

print(smb.trot2(30, "deg", t=[1, 2]), "\n")

T1 = smb.trot2(30, "deg", t=[1, 2])
print(T1, "\n")

smb.trplot2(T1)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()

T2 = smb.trot2(0, t=[2, 1])
print(T2, "\n")

smb.trplot2(T2)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()

T3 = np.matmul(T1, T2)
print(T3, "\n")

smb.trplot2(T3)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()

T4 = np.matmul(T2, T1)
print(T4, "\n")

smb.trplot2(T4)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()

P = np.asarray([[3], [2]])
print(P, "\n")

plt.plot(P[0], P[1], "b*")
plt.show()

P1 = np.matmul(np.linalg.inv(T1), [[3], [2], [1]])
print(P1)
