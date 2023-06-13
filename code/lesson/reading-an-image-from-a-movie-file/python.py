import machinevisiontoolbox as mv

# 1:18
video = mv.VideoFile("traffic_sequence.mp4")
cam = (im for im in video)

# 1:31
next(cam, None).disp()

# 1:37
next(cam, None).disp()

# 1:38
next(cam, None).disp()

# 1:40
next(cam, None).disp()

# 1:41
next(cam, None).disp()

# 1:42
next(cam, None).disp()

# 1:50
print(cam)