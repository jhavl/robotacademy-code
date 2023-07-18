%% 10:41
p560 = loadrobot("puma560");

%% 10:47
p560

%% 11:11
qz = [0, 0, 0, 0, 0, 0];
config = homeConfiguration(p560)
config(1).JointPosition = qz(1);
config(2).JointPosition = qz(2);
config(3).JointPosition = qz(3);
config(4).JointPosition = qz(4);
config(5).JointPosition = qz(5);
config(6).JointPosition = qz(6);

show(p560,config);
%% 11:21
qr = [0, 1.570796326794897, -1.570796326794897, 0, 0, 0];
config = homeConfiguration(p560)
config(1).JointPosition = qr(1);
config(2).JointPosition = qr(2);
config(3).JointPosition = qr(3);
config(4).JointPosition = qr(4);
config(5).JointPosition = qr(5);
config(6).JointPosition = qr(6);

show(p560,config);

%% 12:12
eePosition = [0.1 0.2 0.3];
eePose = trvec2tform(eePosition);
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(eePose)