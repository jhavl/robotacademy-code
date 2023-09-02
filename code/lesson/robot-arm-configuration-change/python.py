import roboticstoolbox as rtb
import spatialmath as sm
import spatialmath.base as smb

# 1:12
p560 = rtb.models.DH.Puma560()

#T = sm.SE3.Trans(0.6, 0.1, 0.0) * sm.SE3(smb.rpy2tr(0, 180, 0, unit = 'deg'))
print(T, "\n")

# 1:55
ql = p560.ikine_a(T, config = 'l')
print(ql.q, "\n")

# 2:05
qr = p560.ikine_a(T, config = 'r')
print(qr.q, "\n")

# 2:13
p560.plot(ql.q)

# 2:22
p560.plot(qr.q)

# 2:45
tg = rtb.jtraj(p560.qz, ql.q, 50)

# 3:09
p560.plot(tg.q)

# 3:23
tg = rtb.jtraj(p560.qz, qr.q, 50)

# 3:24
p560.plot(tg.q)

# 3:56
tg = rtb.jtraj(ql.q, qr.q, 50)

# 4:00
p560.plot(tg.q)