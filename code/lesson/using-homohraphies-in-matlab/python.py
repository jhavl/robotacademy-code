import spatialmath as sm
import spatialmath.base as smb
import machinevisiontoolbox as mv
import numpy as np

# 0:00
P = np.asarray([[-0.1, -0.1, 0.1, 0.1],[-0.1, 0.1, 0.1, -0.1],[0, 0, 0, 0]])
Pose = sm.SE3.Trans([0, 0, 4])*sm.SE3.Rz(np.pi/3)*sm.SE3.Ry(np.pi)
cam = mv.CentralCamera(f = 0.008, pp = [512, 512], rho=1e-5, pose = Pose)

# 0:19
p = cam.project_point(P)
print(p,"\n")

# 0:26
print(P,"\n")

#  0:41
Q = P[:2]
print(Q,"\n")

# 1:07
# H = mv.homography(p,Q)

# 1:31
#print(smb.homtrans(H,p))

# 1:52
#print(smb.homtrans(np.linalg.inv(H),p))
