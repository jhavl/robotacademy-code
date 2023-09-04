import machinevisiontoolbox as mv

# 2:22
#im.ncc([-0.5, 0, 0.5])

# 3:35
#im.ncc(np.transpose([-0.5, 0, 0.5]))

# 4:33
#mv.Kernel.Sobel()

# 4:55
# Currently no isobel equivalent functionality for the machine vision toolbox

# 5:22
im = mv.Image.Read('penguins.png', rgb = False, dtype = "float32")

# 5:24
im.disp()

# 6:58
# Currently no isobel equivalent functionality for the machine vision toolbox