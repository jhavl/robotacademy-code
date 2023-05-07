%% 0:15
mdl_puma560

%% 0:47
p560.plot(qz)

%% 1:49
T = transl(0.6, 0.1, 0) * rpy2tr(0, 180, 0, 'deg')

%% 2:05
hold on

%% 2:08
trplot(T)

%% 2:57
q = p560.ikine6s(T)

%% 3:11
p560.plot(q)

%% 4:05
p560.plot3d(q)

%% 4:42
q = p560.ikine6s(T, 'r')

%% 4:47
p560.plot3d(q)

%% 5:03
q = p560.ikine6s(T, 'rd')

%% 5:10
p560.plot3d(q)

%% 5:28
q = p560.ikine6s(T, 'ld')

%% 5:32
p560.plot3d(q)