% Currently the inverse kinematics solver is producing different values or
% not working compared to the one implemented in the robotic vision
% toolbox, this issue is being investigated.

%% 10:41
p560 = loadrobot("puma560");
p560.DataFormat = "row";

%% 10:47
p560

%% 11:11
qz = [0, 0, 0, 0, 0, 0];
config = qz

show(p560,config);
%% 11:21
qr = [0, 1.570796326794897, -1.570796326794897, 0, 0, 0];
config = qr

show(p560,config);

%% 12:12
eePosition = [0.1 0.2 0.3];
eePose = trvec2tform(eePosition);
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(eePose)