import machinevisiontoolbox as mv

# 2:22
im = mv.Image.Read("building2-1.png")

# 2:25
im.disp()

# 2:47
C = im.SIFT()

# 2:57
print(C[0])

# 4:04
im.disp(darken = True) 

# 6:10
print(C[0].descriptor)