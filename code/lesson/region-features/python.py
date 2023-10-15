import machinevisiontoolbox as mv
from spatialmath.base import *
import numpy as np

# 4:03
im = mv.Image.Read('shark2a.png')

# 4:07
im.disp()

# 4:21
b = mv.Blobs(im)
print(b)

# 6:32
im.disp(block=None)
E = np.array([[b[0].moments.mu20, b[0].moments.mu11],[b[0].moments.mu11, b[0].moments.mu02]])
plot_ellipse(4 * E/b[0].moments.m00, centre=(b[0].centroid[0], b[0].centroid[1]), inverted=True, color="green")
E = np.array([[b[1].moments.mu20, b[1].moments.mu11],[b[1].moments.mu11, b[1].moments.mu02]])
plot_ellipse(4 * E/b[1].moments.m00, centre=(b[1].centroid[0], b[1].centroid[1]), inverted=True, color="green")

# 6:42
im.disp(block=None)
plot_point((b[0].centroid[0], b[0].centroid[1]), color = "blue")
plot_point((b[1].centroid[0], b[1].centroid[1]), color = "blue")