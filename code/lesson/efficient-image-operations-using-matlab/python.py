import machinevisiontoolbox as mv
import numpy as np

# 1:50
m = np.round(np.random.rand(4,4)*10)
print(m, "\n")

# 2:03
print(m+1, "\n")

# 2:13
print(m*2, "\n")

# 2:27
print(np.sqrt(m), "\n")

# 2:43
print(np.power(m,np.ones((4,4))*2), "\n")

# 2:52
print(np.linalg.matrix_power(m, 2), "\n")

# 2:59
print(np.matmul(m, m), "\n")
