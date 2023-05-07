%% 1:12
mdl_puma560

%% 1:26
T = transl(0.6, 0.1, 0) * rpy2tr(0, 180, 0, 'deg')

%% 1:55
ql = p560.ikine6s(T,'l')

%% 2:05
qr = p560.ikine6s(T,'r')

%% 2:13
p560.plot(ql)

%% 2:22
p560.plot(qr)

%% 2:45
tg = jtraj(qz, ql, 50);

%% 3:09
p560.plot(tg)

%% 3:23
tg = jtraj(qz, qr, 50);

%% 3:24
p560.plot(tg)

%% 3:56
tg = jtraj(ql, qr, 50);

%% 4:00
p560.plot(tg)