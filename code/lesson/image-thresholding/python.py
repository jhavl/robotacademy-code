import machinevisiontoolbox as mv
import numpy as np
import matplotlib.pyplot as plt

# 2:06
print(2 > 1, "\n")

# 2:41
print(1 > 2, "\n")

# 2:52
print(True, "\n")

# 2:57
print(False, "\n")

# 3:05
print(1 == 2, "\n")

# 3:11
print(2 == 2, "\n")

# 3:20
a = 2 == 3
print(a, "\n")

# 4:13
m = np.round(np.random.rand(4,4)*10)
print(m, "\n")

# 4:19
print(m > 5, "\n")

# 5:03
print(m == 3, "\n")

# 5:12
im = mv.Image.Read('penguins.png', grey = True, dtype = 'float32')

im.disp()

hist = im.hist()
hist.plot()

# 5:34
b = im > 0.45

# 5:55
b.disp()

# 6:55
b = im > 0.6

# 7:01
b.disp()

# 7:21
im.threshold_interactive()

input("Press any key to exit")