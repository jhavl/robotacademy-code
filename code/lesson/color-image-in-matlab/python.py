import machinevisiontoolbox as mv

# 0:19
im = mv.Image.Read('flowers8.png')

# 0:52
im.disp()

# 2:10
im[0].disp()

# 2:37
im[1].disp()

# 2:59
im[2].disp()

# 5:39
im = mv.Image.Read('flowers8.png')

# 5:52
print(im.image[99, 99, 0],"\n")
print(im.image[99, 99, 1],"\n")
print(im.image[99, 99, 2],"\n")

# 6:11
print(im.image[99, 99],"\n")