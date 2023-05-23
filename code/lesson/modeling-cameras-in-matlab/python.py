import spatialmath as sm
import machinevisiontoolbox as mv
import numpy as np

# 0:31
P = np.asarray([[0.2], [0.3], [5]]) # for now have hardcoded until I find the function for this

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

# 3:01
print(cam.K,"\n")

# 3:06
print(cam.C(),"\n")

# 3:32

# 4:12

# 5:00
P = np.asarray([[-0.1, -0.1, 0.1, 0.1],[-0.1, 0.1, 0.1, -0.1],[0, 0, 0, 0]])
Pose = sm.SE3.Trans([0, 0, 4])*sm.SE3.Rz(np.pi/3)*sm.SE3.Ry(np.pi)

# 6:04
cam = mv.CentralCamera(f = 0.008, pp = [512, 512], rho=1e-5, pose = Pose)

# 6:13
p = cam.project_point(P)
print(p,"\n")

# 6:24
cam.plot_point(P)

# 6:47
cam.plot()

# 7:02
sm.plot_sphere(radius=0.05, centre = P)

input("press any key to exit")