% The geometric jacaobian and transform function currently do not produce
% the same coordinates and values as those from the robotics vision
% toolbox. This issue is being investigated currently.

%% 3:22
p560 = loadrobot("puma560");
p560.DataFormat = "row";

%% 3:43
qn = [0	0.7853	3.1415	0	0.7853	0];
config = qn;

J = geometricJacobian(p560,config,'link6')

%% 3:48
qn