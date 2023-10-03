# The machine vision toolbox for python does not have the same functionality for homographies
import numpy as np
import spatialmath as sm
import machinevisiontoolbox as mv

# 0:00
P = mv.mkgrid(n=2, side=0.2)

cam = mv.CentralCamera.Default(imagesize=[1024, 1024], pp=[512, 512], pose = sm.SE3.Trans(0, 0, 4)*sm.SE3.Rz(np.pi/3)*sm.SE3.Ry(np.pi))

print(cam.project_point(P), "\n")

# 0:19
p = cam.project_point(P)
print(p, "\n")

# 0:26
print(P, "\n")

# 0:41
Q = P[:2,:]
print(Q, "\n")

# 1:07
H, resid = mv.CentralCamera.points2H(p, Q)
print(H, "\n")

# 1:31
print(mv.base.homtrans(H,p), "\n")

# 1:52
print(mv.base.homtrans(np.linalg.inv(H), Q), "\n")