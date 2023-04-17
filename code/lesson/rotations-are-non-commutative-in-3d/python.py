import spatialmath.base as smb
import numpy as np

# 1:32 - 1:44

ans = np.matmul(smb.rotx(np.pi / 2), smb.roty(np.pi / 2))
print(ans, "\n")

ans = np.matmul(smb.roty(np.pi / 2), smb.rotx(np.pi / 2))
print(ans, "\n")
