import machinevisiontoolbox as mv
import numpy as np

# 2:09
print(mv.name2color("maroon"),"\n")

# 2:44
print(mv.color2name([0.1, 0.2, 0.3]),"\n")

# 3:13
pix = np.ones(3)
print(pix,"\n")

# 3:26
pix = mv.name2color("maroon")
print(pix)