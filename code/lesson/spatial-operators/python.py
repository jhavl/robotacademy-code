import machinevisiontoolbox as mv
import numpy as np

# 3:36
im = mv.Image.Read('monalisa.png', grey = True, dtype = 'float64')

# 4:36
s7 = im.convolve(K = np.ones((7,7)))

# 4:42
im.disp()

# 4:47
s7.disp()

# 5:16
s21 = im.convolve(K = np.ones((21,21)))

# 5:22
s21.disp()