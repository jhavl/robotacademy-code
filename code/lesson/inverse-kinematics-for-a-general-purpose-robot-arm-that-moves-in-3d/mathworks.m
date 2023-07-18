%% 0:15
p560 = loadrobot("puma560");

%% 0:47
qz = [0, 0, 0, 0, 0, 0];
config = homeConfiguration(p560)
config(1).JointPosition = qz(1);
config(2).JointPosition = qz(2);
config(3).JointPosition = qz(3);
config(4).JointPosition = qz(4);
config(5).JointPosition = qz(5);
config(6).JointPosition = qz(6);

show(p560,config);

%% 1:49
T1 = tform(se3([0.6,0.1,0],"trvec"))*eul2tform([0,pi,0])

%% 2:05
hold on

%% 2:08
plotTransforms(se3(T1))

%% 2:57
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(T1)

%% 3:11 - 4:05
show(p560,ikConfig);

%% 4:42
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(T1)

%% 4:47
show(p560,ikConfig);

%% 5:03
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(T1)

%% 5:10
show(p560,ikConfig);

%% 5:28
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(T1)

%% 5:32
show(p560,ikConfig);