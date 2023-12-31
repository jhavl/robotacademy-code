%% 3:19
p560 = loadrobot("puma560");
p560.DataFormat = "row";

%% 3:41
qn = [0	0.7853	3.1415	0	0.7853	0];
config = qn;

show(p560,config);

%% 3:59
T = getTransform(p560,config,'link7')

%% 4:28
config(2) = config(2)+0.01;

Td = getTransform(p560,config,'link7')
