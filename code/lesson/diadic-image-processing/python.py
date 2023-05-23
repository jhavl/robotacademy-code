import machinevisiontoolbox as mv

# 5:24
cam = mv.VideoFile("traffic_sequence.mp4",dtype = "float32", grey = 1)
images = (im for im in cam)

# 5:44
im1 = next(images, None)

# 5:53
im2 = next(images, None)

# 6:02
mv.idisp(im1.image - im2.image)

input("press any key to close")

