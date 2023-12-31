%% 1:12
p560 = loadrobot("puma560");
p560.DataFormat = "row";


%% 1:26
T1 = tform(se3([0.6,0.1,0],"trvec"))*eul2tform([0,pi,0])

%% 1:55
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
ql = robotIK(T1)

%% 2:05
aik = analyticalInverseKinematics(p560);
aik.KinematicGroup
generateIKFunction(aik,'robotIK');
qr = robotIK(T1)

%% 2:13
show(p560,ql);

%% 2:22
show(p560,qr);

%% 2:45
qz = [0, 0, 0, 0, 0, 0];
config = qz

vellim = [-1 1];
acclim = [-1 1];
[q,qd,qdd,t] = contopptraj([config,ql],vellim, acclim);

%% 3:09
show(p560,ql); % Mathworks Robotics Toolbox does not have equivalent support for animations of the robot 

%% 3:23
[q,qd,qdd,t] = contopptraj([config,qr],vellim, acclim);

%% 3:24
show(p560,qr); % Mathworks Robotics Toolbox does not have equivalent support for animations of the robot 

%% 3:56
[q,qd,qdd,t] = contopptraj([ql,qr],vellim, acclim);

%% 4:00
show(p560,qr); % Mathworks Robotics Toolbox does not have equivalent support for animations of the robot 