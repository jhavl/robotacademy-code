%% 5:50  - 7:08

rotm(so2(0, "theta"))
rotm(so2(0.2, "theta"))
rotm(so2(30*(pi/180), "theta"))

R = ans

c1 = R(:, 1)
c2 = R(:, 2)

dot(c1, c2)
det(R)
inv(R)

R'

%% 7:26

plotTransforms(se2(R),FrameAxisLabels = "on")
