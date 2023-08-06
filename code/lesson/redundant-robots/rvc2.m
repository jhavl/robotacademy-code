%% 1:50
T2 = transl(0.6, 0.2, 0) * rpy2tr(0, 180, 180, 'deg')

%% 2:07
mdl_hyper3d(20)

%% 2:09
h3d

%% 2:39
q = h3d.ikine(T2, qz)

%% 2:55
h3d.fkine(q)

%% 2:58
T2

%% 3:08
h3d.plot(q)

%% 3:13
hold on

%% 3:20
trplot(T2)
