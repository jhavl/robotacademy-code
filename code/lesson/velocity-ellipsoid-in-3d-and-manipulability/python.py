import roboticstoolbox as rtb
import numpy as np

# 1:11
p560 = rtb.models.Puma560()

J = p560.jacobe(p560.qz)
print(J, "\n")

# 1:18
print(np.linalg.det(J), "\n")

# 1:25
print(np.linalg.matrix_rank(J), "\n")

# 1:40
J = p560.jacobe(p560.qn)

# 1:46
print(np.linalg.det(J), "\n")

# 1:49
print(np.linalg.matrix_rank(J), "\n")

# 4:42
p560 = rtb.models.Puma560()

# 4:51
p560.plot(p560.qn)

# 5:23
# Ellipse plotting of ERobot's is not currently implemented yet

# 6:02
p560.plot(p560.qs)

# 6:16
# Ellipse plotting of ERobot's is not currently implemented yet
