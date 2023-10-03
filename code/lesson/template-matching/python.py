import machinevisiontoolbox as mv
import matplotlib.pyplot as plt
# 3:32
crowd = mv.Image.Read('wheres-wally.png', dtype= "float32", mono=True)

# 3:36
crowd.disp()

# 3:53
bender = mv.Image.Read('wally.png', dtype= "float32", mono=True)

# 4:09
bender.disp()

# 5:03
S = crowd.similarity(bender, "zncc")

# 5:12
S.disp(colormap="signed", colorbar=True)

# 6:48
maxima, location = S.peak2d(npeaks=5, scale = 1)
print(maxima, "\n")
print(location, "\n")

# 8:14
crowd.disp()
mv.base.plot_circle(centre=location, radius=20, color="k");

# 8:34
mv.base.plot_point(location, color="none", marker="none", text=" #{}");

# 9:35
crowd.roi([location[0, 0], location[0, 0]+30, location[1, 0], location[1, 0]+30]).disp()