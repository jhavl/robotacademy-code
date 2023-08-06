import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import numpy as np

# 1:58
first = [10, 20]
print(first, "\n")

# 2:03
last = [30, 10]
print(last, "\n")

# 2:17
x = rtb.jtraj(first, last, 50)

# 2:34
x.plot()

# 2:52
x = rtb.jtraj(first, last, 50)

# 2:57
x.plot()

# 3:20
x = rtb.jtraj(first, last, 50, qd0 = [0, 0], qd1 = [10, 10])

# 3:22
x.plot()

# 4:39
start = [40, 50]

# 4:55
via = np.asarray([[60, 30], [40, 10], [20, 30], start])

# 5:22
x = rtb.mstraj(via, 0.1, 1, qdmax = 2, q0 = start)

# 5:41
plt.figure()
plt.plot(x.q[:,:])
plt.show()

# 5:56
plt.figure()
plt.plot(x.q[:,0],x.q[:,1])
plt.show()

# 7:56
x = rtb.mstraj(via, 0.1, 1, qdmax = [1, 3], q0 = start)

# 8:32
plt.figure()
plt.plot(x.q[:,:])
plt.show()

# 8:40
plt.figure()
plt.plot(x.q[:,0],x.q[:,1])
plt.show()