%% 5:14 - 11:17

tform(se2([1,2],"trvec"))

rotm(so2(30*(pi/180), 'theta'))

tform(se2(30*(pi/180), 'theta'))

tform(se2([1,2],"trvec")) * tform(se2(30*(pi/180), 'theta'))

tform(se2(30*(pi/180),"theta",[1,2]))

axis([0 5 0 5])

axis square
hold on

T1 = tform(se2(30*(pi/180),"theta",[1,2]))

plotTransforms(se2(T1),Framecolor = "blue",FrameAxisLabels = "on")

T2 = tform(se2([2,1],"trvec"))

plotTransforms(se2(T2),Framecolor = "red",FrameAxisLabels = "on")

T3 = T1 * T2

plotTransforms(se2(T3),Framecolor = "green",FrameAxisLabels = "on")

T4 = T2 * T1

plotTransforms(se2(T4),Framecolor = "cyan",FrameAxisLabels = "on")

P = [3 2]'

plot(P(1),P(2),'b*')

P1 = inv(T1) * [P ; 1]
