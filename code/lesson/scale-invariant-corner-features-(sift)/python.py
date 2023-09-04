import machinevisiontoolbox as mv

# 2:22
im = mv.Image.Read("building2-1.png")

# 2:25
im.disp()

# 2:47
C = im.SIFT()

# 2:57
print(C[0])

# 3:37
im2 = mv.Image.colorize(im)
C[0].draw(im2)
im2.disp()

# 4:04
im.disp(darken = True) 

# 4:14
im2 = mv.Image.colorize(im)
C.draw(im2)
im2.disp()

# 6:10
d = C[0].descriptor