%% 1:05
p560 = loadrobot("puma560");

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
config = homeConfiguration(p560)
config(1).JointPosition = qs(1);
config(2).JointPosition = qs(2);
config(3).JointPosition = qs(3);
config(4).JointPosition = qs(4);
config(5).JointPosition = qs(5);
config(6).JointPosition = qs(6);

show(p560,config);
