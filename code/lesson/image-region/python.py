import machinevisiontoolbox as mv
import numpy as np

# 1:04
im = mv.Image.Read('shark1.png')

# 1:09
im.disp()

# 2:06
indices = np.argwhere(im > 0)
u, v = indices[:,0], indices[:,1]

# 2:24
print([u, v],"\n")

# 2:55
umin = min(u)
print(umin,"\n")

# 3:03
umax = max(u)
print(umax,"\n")

# 3:14
vmin = min(v)
print(vmin,"\n")

# 3:19
vmax = max(v)
print(vmax,"\n")

# 3:39
im.draw_box(lt = (umin, vmin), rb = (umax, vmax), color = 255)
im.disp()

# 4:08
uc = (umin + umax)/2
print(uc,"\n")

# 4:16
vc = (vmin + vmax)/2
print(vc, "\n")

# 4:32
im.draw_circle((int(uc), int(vc)), 1, color = 0, thickness = 3)
im.disp()

# 6:45
m00 = im.mpq(0, 0)
print(m00,"\n")

# 7:05
m10 = im.mpq(1, 0)
print(m10,"\n")

# 7:05
m01 = im.mpq(0, 1)
print(m01,"\n")

#7:30
ucen = m10 / m00
print(ucen,"\n")

# 7:38
vcen = m01 / m00
print(vcen,"\n")

im.draw_circle((int(ucen), int(vcen)), 1, color = 0, thickness = 3)
im.disp()