import machinevisiontoolbox as mv
import matplotlib.pyplot as plt
import numpy as np

# 7:54
K = mv.Kernel.Gauss(sigma=5, h=15)

# 8:05
mv.idisp(K)

# 8:21
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# 8:27
X = np.arange(-15, 16, 1)
Y = np.arange(-15, 16, 1)
X, Y = np.meshgrid(X, Y)
surf = ax.plot_surface(X, Y, K)
plt.show()

# 8:56
im = mv.Image.Read('monalisa.png', dtype = "float64", mono=True)

# 9:04
s = im.convolve(K)

# 9:09
s.disp()