% Due to the contopptraj function behaving slightly differently to the one
% in the robotics vision toolbox the graphs will not line up identically 

%% 1:58
first = [10;20]

%% 2:03
last = [30;10]

%% 2:17
vellim = [-1 1; -1 1];
acclim = [-.033 .033; -.033 .033];
[q,qd,qdd,t] = contopptraj([first,last],vellim, acclim);

%% 2:34
plot(t,q)

%% 2:52
[q,qd,qdd,t] = contopptraj([first,last],vellim, acclim);

%% 2:57
plot(t,qd)

%% 3:20
[q,qd,qdd,t] = contopptraj([first,last],vellim, acclim);

%% 3:22
plot(t,q)

%% 4:55
via = [40 60 20 40; 50 30 10 50] 

%% 5:22
[q,qd,qdd,t] = contopptraj(via,[-2 2; -2 2],[-1 1; -1 1]);

%% 5:41
plot(t,q)

%% 5:56
plot(q(1,:), q(2,:))

%% 7:56
[q,qd,qdd,t] = contopptraj(via,[-1 1; -3 3],[-1 1; -1 1]);

%% 8:32
plot(t,q)

%% 8:40
plot(q(1,:), q(2,:))
