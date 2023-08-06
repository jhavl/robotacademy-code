%% 3:19
p560 = loadrobot("puma560");

%% 3:41
qn = [0	0.785398163397448 3.14159265358979 0 0.785398163397448 0]
config = homeConfiguration(p560)
config(1).JointPosition = qn(1);
config(2).JointPosition = qn(2);
config(3).JointPosition = qn(3);
config(4).JointPosition = qn(4);
config(5).JointPosition = qn(5);
config(6).JointPosition = qn(6);

show(p560,config);

%% 3:59
T = getTransform(p560,config,'link7')

%% 4:28
config(1).JointPosition = qn(1)+0.01;

Td = getTransform(p560,config,'link7')
