import machinevisiontoolbox as mv
import numpy as np

# 1:37
im = mv.Image.Read('monalisa.png', grey = True, dtype = 'float64')

K = np.ones((7,7))
s7 = im.convolve(K)

im.disp()

s7.disp()

K = np.ones((21,21))
s21 = im.convolve(K)

s21.disp()