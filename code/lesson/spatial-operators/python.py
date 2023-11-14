import machinevisiontoolbox as mv
import numpy as np

# 3:36
im = mv.Image.Read('monalisa.png', grey = True, dtype = 'float64')

# 4:36
K = np.ones((7,7))
s7 = im.convolve(K)

# 4:42
im.disp()

# 4:47
s7.disp()

# 5:16
K = np.ones((21,21))
s21 = im.convolve(K)

# 5:22
s21.disp()