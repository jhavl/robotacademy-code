import machinevisiontoolbox as mv
import spatialmath as sm
import matplotlib.pyplot as plt

# 1:47
cam = mv.CentralCamera().Default()

# 1:59
P = (1, 1, 5)

# 2:09
p0 = cam.project_point(P)
print(p0, "\n")

# 2:52
px = cam.project_point(P, pose = sm.SE3.Trans(0.1, 0, 0))
print(px, "\n")

# 3:18
print((px-p0)/0.1, "\n")

# 3:47
print((cam.project_point(P, pose = sm.SE3.Trans(0, 0, 0.1))-p0)/0.1, "\n")

# 4:08
print((cam.project_point(P, pose = sm.SE3.Rx(0.1))-p0)/0.1, "\n")

# 4:47
cam.flowfield([1, 0, 0, 0, 0, 0])
plt.show()

# 5:02
cam.flowfield([0, 1, 0, 0, 0, 0])
plt.show()

# 5:22
cam.flowfield([0, 0, 1, 0, 0, 0])
plt.show()

# 5:38
cam.flowfield([0, 0, 0, 0, 0, 1])
plt.show()