import machinevisiontoolbox as mv
import matplotlib.pyplot as plt
import numpy as np

# 0:21
im = mv.Image.Read('tomato_124.png', dtype= "float32")

# 0:25
im.disp()

# 1:56
im = mv.Image.Read('tomato_124.png', dtype= "float32", gamma = 2.2)

# 2:01
im.disp()

# 2:35
im[:, :, 0].disp()

# 2:44
im[:, :, 1].disp()

# 2:58
R = im[:, :, 0]

# 3:02
G = im[:, :, 1]

# 3:08
B = im[:, :, 2]

# 3:13
G.disp()

# 3:27
Y = R + G + B

# 3:36
Y.disp()

# 3:58
r = np.divide(np.asarray(R), np.asarray(Y))

# 4:20
g = np.divide(np.asarray(G), np.asarray(Y))

# 4:30
r.disp()

# 4:38
g.disp()

# 6:03
tom = (r > 0.8) and (g < 0.2)

# 6:07
tom.disp()

# 6:46
b = tom.blobs()

# 7:05
im.disp()

# 7:16
im.draw_box(ltrb=[b.bbox[0], b.bbox[2], b.bbox[1], b.bbox[3]], color=[0, 255, 0])