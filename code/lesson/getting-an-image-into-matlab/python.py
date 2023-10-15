import machinevisiontoolbox as mv

# 0:37
im = mv.Image.Read("P1030150.jpg")

# 0:47
im.disp()

# 1:19
im = mv.Image.Read("P1030150.jpg")

# 1:22
print(im, "\n")

# 1:38
print(im.metadata, "\n")

# 2:26
im = mv.Image.Read("street.png")

# 4:07
im.disp()

# 6:07
print(im.image[652, 561])