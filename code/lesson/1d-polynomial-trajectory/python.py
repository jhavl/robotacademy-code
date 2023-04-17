import roboticstoolbox as rtb

# 3:07 - 4:40
print(rtb.tools.trajectory.quintic(0, 1, 50).s, "\n")
rtb.tools.trajectory.quintic(0, 1, 50).plot()

print(rtb.tools.trajectory.quintic(0, -1, 50).s, "\n")
rtb.tools.trajectory.quintic(0, -1, 50).plot()

tg = rtb.tools.trajectory.quintic(0, 1, 50)

tg = rtb.tools.trajectory.quintic(0, 1, 50)
print(tg.s, "\n")
print(tg.sd, "\n")
print(tg.sdd, "\n")

print(rtb.tools.trajectory.quintic(0, 1, 50, 0.5, 0).s)
rtb.tools.trajectory.quintic(0, 1, 50, 0.5, 0).plot()
