import machinevisiontoolbox as mv
import matplotlib.pyplot as plt

# 0:32
im = mv.Image.Read('monalisa.png', grey = True)

# 0:39
print(im)

# 0:57
im.disp()

# 1:43
print(im.image[193][275], "\n")

# 2:17
print(im.image[179:209,259:289], "\n")

# 2:36
im2 = mv.convert(im.image[179:209,259:289])
print(im2, "\n")

# 2:48
mv.idisp(im2)

# 3:19
lin = im.image[189,259:289]

# 3:30
plt.figure()
plt.plot(lin)
plt.show()

# 4:21
im3 = im.image[::4,::4]

# 4:24
mv.idisp(im3)

# 5:19
im4 = im.image[im.image.shape[0]::-4,im.image.shape[1]::-4]
print(im4)

# 5:23
mv.idisp(im4)

# 5:59
im4 = im.image[im.image.shape[0]::-1,:]