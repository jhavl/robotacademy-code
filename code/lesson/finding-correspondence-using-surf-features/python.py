import machinevisiontoolbox as mv

# 0:00
im1 = mv.Image.Read("building2-1.png")
im2 = mv.Image.Read("building2-2.png")

# 0:15
im1.stdisp(im2)

