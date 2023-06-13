import machinevisiontoolbox as mv
import numpy as np

# 0:16
a = 100
print(a, "\n")

# 0:22
b = 200
print(b, "\n")

# 0:25
print(a+b, "\n")

# 0:28
print(a-b, "\n")

# 0:31
print(a/b, "\n")

# 0:51
a = np.uint8(100)
print(a, " ", type(a), "\n")

# 1:03
b = np.uint8(200)
print(b, " ", type(b), "\n")

# 1:08
print(a+b, " ", type(a+b), "\n")

# 1:13
print(a-b, " ", type(a-b), "\n")

# 1:19
print(np.uint8(a/b), " ", type(np.uint8(a/b)), "\n")

# 3:10
im = mv.Image.Read('street.png')

im.disp()

# 3:43
imd = mv.Image.Read('street.png', dtype = "double")

# 4:02
imd.disp()

# 5:01
print(im, "\n")

# 5:07
print(imd, "\n")