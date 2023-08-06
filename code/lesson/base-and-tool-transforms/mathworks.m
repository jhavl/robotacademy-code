%% 2:20
p560 = loadrobot("puma560");

p560

eePosition = [0.1 0.2 0.3];
eePose = trvec2tform(eePosition);
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(eePose)

%% 3:02

%% 3:14
eePosition = [0.1 0.2 0.3];
eePose = trvec2tform(eePosition);
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(eePose)

%% 3:32

%% 3:39
eePosition = [0.1 0.2 0.3];
eePose = trvec2tform(eePosition);
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(eePose)

%% 4:18

%% 4:32
eePosition = [0.1 0.2 0.3];
eePose = trvec2tform(eePosition);
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ikConfig = robotIK(eePose)