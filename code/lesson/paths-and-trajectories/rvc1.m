%% 0:45
T0 = eye(4,4)

T1 = transl(1, 2, 3)* rpy2tr(0.6, 0.8, 1.4)

%% 1:26
trplot(T0)

%% 1:39
trplot(T1)

%% 1:53
tranimate(T0,T1)