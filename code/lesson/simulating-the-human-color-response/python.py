import machinevisiontoolbox as mv
import numpy as np
import matplotlib.pyplot as plt

# 0:13
nm = 1e-9

# 0:34
lam = np.linspace(350, 800, int((800-350+5)/5))*nm

# 0:54
E = mv.loadspectrum(lam, 'solar')

# 1:07
plt.plot(lam, E)
plt.show()

# 1:30
R = mv.loadspectrum(lam, 'redbrick')

# 1:41
plt.plot(lam, R)
plt.show()

# 2:13
L = np.multiply(E, R)

# 2:23
plt.plot(lam, L)
plt.show()

# 2:52
cones = mv.loadspectrum(lam, 'cones')

# 3:11
plt.plot(lam, cones)
plt.show()

# 3:41
plt.plot(lam, np.multiply(L, np.transpose(cones)[0]))
plt.show()

# 4:06
plt.plot(lam, np.multiply(L, np.transpose(cones)[1]))
plt.show()

# 4:24
plt.plot(lam, np.multiply(L, np.transpose(cones)[2]))
plt.show()

# 5:04
print(np.sum(np.multiply(L,np.transpose(cones)[0])*5*nm))

# 5:09
print(np.sum(np.multiply(L,np.transpose(cones)[1])*5*nm))

# 5:15
print(np.sum(np.multiply(L,np.transpose(cones)[2])*5*nm))