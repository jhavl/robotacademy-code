%% 1:05
mdl_puma560

TA = transl(0.4, 0.2, 0) * trotx(pi)

TB = transl(0.4, -0.2, 0) * trotx(pi/2)

qA = p560.ikine6s(TA)

qB = p560.ikine6s(TB)

tg = jtraj(qA, qB, 50);

p560.plot(tg)

figure

qplot(tg)

%% 1:28
Ts = ctraj(TA, TB, 50);

%% 1:55
Ts(:, :, 1)

%% 2:02
Ts(:, :, 2)

%% 2:05
Ts(:, :, 3)

%% 2:27
qs = p560.ikine6s(Ts);

%% 2:44
figure(1)

%% 2:51
p560.plot(qs)

%% 2:59
figure(2)

%% 3:04
qplot(qs)