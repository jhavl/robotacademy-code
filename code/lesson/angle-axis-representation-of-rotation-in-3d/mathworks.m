%% 1:32 - 4:03

R = eul2rotm([0.1, 0.2, 0.3],"ZYZ") % using ZYZ creates the correct values

plotTransforms(se3(R))

eig(R)

[v,e] = eig(R)

rotm2axang(R)

Rotation = rotm2axang(R);

th = Rotation(4)
v = Rotation(1:3)
%% 4:03

axang2rotm([v,th])
