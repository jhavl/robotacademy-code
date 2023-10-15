import machinevisiontoolbox as mv
import numpy as np

# 2:00
out = im.erode(np.ones((3, 3)));

# 2:58
out = im.dilate(np.ones((3, 3)));

# 3:48
out = im.close(np.ones((3, 3)));

# 5:26
out = im.open(np.ones((3, 3)));