import machinevisiontoolbox as mv
import numpy as np

# 2:32
cam = mv.CentralCamera(f = 0.008, pp = [512, 512], rho=1e-5)

# 3:03
J = cam.visjac_p((600, 600), 5)

# 3:19
print(np.matmul(J,[1, 0, 0, 0, 0, 0]))

# 3:38
print(np.matmul(J,[0, 1, 0, 0, 0, 0]))

# 3:53
print(np.matmul(J,[0, 0, 1, 0, 0, 0]))