%% 5:40
p560 = loadrobot("puma560");
p560.DataFormat = 'row';

%% 3:43
qz = [0	0 0 0 0 0]
p560.Gravity = [0 0 -9.81]

%% 5:57
show(p560,config);

%% 6:08
gravityTorque(p560,qz)

%% 6:37
p560.Gravity = [0 0 -9.81/6]

%% 6:50
gravityTorque(p560,qz)