%% 1:11 - 2:26
T0 = eye(4,4)

T1 = transl(1,2,3) * rpy2tr(0.6,0.8,1.4)

T = ctraj(T0,T1,50);

T(:,:,1)

T(:,:,10)

tranimate(T)