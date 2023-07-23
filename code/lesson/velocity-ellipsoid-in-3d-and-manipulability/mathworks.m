%% 1:11
p560 = loadrobot("puma560");

qz = [0, 0, 0, 0, 0, 0];
config = homeConfiguration(p560)
config(1).JointPosition = qz(1);
config(2).JointPosition = qz(2);
config(3).JointPosition = qz(3);
config(4).JointPosition = qz(4);
config(5).JointPosition = qz(5);
config(6).JointPosition = qz(6);

J = geometricJacobian(p560,config,'link7')
%% 1:18
det(J)

%% 1:25
rank(J)

%% 1:40
qn = [0	0.785398163397448 3.14159265358979 0 0.785398163397448 0]
config = homeConfiguration(p560)
config(1).JointPosition = qn(1);
config(2).JointPosition = qn(2);
config(3).JointPosition = qn(3);
config(4).JointPosition = qn(4);
config(5).JointPosition = qn(5);
config(6).JointPosition = qn(6);

J = geometricJacobian(p560,config,'link7')

%% 1:46
det(J)

%% 1:49
rank(J)

%% 4:42
p560 = loadrobot("puma560");

%% 4:51
show(p560,config);

%% 6:02
qs = [0 0 -1.570796326794897 0 0 0]
config = homeConfiguration(p560)
config(1).JointPosition = qs(1);
config(2).JointPosition = qs(2);
config(3).JointPosition = qs(3);
config(4).JointPosition = qs(4);
config(5).JointPosition = qs(5);
config(6).JointPosition = qs(6);

show(p560,config);