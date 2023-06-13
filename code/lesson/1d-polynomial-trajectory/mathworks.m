%% 3:07 - 4:40

quinticpolytraj([0 1], 0:1, 0:(1/49):1)
quinticpolytraj([0 -1], 0:1, 0:(1/49):1)

s = quinticpolytraj([0 1], 0:1, 0:(1/49):1)

[s, sd, sdd, ~] = quinticpolytraj([0 1], 0:1, 0:(1/49):1)

subplot(3,1,1)
plot(s)

subplot(3,1,2)
plot(sd)

subplot(3,1,3)
plot(sdd)

quinticpolytraj([0 1],0:1,0:(1/49):1, "VelocityBoundaryCondition") 
