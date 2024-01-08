% Currently the inverse kinematics solver is producing different values or
% not working compared to the one implemented in the robotic vision
% toolbox, this issue is being investigated.

%% 1:05
p560 = loadrobot("puma560");
p560.DataFormat = "row";

TA = tform(se3([0.4,0.2,0],"trvec"))*eul2tform([0,0,pi])

TB = tform(se3([0.4,-0.2,0],"trvec"))*eul2tform([0,0,pi/2])

%% 1:28
[Ts,vel,acc] = transformtraj(TA,TB,[0 1],0:0.02:1)

%% 1:55
Ts(:, :, 1)

%% 2:02
Ts(:, :, 2)

%% 2:05
Ts(:, :, 3)

%% 2:27
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
qs = robotIK(Ts(:,:,end))

%% 2:44
figure(1)

%% 2:51
config = qs

show(p560,config);
