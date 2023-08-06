import machinevisiontoolbox as mv
import numpy as np

# 2:49
cam = mv.CentralCamera().Default()

J = cam.visjac_p([600, 600], 5)
print(J, "\n")

print(np.matmul(J, [[1], [0], [0], [0], [0], [0]]), "\n")

print(np.matmul(J, [[0], [1], [0], [0], [0], [0]]), "\n")

print(np.matmul(J, [[0], [0], [1], [0], [0], [0]]), "\n")

# 3:06
J = cam.visjac_p([512, 512], 5)

# 3:16
print(np.matmul(J, [[1], [0], [0], [0], [0], [0]]), "\n")

# 3:30
print(np.matmul(J, [[0], [1], [0], [0], [0], [0]]), "\n")

# 3:49
print(np.matmul(J, [[0], [0], [1], [0], [0], [0]]), "\n")
