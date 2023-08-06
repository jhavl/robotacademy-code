import roboticstoolbox as rtb

# 3:22
p560 = rtb.models.Puma560()

# 3:43
J = p560.jacobe(p560.qn)
print(J, "\n")

# 3:48
print(p560.qn, "\n")
