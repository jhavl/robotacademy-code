import roboticstoolbox as rtb
import spatialmath.base as smb
import spatialmath as sm

# 0:15
p560 = rtb.models.DH.Puma560()

# 0:47
p560.plot(p560.qz)

# 1:49
T = sm.SE3.Trans(0.6, 0.1, 0) * sm.SE3(smb.rpy2tr(0, 180, 0, 'deg'))
print(T, "\n")

# 2:08
smb.trplot(T.A)

# 2:57
q = p560.ikine_a(T)
print(q.q)

# 3:11
p560.plot(q.q)

# 4:05
# Python robotics toolbox does not have plot3d functionality

# 4:42
q = p560.ikine_a(T, config = 'r')
print(q.q)

# 4:47
# Python robotics toolbox does not have plot3d functionality, instead using plot
p560.plot(q.q)

# 5:03
q = p560.ikine_a(T, config = 'rd')
print(q.q)

# 5:10
# Python robotics toolbox does not have plot3d functionality, instead using plot
p560.plot(q.q)

# 5:28
q = p560.ikine_a(T, config = 'ld')
print(q.q)

# 5:32
# Python robotics toolbox does not have plot3d functionality, instead using plot
p560.plot(q.q)