import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

# 2:26
first = 10

# 2:31
last = 30

# 2:38
via = np.asarray([[40],[10],[last]])

# 3:11
traj = rtb.mstraj(via, 0.1, 2, qdmax = 1, q0 = first)
plt.plot(traj.q)
plt.show()

# 3:28
traj = rtb.mstraj(via, 0.1, 4, qdmax = 1, q0 = first)
plt.plot(traj.q)
plt.show()

# 3:39
traj = rtb.mstraj(via, 0.1, 8, qdmax = 1, q0 = first)
plt.plot(traj.q)
plt.show()

# 3:54
traj = rtb.mstraj(via, 0.1, 0, qdmax = 1, q0 = first)
plt.plot(traj.q)
plt.show()

# 4:03
traj = rtb.mstraj(via, 0.1, 4, qdmax = 1, q0 = first)
plt.plot(traj.q)
plt.show()

# 4:19
traj = rtb.mstraj(via, 0.1, 4, qdmax = 2, q0 = first)
plt.plot(traj.q)
plt.show()

# 4:49
traj = rtb.mstraj(via, 0.1, 4, tsegment = [10, 30, 20], q0 = first)
plt.plot(traj.q)
plt.show()