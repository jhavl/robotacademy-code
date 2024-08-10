import roboticstoolbox as rtb

# 7:46
r = rtb.models.DH.TwoLink()

# 8:27
print(r, "\n")

# 8:59
r.plot([0.2, 0.3])

# 9:05
r.teach()

# 9:30
r.fkine([0.2, 0.3])

# 10:41
p560 = rtb.models.DH.Puma560()

# 10:47
print(p560, "\n")

# 11:11
p560.plot(p560.qz)

# 11:21
p560.plot(p560.qr)

# 11:30
p560.teach()

# 12:12
print(p560.fkine([0.1, 0.2, 0.3, 0, 0, 0]), "\n")
