from spatialmath.base import*

import numpy as np
import matplotlib.pyplot as plt

# 5:50

print(rot2(0),"\n")

# 6:03

print(rot2(0.2),"\n")

# 6:12 , 6:18

R = rot2(30, 'deg')
print(R,"\n")

# 6:37

c1 = R[:,0]

print(c1,"\n")

# 6:42

c2 = R[:,1]

print(c2,"\n")

# 6:48

print(np.dot(c1,c2),"\n")

# 6:54

print(np.linalg.det(R),"\n")

# 7:05

print(np.linalg.inv(R),"\n")

# 7:08

print(np.transpose(R),"\n")

# 7:26

trplot2(R)
plt.xlim(-1,1.5)
plt.ylim(-1,1.5)
plt.show()
