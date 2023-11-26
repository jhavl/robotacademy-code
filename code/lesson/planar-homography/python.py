import machinevisiontoolbox as mv
import numpy as np

# 3:31
camera = mv.CentralCamera.Default()
P = ....
camera.project_point(np.vstack([P,np.zeros((4, ))]))
H = mv.delete(camera.c(), 2, axis = 1)

# 3:40
im.warp_perspective(H)

# 8:09
camera = mv.CentralCamera.Default()
P = ....
camera.project_point(np.vstack([P,np.zeros((4, ))]))
H = mv.delete(camera.c(), 2, axis = 1)

Q = mv.homtrans(H, P)