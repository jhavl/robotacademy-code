% Currently the inverse kinematics solver is producing different values or
% not working compared to the one implemented in the robotic vision
% toolbox, this issue is being investigated.

%% 0:17
p560 = loadrobot("puma560");
p560.DataFormat = "row";

%% 0:33
qz = [0, 0, 0, 0, 0, 0];
config = qz

show(p560,config);
%% 1:10
T = tform(se3([1,1,0],"trvec"))

%% 2:33
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
q = robotIK(T)

%% 2:43
config = q
show(p560,config);

%% 4:29
p560 = loadrobot("puma560");

%% 4:39
qz = [0, 0, 0, 0, 0, 0];
config = qz

show(p560,config);

%% 5:07
T2 = tform(se3([0.6,0.2,0],"trvec"))*eul2tform([0,pi,pi])

%% 5:15
hold on

%% 5:21
plotTransforms(se3(T2))

%% 5:49
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
q = robotIK(T2)

%% 6:01
config = q
show(p560,config);