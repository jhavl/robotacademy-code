import machinevisiontoolbox as mv

# 2:22
#im.ncc([-0.5, 0, 0.5])

# 3:35
#im.ncc(np.transpose([-0.5, 0, 0.5]))

# 5:22
im = mv.Image.Read('penguins.png', rgb = False, dtype = "float32")

# 5:24
im.disp()

input("press any key to exit")
