import machinevisiontoolbox as mv

# 2:22
#K = [-0.5, 0, 0.5]
#im.convolve(K).disp(colormap="signed")

# 3:35
#K = np.transpose([-0.5, 0, 0.5])
#im.convolve(K).disp(colormap="signed")

# 4:33
#Du = mv.Kernel.Sobel()

# 4:55
# Currently no isobel equivalent functionality for the machine vision toolbox

# 5:22
im = mv.Image.Read('penguins.png', rgb = False, dtype = "float32")

# 5:24
im.disp()

# 6:58
# Currently no isobel equivalent functionality for the machine vision toolbox