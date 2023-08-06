import roboticstoolbox as rtb

# 3:00
p2 = rtb.models.DH.Planar2()

p2.plot([0.1, 0.1], limits = [-3, 3, -3, 3, -1, 1])

p2.teach()