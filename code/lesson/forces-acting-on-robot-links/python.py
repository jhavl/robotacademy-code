import roboticstoolbox as rtb

# 7:08
twolink = rtb.models.DH.Planar2()

# 7:33
twolink.plot([0, 0])

# 8:22
tau = twolink.rne([0, 0], qd = [0, 0], qdd = [0, 0])

# 9:03
twolink.plot([0, 0])
