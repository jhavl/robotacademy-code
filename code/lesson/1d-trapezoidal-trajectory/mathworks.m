%% 2:13 - 4:09

trapveltraj([0 1],50)

trapveltraj([0 -1],50)

s = trapveltraj([0 1],50)

[s,sd,sdd] = trapveltraj([0 1],50)

subplot(3,1,1)
plot(s)
subplot(3,1,2)
plot(sd)
subplot(3,1,3)
plot(sdd)

trapveltraj([0 1],50)

[s,sd,sdd] = trapveltraj([0 1],50,"PeakVelocity",0.025)

subplot(3,1,1)
plot(s)
subplot(3,1,2)
plot(sd)
subplot(3,1,3)
plot(sdd)

[s,sd,sdd] = trapveltraj([0 1],50,"PeakVelocity",0.035)

subplot(3,1,1)
plot(s)
subplot(3,1,2)
plot(sd)
subplot(3,1,3)
plot(sdd)

[s,sd,sdd] = trapveltraj([0 1],50,"PeakVelocity",0.02)

subplot(3,1,1)
plot(s)
subplot(3,1,2)
plot(sd)
subplot(3,1,3)
plot(sdd)