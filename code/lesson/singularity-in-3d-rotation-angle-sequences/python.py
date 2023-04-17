import spatialmath.base as smb
import numpy as np

# 0:20 - 0:36

print(smb.rpy2r([0.3, np.pi / 2, 0.5], order="xyz"), "\n")

ans = smb.rpy2r([0.3, np.pi / 2, 0.5], order="xyz")
print(smb.tr2rpy(ans, order="xyz"))
