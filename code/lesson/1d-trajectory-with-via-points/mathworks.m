%% 2:26
first = 10

%% 2:31
last = 30

%% 2:38
via = [first, 40, 10, last]

%% 3:11
[q,qd,qdd,t] = contopptraj(via,[-1 1],[-2 2],NumSamples=100);
plot(t,q)

%% 3:28
[q,qd,qdd,t] = contopptraj(via,[-1 1],[-1 1],NumSamples=100);
plot(t,q)

%% 3:39
[q,qd,qdd,t] = contopptraj(via,[-1 1],[-0.5 0.5],NumSamples=100);
plot(t,q)

%% 3:54
[q,qd,qdd,t] = contopptraj(via,[-1 1],[-100 100],NumSamples=100);
plot(t,q)

%% 4:03
[q,qd,qdd,t] = contopptraj(via,[-1 1],[-1 1],NumSamples=100);
plot(t,q)

%% 4:19
[q,qd,qdd,t] = contopptraj(via,[-1 1],[-1 1],NumSamples=100);
plot(t,q)

%% 4:49
tvec = 0:1:60;
[q,qd,qdd,pp] = cubicpolytraj(via, [0, 10, 40, 60], tvec);
plot(tvec,q)