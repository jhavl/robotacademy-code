%% 0:51
mdl_puma560

%% 1:11
TA = transl(0.4, 0.2, 0) * trotx(pi)

%% 1:32
TB = transl(0.4, -0.2, 0) * trotx(pi/2)

%% 1:44
qA = p560.ikine6s(TA)

%% 1:52

qB = p560.ikine6s(TB)

%% 2:04
tg = jtraj(qA, qB, 50);

%% 2:25
p560.plot(tg)

%% 2:38
figure

%% 2:43
qplot(tg)
