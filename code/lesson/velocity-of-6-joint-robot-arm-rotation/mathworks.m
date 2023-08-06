%% 3:22
p560 = loadrobot("puma560");

%% 3:43
qn = [0	0.785398163397448 3.14159265358979 0 0.785398163397448 0]
config = homeConfiguration(p560)
config(1).JointPosition = qn(1);
config(2).JointPosition = qn(2);
config(3).JointPosition = qn(3);
config(4).JointPosition = qn(4);
config(5).JointPosition = qn(5);
config(6).JointPosition = qn(6);

J = geometricJacobian(p560,config,'link7')

%% 3:48
qn