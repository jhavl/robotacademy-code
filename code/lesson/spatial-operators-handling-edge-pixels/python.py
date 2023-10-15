import machinevisiontoolbox as mv
import numpy as np

# 1:37
im = mv.Image.Read('monalisa.png', grey = True, dtype = 'float64')

s7 = im.convolve(K = np.ones((7,7)))

im.disp()

s7.disp()

s21 = im.convolve(K = np.ones((21,21)))

s21.disp()