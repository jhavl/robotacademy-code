import roboticstoolbox as rtb

# 2:13 - 4:09
print(rtb.tools.trajectory.trapezoidal(0, 1, 50).s, "\n")
rtb.tools.trajectory.trapezoidal(0, 1, 50).plot()

print(rtb.tools.trajectory.trapezoidal(0, -1, 50).s, "\n")
rtb.tools.trajectory.trapezoidal(0, -1, 50).plot()

tg = rtb.tools.trajectory.trapezoidal(0, 1, 50)
print(tg.s)

tg = rtb.tools.trajectory.trapezoidal(0, 1, 50)
print(tg.s, "\n")
print(tg.sd, "\n")
print(tg.sdd, "\n")

print(rtb.tools.trajectory.trapezoidal(0, 1, 50).s, "\n")
rtb.tools.trajectory.trapezoidal(0, 1, 50).plot()

print(rtb.tools.trajectory.trapezoidal(0, 1, 50, 0.025).sd, "\n")
rtb.tools.trajectory.trapezoidal(0, 1, 50, 0.025).plot()

print(rtb.tools.trajectory.trapezoidal(0, 1, 50, 0.035).sd, "\n")
rtb.tools.trajectory.trapezoidal(0, 1, 50, 0.035).plot()

print(rtb.tools.trajectory.trapezoidal(0, 1, 50, 0.02).sd, "\n")
rtb.tools.trajectory.trapezoidal(0, 1, 50, 0.02).plot()
