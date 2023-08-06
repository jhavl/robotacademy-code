%% 0:17
p560 = loadrobot("puma560");

%% 0:33
qz = [0, 0, 0, 0, 0, 0];
config = homeConfiguration(p560)
config(1).JointPosition = qz(1);
config(2).JointPosition = qz(2);
config(3).JointPosition = qz(3);
config(4).JointPosition = qz(4);
config(5).JointPosition = qz(5);
config(6).JointPosition = qz(6);

show(p560,config);
%% 1:10
T = tform(se3([1,1,0],"trvec"))

%% 2:33
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
q = robotIK(T)

%% 2:43
config = homeConfiguration(p560)
config(1).JointPosition = q(1);
config(2).JointPosition = q(2);
config(3).JointPosition = q(3);
config(4).JointPosition = q(4);
config(5).JointPosition = q(5);
config(6).JointPosition = q(6);
show(p560,config);

%% 4:29
p560 = loadrobot("puma560");

%% 4:39
qz = [0, 0, 0, 0, 0, 0];
config = homeConfiguration(p560)
config(1).JointPosition = qz(1);
config(2).JointPosition = qz(2);
config(3).JointPosition = qz(3);
config(4).JointPosition = qz(4);
config(5).JointPosition = qz(5);
config(6).JointPosition = qz(6);

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
config = homeConfiguration(p560)
config(1).JointPosition = q(1);
config(2).JointPosition = q(2);
config(3).JointPosition = q(3);
config(4).JointPosition = q(4);
config(5).JointPosition = q(5);
config(6).JointPosition = q(6);
show(p560,config);