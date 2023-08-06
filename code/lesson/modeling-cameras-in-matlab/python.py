import spatialmath as sm
import spatialmath.base as smb
import machinevisiontoolbox as mv
import numpy as np
import matplotlib.pyplot as plt

# 0:31
P = np.asarray([0.2, 0.3, 5])

# 0:47
cam = mv.CentralCamera(f = 0.008, pp = [0, 0], rho=1)

# 0:1:06
p = cam.project_point(P)
print(p,"\n")

# 2:06
cam = mv.CentralCamera(f = 0.008, pp = [512, 512], rho=1e-5, imagesize = [1024, 1024])

# 2:38
p = cam.project_point(P)
print(p,"\n")

# 2:48
cam.plot_point(P)
plt.show()

# 3:01
print(cam.K,"\n")

# 3:06
print(cam.C(),"\n")

# 3:32
print(cam.project_point(P, pose = sm.SE3.Trans(0.1, 0, 0)), "\n")

# 4:12
print(cam.project_point(P, pose = sm.SE3.Ry(0.1)), "\n")

# 5:00
P = np.asarray([[-0.1, -0.1, 0.1, 0.1],[-0.1, 0.1, 0.1, -0.1],[0, 0, 0, 0]])
Pose = sm.SE3.Trans(0, 0, 4)*sm.SE3.Rz(np.pi/3)*sm.SE3.Ry(np.pi)

# 6:04
cam = mv.CentralCamera(f = 0.008, pp = [512, 512], rho=1e-5, imagesize = [1024, 1024], pose = Pose)

# 6:13
p = cam.project_point(P)
print(p,"\n")

# 6:24
cam.plot_point(P)
plt.show()

# 6:47
cam.plot()
plt.show()

# 7:02
smb.plot_sphere(radius=0.05, centre = P)
plt.show()