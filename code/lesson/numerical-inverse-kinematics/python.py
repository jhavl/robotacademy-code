import roboticstoolbox as rtb
import spatialmath as sm
import spatialmath.base as smb

# 0:17
p2 = rtb.models.DH.Planar2()

# 0:33
p2.plot(p2.qz)

# 1:10
T = sm.SE3.Trans(1, 1, 0.0)

# 2:33
q = p2.ikine_LM(T, q0 = [0, 0], mask =[1, 1, 0, 0, 0, 0])
print(q.q)

# 2:43
p2.plot(q.q)

# 3:22
q = p2.ikine_LM(T, q0 = [-1, 0], mask =[1, 1, 0, 0, 0, 0])
print(q.q)

# 3:36
q = p2.ikine_LM(T, q0 = [-1, -1], mask =[1, 1, 0, 0, 0, 0])
print(q.q)

# 3:45
p2.plot(q.q)

# 4:29
p560 = rtb.models.DH.Puma560()

# 4:39
p560.plot(p560.qz)

# 5:07
T2 = sm.SE3.Trans(0.6, 0.2, 0.0) * sm.SE3(smb.rpy2tr(0, 180, 180, unit = 'deg'))
print(T2.A, "\n")

# 5:21
smb.trplot(T2.A)

# 5:49
q = p560.ikine_LM(T2, mask =[0, 0, 0, 0, 0, 0])

# 6:01
p560.plot(q.q)