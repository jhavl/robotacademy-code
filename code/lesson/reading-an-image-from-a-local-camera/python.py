import machinevisiontoolbox as mv

# 1:01
cam = mv.VideoCamera(0)

# 1:24
cam.grab().disp()

# 1:38
im = cam.grab()

# 1:46
cam.grab().disp()

# 2:04
cam.release()