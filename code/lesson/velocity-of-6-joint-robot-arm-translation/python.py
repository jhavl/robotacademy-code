import roboticstoolbox as rtb

# 3:19
p560 = rtb.models.DH.Puma560()

# 3:41
p560.plot(p560.qn)

# 3:59
T = p560.fkine(p560.qn)
print(T, "\n")

# 4:28
Td = p560.fkine(p560.qn + [0.01, 0, 0, 0, 0, 0])
print(Td, "\n")
