%% 0:17
mdl_planar2

%% 0:33
p2.plot(qz)

%% 1:10
T = transl(1, 1, 0)

%% 2:33
q = p2.ikine(T, [0 0], [1 1 0 0 0 0])

%% 2:43
p2.plot(q)

%% 3:22
q = p2.ikine(T, [-1 0], [1 1 0 0 0 0])

%% 3:36
q = p2.ikine(T, [-1 -1], [1 1 0 0 0 0])

%% 3:45
p2.plot(q)

%% 4:29
mdl_puma560

%% 4:39
p560.plot(qz)

%% 5:07
T2 = transl(0.6, 0.2, 0) * rpy2tr(0, 180, 180, 'deg')

%% 5:15
hold on

%% 5:21
trplot(T2)

%% 5:49
q = p560.ikine(T2, [0 0 0 0 0 0])

%% 6:01
p560.plot(q)