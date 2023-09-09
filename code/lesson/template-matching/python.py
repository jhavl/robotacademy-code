import machinevisiontoolbox as mv

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
mx, p = S.peak2d(npeaks=5, scale = 1)
print(mx, "\n")
print(p, "\n")

# 8:14
crowd.draw_circle((int(p[0,0]),int(p[1,0])), 30, color = 0)
crowd.disp()

# 8:34
# machine vision toolbox does not support this kind of plot circle functionality

# 9:35
crowd.roi([int(p[0,0] ) - 25, int(p[0,0]) + 25, int(p[1,0]) - 25, int(p[1,0]) + 25]).disp()