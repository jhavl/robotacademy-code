import machinevisiontoolbox as mv
import numpy as np
import matplotlib.pyplot as plt

# 5:02
nm = 1e-9

# 5:25
lam = np.linspace(300, 1000, int((1000-300+10)/10))*nm

# 5:41
E = mv.blackbody(lam, 6500)

# 5:56
plt.plot(lam, E)
plt.show()

# 6:09
plt.plot(lam, E)
E = mv.blackbody(lam, 6000)

# 6:23
plt.plot(lam, E,'--')
plt.show()
