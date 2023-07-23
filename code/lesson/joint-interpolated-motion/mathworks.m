%% 0:51
p560 = loadrobot("puma560");

%% 1:11
TA = tform(se3([0.4,0.2,0],"trvec"))*eul2tform([0,0,pi])

%% 1:32
TB = tform(se3([0.4,-0.2,0],"trvec"))*eul2tform([0,0,pi/2])

%% 1:44
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
qA = robotIK(TA)

%% 1:52
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
qB = robotIK(TB)

%% 2:04
[tg,vel,acc] = transformtraj(qA,qB,[0 1],0:0.01:1)




