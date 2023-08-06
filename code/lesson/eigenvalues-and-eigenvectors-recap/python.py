import numpy as np

# 3:00
A = np.asarray([[1,3],[0,-2]])
print(A,"\n")

# 3:06
print(np.linalg.eig(A),"\n")

#3:19
e, x = np.linalg.eig(A)
print(x,"\n")
print(e,"\n")

# 3:56
print(np.matmul(A,x[:,0]),"\n")

# 4:28
print(np.matmul(A,x[:,1]),"\n")