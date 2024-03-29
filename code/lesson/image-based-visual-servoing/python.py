import machinevisiontoolbox as mv
import spatialmath as sm
import numpy as np

# 6:23
cam = mv.CentralCamera().Default()

d = 0.5
z = 1
P = [[-d, np.sqrt(3)/2*d, z], [d, -np.sqrt(3)/2*d, z], [0, np.sqrt(3)/2*d, z]]
Tcam = sm.SE3.Trans(3.5, 3.5, -5)*sm.SE3.Rx(0.1)*sm.SE3.Ry(-0.1)*sm.SE3.Rz(0.2)

# 7:14
p = cam.plot_point(P, pose = Tcam)

# 8:07
J = cam.visjac_p(p, 5)
print(J, "\n")

# 8:19
print(np.linalg.inv(J), "\n")